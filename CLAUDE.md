# CLAUDE.md

Small Python (Flask) app, packaged as a distroless Chainguard image with gunicorn. Created from [tuxpeople/template-python-app](https://github.com/tuxpeople/template-python-app).

## Commands

```bash
pip install -r requirements.txt -r requirements-dev.txt
ruff check . && ruff format --check . && pytest
docker build -t app:test .
```

## Rules

- **Security first:** never enable Flask debug (the Werkzeug debugger allows code execution). File access from request input must stay inside its folder (`safe_join` / `send_from_directory`). Add regression tests for security fixes.
- **Ruff S rules** (flake8-bandit) are enabled on purpose; fix findings instead of ignoring them.
- **Image:** the venv lives in `/opt/venv` (readable by any UID); the root filesystem is read-only in Kubernetes, gunicorn uses `/dev/shm`.
- **Commits:** Conventional Commits; they drive release-please (`feat` → minor, `fix` → patch, `!` → major, `deps` → patch). Use `chore`/`ci`/`docs` for changes that should not produce a release.
- **release-as** in `release-please-config.json` is only for the first release; remove it afterwards.
- **Actions** are pinned by commit SHA (`@<sha> # vX.Y.Z`); Renovate keeps them up to date.
