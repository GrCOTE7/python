#!/bin/bash
set -e

echo "🚀 postCreateCommand: démarrage"

# 1) Vérifier uv (déjà installé dans le Dockerfile)
if ! command -v uv >/dev/null 2>&1; then
    echo "❌ uv n'est pas disponible — problème dans le Dockerfile"
    exit 1
fi

# 2) Installer les dépendances Python (sans réinstaller Python)
echo "📦 Installation des dépendances Python via uv..."
uv sync --no-install-python

# 3) Forcer ripgrep pour Todo Tree (déjà installé dans Dockerfile)
if command -v rg >/dev/null 2>&1; then
    ln -sf /usr/bin/rg /usr/bin/vscode-ripgrep
    echo "🔍 ripgrep configuré pour Todo Tree"
else
    echo "⚠️ ripgrep introuvable — vérifier Dockerfile"
fi

# 4) Copier les keybindings VS Code
WORKSPACE_DIR="${GITHUB_WORKSPACE:-$PWD}"
KEYBINDINGS_SOURCE="$WORKSPACE_DIR/doc/files/keybindings.json"

if [ -f "$KEYBINDINGS_SOURCE" ]; then
    for TARGET in \
        "$HOME/.vscode-remote/data/User/keybindings.json" \
        "$HOME/.vscode-server/data/User/keybindings.json" \
        "$HOME/.vscode-remote/data/Machine/keybindings.json" \
        "$HOME/.vscode-server/data/Machine/keybindings.json"
    do
        mkdir -p "$(dirname "$TARGET")"
        cp "$KEYBINDINGS_SOURCE" "$TARGET"
        echo "🎹 keybindings copiés vers $TARGET"
    done
else
    echo "⚠️ keybindings source introuvable: $KEYBINDINGS_SOURCE"
fi

echo "✅ postCreateCommand terminé"
