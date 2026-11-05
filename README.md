# template-python-app

Template for small Python apps that are published as a container image. It includes a minimal Flask app and the release pipeline used by [bildergallerie](https://github.com/tuxpeople/bildergallerie) and [feeder](https://github.com/tuxpeople/feeder):

- **Checks** on every PR: ruff (incl. the bandit `S` security rules), pytest, Hadolint, a container smoke test (read-only root, foreign UID, no capabilities) and a blocking Trivy scan
- **Releases** with [release-please](https://github.com/googleapis/release-please) from Conventional Commits
- **Image** `ghcr.io/<owner>/<repo>`: distroless Chainguard Python, gunicorn, amd64/arm64, Cosign-signed, signed SLSA provenance and SPDX SBOM
- **Renovate** via the shared presets in [tuxpeople/shared](https://github.com/tuxpeople/shared); base image and runtime dependency updates are released automatically
- **GHCR cleanup** once a month

## New repository from this template

```bash
gh repo create tuxpeople/<name> --public --template tuxpeople/template-python-app --clone
```

Then:

1. **Replace the app:** `app.py`, `templates/`, `tests/`, `requirements.txt`. Adjust the `COPY` lines and the gunicorn `ENTRYPOINT` in the `Dockerfile` if the module is not `app:app`.
2. **Names:** `name` in `pyproject.toml`, `package-name` in `release-please-config.json`, the OCI labels in the `Dockerfile`, this README and `CLAUDE.md`.
3. **Smoke test:** adapt the endpoints in `.github/workflows/tests.yml` (step "Smoke test").
4. **First version:** the first `feat` commit releases `0.1.0`. To continue an existing image's versions, set `"release-as": "X.Y.Z"` in `release-please-config.json` for the first release and **remove it afterwards** (it applies to every release until removed).
5. **Repository settings:** squash/rebase merges only, delete branches on merge.
6. **Release app:** install the release-please GitHub App on the repository, set the variable `RELEASE_APP_CLIENT_ID` and the secret `RELEASE_APP_PRIVATE_KEY`.
7. **Package access:** if the package `ghcr.io/<owner>/<name>` already exists, grant the new repository the **Admin** role under *Package settings → Manage Actions access*.

The release and cleanup workflows skip `tuxpeople/template-python-app` itself.

## Development

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
ruff check . && ruff format --check . && pytest
python app.py   # http://127.0.0.1:8080
docker build -t app:test .
```
