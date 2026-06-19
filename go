#!/bin/bash
cd "$(dirname "$0")"

uv sync

# Optionnel : forcer le mode copy uniquement pour cette session bash
export UV_LINK_MODE=copy

uv run src/main.py
# --web --host 0.0.0.0 --port 8550
