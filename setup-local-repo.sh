#!/bin/bash

# Setup Local Code Repository for Bob Projects
# This creates a centralized location for all Bob-generated projects

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🏗️  Setting Up Local Bob Projects Repository${NC}"
echo "================================================"

# Define paths
REPO_DIR="$HOME/Documents/ibm_bob_projects_repo"
CURRENT_PROJECT="bva-generator-agent"
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}📂 Repository location:${NC} $REPO_DIR"

# Create the repository directory
if [ -d "$REPO_DIR" ]; then
    echo -e "${YELLOW}⚠️  Repository directory already exists${NC}"
else
    echo -e "${BLUE}📁 Creating repository directory...${NC}"
    mkdir -p "$REPO_DIR"
    echo -e "${GREEN}✅ Created: $REPO_DIR${NC}"
fi

# Move or copy current project
echo -e "\n${BLUE}📦 Setting up current project...${NC}"

PROJECT_PATH="$REPO_DIR/$CURRENT_PROJECT"

if [ -d "$PROJECT_PATH" ]; then
    echo -e "${YELLOW}⚠️  Project already exists in repository${NC}"
    echo -e "${YELLOW}Choose an option:${NC}"
    echo "  1. Skip (keep existing)"
    echo "  2. Update (copy current files over)"
    echo "  3. Backup and replace"
    read -p "Enter choice (1-3): " choice
    
    case $choice in
        2)
            echo -e "${BLUE}📋 Copying current project files...${NC}"
            rsync -av --exclude='.git' --exclude='venv' --exclude='__pycache__' --exclude='node_modules' "$CURRENT_DIR/" "$PROJECT_PATH/"
            echo -e "${GREEN}✅ Updated project files${NC}"
            ;;
        3)
            BACKUP_DIR="$REPO_DIR/${CURRENT_PROJECT}_backup_$(date +%Y%m%d_%H%M%S)"
            echo -e "${BLUE}💾 Backing up to: $BACKUP_DIR${NC}"
            mv "$PROJECT_PATH" "$BACKUP_DIR"
            cp -r "$CURRENT_DIR" "$PROJECT_PATH"
            echo -e "${GREEN}✅ Backed up and replaced${NC}"
            ;;
        *)
            echo -e "${YELLOW}⏭️  Skipping project setup${NC}"
            ;;
    esac
else
    echo -e "${BLUE}📋 Copying project to repository...${NC}"
    cp -r "$CURRENT_DIR" "$PROJECT_PATH"
    echo -e "${GREEN}✅ Copied: $CURRENT_PROJECT${NC}"
fi

# Create README for the repository
echo -e "\n${BLUE}📝 Creating repository README...${NC}"
cat > "$REPO_DIR/README.md" << 'EOF'
# IBM Bob Projects Repository

This directory contains all projects created with Bob AI assistant.

## 📁 Structure

```
ibm_bob_projects_repo/
├── bva-generator-agent/     # Business Value Assessment Generator
├── [future-project-1]/      # Your next Bob project
├── [future-project-2]/      # Another Bob project
└── README.md                # This file
```

## 🚀 Quick Start

Each project has its own setup instructions. Navigate to a project directory and check its README.md or SETUP.md file.

## 📋 Projects

### BVA Generator Agent
- **Location:** `bva-generator-agent/`
- **Description:** Multi-agent system for generating Business Value Assessments
- **GitHub:** https://github.com/monaghs/ibm_hackathon
- **Quick Start:** `cd bva-generator-agent && python main.py`

## 🔧 Adding New Projects

When Bob creates a new project, run:
```bash
cp -r /path/to/new/project ~/Documents/ibm_bob_projects_repo/
```

Or use the setup script:
```bash
./setup-local-repo.sh
```

## 💡 Tips

- Keep all Bob projects here for easy organization
- Each project maintains its own git repository
- Backup this directory regularly
- Use GitHub for cloud backup of individual projects

## 📞 Support

For issues with specific projects, check their individual documentation.

---
Created with ❤️ by Bob AI Assistant
EOF

echo -e "${GREEN}✅ Created repository README${NC}"

# Create a quick access script
echo -e "\n${BLUE}🔗 Creating quick access script...${NC}"
cat > "$REPO_DIR/open-project.sh" << 'EOF'
#!/bin/bash

# Quick access to Bob projects

REPO_DIR="$HOME/Documents/ibm_bob_projects_repo"

echo "📂 Available Projects:"
echo "===================="
ls -1 "$REPO_DIR" | grep -v "README.md" | grep -v "open-project.sh" | nl

echo ""
read -p "Enter project number to open (or 'q' to quit): " choice

if [ "$choice" = "q" ]; then
    exit 0
fi

project=$(ls -1 "$REPO_DIR" | grep -v "README.md" | grep -v "open-project.sh" | sed -n "${choice}p")

if [ -n "$project" ]; then
    cd "$REPO_DIR/$project"
    echo "📂 Opening: $project"
    echo "📍 Location: $(pwd)"
    
    # Open in VS Code if available
    if command -v code &> /dev/null; then
        code .
    fi
    
    # Start a new shell in the project directory
    exec $SHELL
else
    echo "❌ Invalid selection"
fi
EOF

chmod +x "$REPO_DIR/open-project.sh"
echo -e "${GREEN}✅ Created quick access script${NC}"

# Create alias suggestion
echo -e "\n${BLUE}💡 Suggested Shell Alias${NC}"
echo "Add this to your ~/.zshrc or ~/.bashrc:"
echo ""
echo -e "${YELLOW}alias bob-projects='cd ~/Documents/ibm_bob_projects_repo'${NC}"
echo -e "${YELLOW}alias bob-open='~/Documents/ibm_bob_projects_repo/open-project.sh'${NC}"
echo ""

# Summary
echo -e "\n${GREEN}✅ Setup Complete!${NC}"
echo "================================================"
echo -e "${BLUE}📂 Repository Location:${NC} $REPO_DIR"
echo -e "${BLUE}📁 Current Project:${NC} $PROJECT_PATH"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "  1. Navigate to repository: cd ~/Documents/ibm_bob_projects_repo"
echo "  2. View projects: ls -la"
echo "  3. Quick access: ~/Documents/ibm_bob_projects_repo/open-project.sh"
echo "  4. Add shell aliases (see above)"
echo ""
echo -e "${GREEN}🎉 Your local Bob projects repository is ready!${NC}"

# Made with Bob
