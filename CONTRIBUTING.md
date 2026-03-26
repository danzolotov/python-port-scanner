# Contributing

Thank you for considering a contribution to this project! The following guidelines will help you get your changes merged quickly.

## Development Setup

1. **Fork** the repository and clone your fork.

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Install development dependencies:**

   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Run the test suite** to confirm everything passes before making any changes:

   ```bash
   pytest test_scanner.py -v
   ```

5. **Run the linter:**

   ```bash
   flake8 scanner.py test_scanner.py
   ```

## Making Changes

- Create a new branch from `main` for each logical change:

  ```bash
  git checkout -b feature/my-new-feature
  ```

- Write or update tests for every change you make in `test_scanner.py`.
- Keep commits small and focused. Use descriptive commit messages.

## Pull Request Checklist

Before opening a PR, make sure:

- [ ] All existing tests pass (`pytest test_scanner.py -v`)
- [ ] New tests have been added for any new behaviour
- [ ] `flake8` reports no issues
- [ ] The PR description explains *what* changed and *why*
- [ ] The `ROADMAP.md` is updated if a roadmap item has been completed

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Use type hints for all function signatures.
- Add or update docstrings for every public function.
- Maximum line length: **120 characters** (configured in `.flake8`).

## Reporting Bugs

Use the **Bug Report** issue template. Please include the Python version, OS, and the exact command you ran.

## Suggesting Features

Use the **Feature Request** issue template or check the [ROADMAP](ROADMAP.md) to see if your idea is already planned.

## Disclaimer

Only scan networks and systems you own or have explicit permission to test.
