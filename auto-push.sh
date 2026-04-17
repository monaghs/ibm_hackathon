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

# Check if git repository exists
if [ ! -d .git ]; then
    echo -e "${RED}❌ Error: Not a git repository${NC}"
    echo -e "${YELLOW}Run: git init${NC}"
    exit 1
fi

# Check if remote exists
if ! git remote get-url origin &> /dev/null; then
    echo -e "${RED}❌ Error: No remote 'origin' configured${NC}"
    echo -e "${YELLOW}To add a remote, run:${NC}"
    echo -e "  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    exit 1
fi

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

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)

# Push to GitHub
echo -e "${BLUE}🚀 Pushing to GitHub (branch: $CURRENT_BRANCH)...${NC}"
if git push origin "$CURRENT_BRANCH" 2>&1; then
    echo -e "\n${GREEN}✅ Successfully pushed to GitHub!${NC}"
    REMOTE_URL=$(git remote get-url origin)
    echo -e "${GREEN}🔗 Remote: $REMOTE_URL${NC}"
else
    echo -e "\n${RED}❌ Push failed!${NC}"
    echo -e "${YELLOW}Common issues:${NC}"
    echo -e "  1. Repository doesn't exist on GitHub"
    echo -e "  2. No permission to push"
    echo -e "  3. Need to authenticate (use Personal Access Token)"
    echo -e "\n${YELLOW}To fix:${NC}"
    echo -e "  • Create repo at: https://github.com/new"
    echo -e "  • Update remote: git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    echo -e "  • Or use GitHub CLI: gh repo create"
    exit 1
fi

# Made with Bob
