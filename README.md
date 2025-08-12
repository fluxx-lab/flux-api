# FLUX API
This is API server that supports `/check`, `/track` & `/attach` endpoint. SDK's would be build around this server

### Setup

#### Clone the repo
```bash
git clone https://github.com/fluxx-lab/flux-api.git
```

#### Install (UV)[https://docs.astral.sh/uv/] python package manager

#### Create venv
```bash
uv venv
```

#### Install the dependencies and packages
```bash
uv sync
```

### How to run application
- Locally using fastapi
```bash
uv run fastapi dev
```

- Locally using uvicorn
```bash
uv run uvicorn app.main:app --reload
```
