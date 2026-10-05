#!/usr/bin/env bash
# Crea un worktree aislado para un agente y una tarea.
# Uso: scripts/agent-worktree.sh <agente> <tarea> [rama-base]
# Rama: agent/<agente>/<tarea>. Ruta: $AGENT_WORKTREE_ROOT/<agente>-<tarea>
# (por defecto ~/worktrees/<proyecto>/, fuera del repositorio).
set -euo pipefail

usage() {
    echo "Uso: $0 <agente> <tarea> [rama-base]" >&2
    exit 1
}

slugify() {
    printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'
}

[[ $# -ge 2 && $# -le 3 ]] || usage

agent="$(slugify "$1")"
task="$(slugify "$2")"
base="${3:-main}"

if [[ -z "$agent" || -z "$task" ]]; then
    echo "El nombre del agente y de la tarea no puede quedar vacío tras normalizarlo." >&2
    exit 1
fi

repo_root="$(git rev-parse --show-toplevel)"
repo_name="$(basename "$repo_root")"
worktree_root="${AGENT_WORKTREE_ROOT:-$HOME/worktrees/$repo_name}"
branch="agent/$agent/$task"
path="$worktree_root/$agent-$task"

if ! git -C "$repo_root" rev-parse --verify --quiet "$base" >/dev/null; then
    echo "La rama base no existe: $base" >&2
    exit 1
fi

if git -C "$repo_root" show-ref --verify --quiet "refs/heads/$branch"; then
    echo "La rama ya existe: $branch" >&2
    exit 1
fi

if [[ -e "$path" ]]; then
    echo "La ruta ya existe: $path" >&2
    exit 1
fi

mkdir -p "$worktree_root"
git -C "$repo_root" worktree add -b "$branch" "$path" "$base"

echo "Worktree creado: $path"
echo "Rama: $branch (desde $base)"
if command -v code >/dev/null 2>&1; then
    echo "Abrir en una ventana nueva de VS Code: code -n \"$path\""
else
    echo "VS Code (comando 'code') no encontrado en el PATH. Ábrelo desde el menú o instala el comando 'code'."
fi
