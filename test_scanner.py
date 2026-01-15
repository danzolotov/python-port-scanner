import random
import socket
from unittest.mock import MagicMock, patch

import pytest

import scanner


@pytest.fixture(autouse=True)
def reset_globals():
    scanner.open_ports = []
    scanner.scanned_ports = set()
    scanner.queue = scanner.Queue()


random_start = str(random.randint(1, 512))
random_end = str(random.randint(513, 1024))
random_threads = str(random.randint(10, 100))


def test_arguments():
    test_args = [
        "scanner.py",
        "-t",
        "127.0.0.1",
        "-s",
        random_start,
        "-e",
        random_end,
        "--threads",
        random_threads,
    ]

    with patch.object(scanner.sys, "argv", test_args):
        args = scanner.get_arguments()
        assert args.target == "127.0.0.1"
        assert args.start_port == int(random_start)
        assert args.end_port == int(random_end)
        assert args.threads == int(random_threads)


def test_scan_port_open():
    target_port = random.randint(int(random_start), int(random_end))

    # Replace real socket with a fake one via mocking
    with patch("socket.socket") as MockSocket:
        mock_instance = MagicMock()
        # Setup context manager support
        mock_instance.__enter__ = MagicMock(return_value=mock_instance)
        mock_instance.__exit__ = MagicMock(return_value=None)

        MockSocket.return_value = mock_instance

        mock_instance.connect_ex.return_value = 0
        mock_instance.recv.return_value = b"Test Service\n"

        with patch.object(scanner, "target", "127.0.0.1"):
            scanner.scan_port(target_port)

    assert any(p["port"] == target_port for p in scanner.open_ports)


def test_scan_port_closed():
    target_port = random.randint(int(random_start), int(random_end))

    # Replace real socket with a fake one via mocking
    with patch("socket.socket") as MockSocket:
        mock_instance = MagicMock()
        # Setup context manager support
        mock_instance.__enter__ = MagicMock(return_value=mock_instance)
        mock_instance.__exit__ = MagicMock(return_value=None)

        MockSocket.return_value = mock_instance

        # Refuse connection
        mock_instance.connect_ex.return_value = 111

        with patch.object(scanner, "target", "127.0.0.1"):
            scanner.scan_port(target_port)

    assert not any(p["port"] == target_port for p in scanner.open_ports)
    assert target_port in scanner.scanned_ports


def test_integrity_logic():
    start = random.randint(1, 100)
    end = start + random.randint(10, 50)

    expected = set(range(start, end + 1))
    scanned = set(range(start, end + 1))

    # Test perfect match
    missing = expected - scanned
    assert len(missing) == 0

    # Test 1 missing port
    victim = random.choice(list(scanned))
    scanned.remove(victim)

    missing = expected - scanned
    assert victim in missing
    assert len(missing) == 1


def test_randomisation():
    mock_args = MagicMock(
        target="127.0.0.1",
        start_port=1,
        end_port=10,
        threads=1,
        randomise=True,
        output=None,
    )

    # Patch dependencies to isolate functionality
    with patch.object(scanner, "args", mock_args), patch.object(
        scanner, "target", "127.0.0.1"
    ), patch("scanner.random.shuffle") as mock_shuffle, patch(
        "scanner.socket.gethostbyname", return_value="127.0.0.1"
    ), patch(
        "scanner.threading.Thread"
    ) as mock_thread:

        scanner.run_scanner()
        mock_shuffle.assert_called_once()

    mock_args.randomise = False
    with patch.object(scanner, "args", mock_args), patch.object(
        scanner, "target", "127.0.0.1"
    ), patch("scanner.random.shuffle") as mock_shuffle, patch(
        "scanner.socket.gethostbyname", return_value="127.0.0.1"
    ), patch(
        "scanner.threading.Thread"
    ) as mock_thread:

        scanner.run_scanner()
        mock_shuffle.assert_not_called()


def test_port_range_start_greater_than_end():
    """
    Test that start_port > end_port is rejected.
    """

    mock_args = MagicMock(
        target="127.0.0.1",
        start_port=5000,
        end_port=1000,
        threads=1,
    )

    with patch.object(scanner, "args", mock_args), patch.object(
        scanner, "target", "127.0.0.1"
    ), patch("sys.exit", side_effect=SystemExit):
        with pytest.raises(SystemExit):
            scanner.run_scanner()


def test_port_range_start_too_low():
    """
    Test that start_port < 1 is rejected.
    """
    mock_args = MagicMock(
        target="127.0.0.1",
        start_port=0,
        end_port=100,
        threads=1,
    )

    with patch.object(scanner, "args", mock_args), patch.object(
        scanner, "target", "127.0.0.1"
    ), patch("sys.exit", side_effect=SystemExit):
        with pytest.raises(SystemExit):
            scanner.run_scanner()


def test_port_range_end_too_high():
    """
    Test that end_port > 65535 is rejected.
    """
    mock_args = MagicMock(
        target="127.0.0.1",
        start_port=1,
        end_port=70000,
        threads=1,
    )

    with patch.object(scanner, "args", mock_args), patch.object(
        scanner, "target", "127.0.0.1"
    ), patch("sys.exit", side_effect=SystemExit):
        with pytest.raises(SystemExit):
            scanner.run_scanner()


def test_invalid_hostname():
    mock_args = MagicMock(
        target="invalid_host", start_port=1, end_port=2, threads=1
    )

    with patch.object(scanner, "args", mock_args):
        with patch("socket.gethostbyname", side_effect=socket.gaierror), patch(
            "sys.exit"
        ) as mock_exit:
            try:
                scanner.run_scanner()
            except Exception:
                pass

            mock_exit.assert_called()


def test_banner_timeout():
    """
    Ensure open ports are recorded even if banner fetching times out.
    """
    target_port = 80

    with patch("socket.socket") as MockSocket:
        mock_instance = MagicMock()
        # Setup context manager support
        mock_instance.__enter__ = MagicMock(return_value=mock_instance)
        mock_instance.__exit__ = MagicMock(return_value=None)

        MockSocket.return_value = mock_instance

        # Connection succeeds, but recv raises timeout
        mock_instance.connect_ex.return_value = 0
        mock_instance.recv.side_effect = socket.timeout

        with patch.object(scanner, "target", "127.0.0.1"):
            scanner.scan_port(target_port)

    # Port should still be considered open, with empty or error banner
    found = next(
        (p for p in scanner.open_ports if p["port"] == target_port), None
    )
    assert found is not None
