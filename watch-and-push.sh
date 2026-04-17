#!/bin/bash

# Automatic Git Push on File Changes
# This script watches for file changes and automatically pushes to GitHub

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Navigate to project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${BLUE}🔍 Auto-Push File Watcher Started${NC}"
echo -e "${BLUE}📂 Watching:${NC} $(pwd)"
echo -e "${YELLOW}⚠️  Changes will be automatically pushed to GitHub${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop${NC}"
echo "================================"

# Check if fswatch is installed
if ! command -v fswatch &> /dev/null; then
    echo -e "${RED}❌ fswatch not found${NC}"
    echo -e "${YELLOW}Installing fswatch...${NC}"
    if command -v brew &> /dev/null; then
        brew install fswatch
    else
        echo -e "${RED}Please install Homebrew first: https://brew.sh${NC}"
        exit 1
    fi
fi

# Debounce timer (seconds to wait after last change before pushing)
DEBOUNCE_TIME=5
last_push=0

# Function to push changes
push_changes() {
    current_time=$(date +%s)
    time_since_last=$((current_time - last_push))
    
    # Only push if enough time has passed (debounce)
    if [ $time_since_last -lt $DEBOUNCE_TIME ]; then
        return
    fi
    
    # Check if there are changes
    if [[ -z $(git status -s) ]]; then
        return
    fi
    
    echo -e "\n${BLUE}📝 Changes detected, pushing...${NC}"
    
    # Run the auto-push script
    if ./auto-push.sh "Auto-save: $(date '+%Y-%m-%d %H:%M:%S')"; then
        last_push=$(date +%s)
        echo -e "${GREEN}✅ Pushed at $(date '+%H:%M:%S')${NC}"
    else
        echo -e "${RED}❌ Push failed${NC}"
    fi
}

# Watch for file changes (excluding .git directory and reports)
fswatch -r \
    --exclude='\.git/' \
    --exclude='reports/' \
    --exclude='__pycache__/' \
    --exclude='\.pyc$' \
    --exclude='venv/' \
    --exclude='node_modules/' \
    --event Created \
    --event Updated \
    --event Removed \
    --event Renamed \
    . | while read -r file; do
    echo -e "${BLUE}📄 File changed:${NC} $file"
    push_changes
done

# Made with Bob
