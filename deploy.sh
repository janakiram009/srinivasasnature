#!/bin/bash

set -Eeuo pipefail

if git diff --quiet && git diff --cached --quiet; then
    echo "Nothing to commit."
    exit 0
fi

echo "Checking git status..."
git status

read -p "Commit message: " MESSAGE

git add .
git commit -m "$MESSAGE"
git push origin main

echo
echo "Code pushed successfully."
echo "GitHub Actions will now deploy it to the VPS."