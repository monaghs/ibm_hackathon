#!/bin/bash

# Auto-Push Script for Bob-Generated Code
# This script automatically commits and pushes changes to GitHub

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 Bob Auto-Push Script${NC}"
echo "================================"

# Navigate to project directory (handle both direct execution and sourcing)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${BLUE}📂 Working directory:${NC} $(pwd)"

# Check if there are any changes
if [[ -z $(git status -s) ]]; then
    echo -e "${YELLOW}⚠️  No changes to commit${NC}"
    exit 0
fi

# Show what will be committed
echo -e "\n${BLUE}📝 Changes to be committed:${NC}"
git status -s

# Get commit message (use argument or default)
if [ -z "$1" ]; then
    COMMIT_MSG="Auto-commit: Bob generated code updates - $(date '+%Y-%m-%d %H:%M:%S')"
else
    COMMIT_MSG="$1"
fi

echo -e "\n${BLUE}💬 Commit message:${NC} $COMMIT_MSG"

# Add all changes
echo -e "\n${BLUE}➕ Adding changes...${NC}"
git add .

# Commit changes
echo -e "${BLUE}💾 Committing changes...${NC}"
git commit -m "$COMMIT_MSG"

# Push to GitHub
echo -e "${BLUE}🚀 Pushing to GitHub...${NC}"
git push origin main

echo -e "\n${GREEN}✅ Successfully pushed to GitHub!${NC}"
echo -e "${GREEN}🔗 View at: https://github.com/monaghs/ibm_hackathon${NC}"

# Made with Bob
