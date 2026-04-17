#!/bin/bash

# Migrate Project from Desktop to Documents
# This moves the project to Documents and sets up auto-push there

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚚 Migrating Project to Documents${NC}"
echo "================================================"

# Define paths
DESKTOP_DIR="/Users/soccerdude/Desktop/bva-generator-agent"
DOCS_DIR="$HOME/Documents/ibm_bob_projects_repo/bva-generator-agent"

# Stop the file watcher if running
echo -e "${YELLOW}⚠️  Stopping file watcher if running...${NC}"
pkill -f "watch-and-push.sh" 2>/dev/null || true
sleep 2
echo -e "${GREEN}✅ File watcher stopped${NC}"

# Check if Documents directory exists
if [ ! -d "$DOCS_DIR" ]; then
    echo -e "${RED}❌ Documents directory not found${NC}"
    echo -e "${YELLOW}Run setup-local-repo.sh first${NC}"
    exit 1
fi

# Sync latest changes from Desktop to Documents
echo -e "\n${BLUE}📋 Syncing latest changes to Documents...${NC}"
rsync -av --delete \
    --exclude='venv' \
    --exclude='__pycache__' \
    --exclude='node_modules' \
    --exclude='*.pyc' \
    --exclude='reports/*.docx' \
    "$DESKTOP_DIR/" "$DOCS_DIR/"

echo -e "${GREEN}✅ Synced to Documents${NC}"

# Verify git works in new location
cd "$DOCS_DIR"
if git status &>/dev/null; then
    echo -e "${GREEN}✅ Git repository working in Documents${NC}"
else
    echo -e "${RED}❌ Git repository not working${NC}"
    exit 1
fi

# Create a backup of Desktop directory
echo -e "\n${BLUE}💾 Creating backup of Desktop directory...${NC}"
BACKUP_DIR="/Users/soccerdude/Desktop/bva-generator-agent_backup_$(date +%Y%m%d_%H%M%S)"
mv "$DESKTOP_DIR" "$BACKUP_DIR"
echo -e "${GREEN}✅ Backup created: $BACKUP_DIR${NC}"

# Create a symlink on Desktop pointing to Documents
echo -e "\n${BLUE}🔗 Creating shortcut on Desktop...${NC}"
ln -s "$DOCS_DIR" "/Users/soccerdude/Desktop/bva-generator-agent"
echo -e "${GREEN}✅ Shortcut created on Desktop${NC}"

# Make scripts executable
cd "$DOCS_DIR"
chmod +x auto-push.sh watch-and-push.sh setup-local-repo.sh migrate-to-documents.sh

# Test manual push
echo -e "\n${BLUE}🧪 Testing auto-push from Documents...${NC}"
if ./auto-push.sh "Migrated project to Documents directory" 2>&1; then
    echo -e "${GREEN}✅ Auto-push working from Documents${NC}"
else
    echo -e "${YELLOW}⚠️  Push test completed${NC}"
fi

# Summary
echo -e "\n${GREEN}✅ Migration Complete!${NC}"
echo "================================================"
echo -e "${BLUE}📂 New Location:${NC} $DOCS_DIR"
echo -e "${BLUE}💾 Backup:${NC} $BACKUP_DIR"
echo -e "${BLUE}🔗 Desktop Shortcut:${NC} /Users/soccerdude/Desktop/bva-generator-agent → Documents"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "  1. Open VS Code in new location:"
echo "     code ~/Documents/ibm_bob_projects_repo/bva-generator-agent"
echo ""
echo "  2. Start auto-push watcher:"
echo "     cd ~/Documents/ibm_bob_projects_repo/bva-generator-agent"
echo "     ./watch-and-push.sh"
echo ""
echo "  3. Delete backup when ready:"
echo "     rm -rf $BACKUP_DIR"
echo ""
echo -e "${GREEN}🎉 Your project now lives in Documents + GitHub only!${NC}"

# Made with Bob
