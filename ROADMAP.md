# Roadmap

This document tracks planned improvements to the Multithreaded Port Scanner, organised into four phases. Each phase builds on the previous one, incrementally increasing the project's capabilities and professional quality.

For a live view of progress, see the [GitHub Project board](https://github.com/danzolotov/multithreaded-port-scanner/projects).

---

## Phase 1 — DevOps & Code Quality

Establish a professional development workflow that signals engineering rigour to potential collaborators and recruiters.

| Feature | Issue | Status |
|---|---|---|
| CI/CD pipeline with GitHub Actions (Python 3.10–3.12, pytest, flake8) | [#1](../../issues/1) | ✅ Done |
| Docker support for containerised deployment | [#2](../../issues/2) | ✅ Done |
| Code quality tooling (flake8, mypy, pre-commit hooks) | [#3](../../issues/3) | 🔄 In Progress |

---

## Phase 2 — Feature Enhancements

Expand the scanner's capabilities to cover a wider range of real-world use cases.

| Feature | Issue | Status |
|---|---|---|
| UDP port scanning support | [#4](../../issues/4) | 📋 Planned |
| IPv6 address support | [#5](../../issues/5) | 📋 Planned |
| Additional output formats — CSV and HTML report | [#6](../../issues/6) | 📋 Planned |
| Structured logging with verbosity levels (`-v` / `-q`) | [#7](../../issues/7) | 📋 Planned |

---

## Phase 3 — Performance & Scalability

Make the scanner faster and more controllable under different network conditions.

| Feature | Issue | Status |
|---|---|---|
| Asyncio-based scanning core for higher concurrency | [#8](../../issues/8) | 📋 Planned |
| Rate limiting to avoid overwhelming targets or triggering IDS | [#9](../../issues/9) | 📋 Planned |
| Predefined scan profiles (`common`, `web`, `full`) | [#10](../../issues/10) | 📋 Planned |

---

## Phase 4 — Advanced Features

Add capabilities that go beyond a basic port scanner and demonstrate depth of knowledge.

| Feature | Issue | Status |
|---|---|---|
| Protocol-aware service version detection | [#11](../../issues/11) | 📋 Planned |
| Basic OS fingerprinting via TTL analysis | [#12](../../issues/12) | 📋 Planned |
| Real-time progress bar during scanning | [#13](../../issues/13) | 📋 Planned |

---

## Status Key

| Symbol | Meaning |
|---|---|
| ✅ Done | Implemented and merged |
| 🔄 In Progress | Actively being worked on |
| 📋 Planned | Scoped but not yet started |
| ❌ Cancelled | Descoped |
