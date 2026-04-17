# 🚀 Automatic GitHub Push Setup

## Overview

Your project now has **two push options**:

1. **Manual Push** - Run `./auto-push.sh` when you want to push
2. **Automatic Push** - File watcher that pushes on every save ⭐ NEW

## 🔄 Automatic Push (File Watcher)

### Quick Start

**Option 1: Run in Terminal (Simple)**
```bash
cd /Users/soccerdude/Desktop/bva-generator-agent
./watch-and-push.sh
```

This will:
- ✅ Watch for file changes in real-time
- ✅ Automatically commit and push after 5 seconds of inactivity
- ✅ Show you what's being pushed
- ⚠️ Runs until you press Ctrl+C

**Option 2: Run in Background (Advanced)**
```bash
cd /Users/soccerdude/Desktop/bva-generator-agent
nohup ./watch-and-push.sh > watch-and-push.log 2>&1 &
```

To stop background process:
```bash
# Find the process
ps aux | grep watch-and-push

# Kill it (replace PID with actual process ID)
kill <PID>
```

### Installation (First Time Only)

The script will automatically install `fswatch` if needed:
```bash
brew install fswatch
```

Or install manually:
```bash
# If you don't have Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install fswatch
brew install fswatch
```

## 📝 How It Works

1. **File Watcher** monitors your project directory
2. **Detects Changes** when you save any file
3. **Waits 5 seconds** (debounce) to batch multiple saves
4. **Auto-commits** with timestamp: "Auto-save: 2024-04-17 13:05:30"
5. **Pushes to GitHub** automatically

### What Gets Pushed

✅ All code files (.py, .js, .md, etc.)  
✅ Configuration files (.yaml, .json)  
✅ Documentation updates  
❌ Excluded: `.git/`, `reports/`, `__pycache__/`, `venv/`, `node_modules/`

## 🎯 Usage Scenarios

### Scenario 1: Working Session
```bash
# Start the watcher at beginning of work
cd /Users/soccerdude/Desktop/bva-generator-agent
./watch-and-push.sh

# Work normally - saves auto-push!
# Edit files in VS Code
# Save files (Cmd+S)
# Changes automatically pushed to GitHub

# Stop when done (Ctrl+C)
```

### Scenario 2: Always Running
```bash
# Start in background
cd /Users/soccerdude/Desktop/bva-generator-agent
nohup ./watch-and-push.sh > watch-and-push.log 2>&1 &

# Check if running
ps aux | grep watch-and-push

# View logs
tail -f watch-and-push.log

# Stop when needed
pkill -f watch-and-push
```

### Scenario 3: Manual Control
```bash
# Use the original script for manual pushes
cd /Users/soccerdude/Desktop/bva-generator-agent
./auto-push.sh "My custom commit message"
```

## ⚙️ Configuration

### Change Debounce Time

Edit `watch-and-push.sh` line 28:
```bash
DEBOUNCE_TIME=5  # Change to 10 for 10 seconds, etc.
```

### Exclude More Directories

Edit `watch-and-push.sh` lines 58-64:
```bash
fswatch -r \
    --exclude='\.git/' \
    --exclude='reports/' \
    --exclude='your_folder/' \  # Add this line
    ...
```

## 🚨 Important Notes

### ⚠️ Caution
- Every save triggers a push (after debounce)
- This creates many commits - good for backup, but clutters history
- Consider using manual push for "clean" commit history

### 💡 Best Practices
1. **Use auto-push for**: Active development, frequent backups
2. **Use manual push for**: Clean commits, before sharing code
3. **Stop watcher when**: Making experimental changes, large refactors

### 🔒 Security
- Never commit sensitive data (API keys, passwords)
- Check `.gitignore` is properly configured
- Review what's being pushed in the terminal output

## 📊 Comparison

| Feature | Manual Push | Auto Push |
|---------|-------------|-----------|
| Control | Full control | Automatic |
| Commit Messages | Custom | Timestamped |
| History | Clean | Frequent |
| Best For | Final changes | Active dev |
| Setup | Ready now | Needs fswatch |

## 🛠️ Troubleshooting

### "fswatch: command not found"
```bash
brew install fswatch
```

### "Permission denied"
```bash
chmod +x watch-and-push.sh
```

### Too many commits
```bash
# Stop the watcher (Ctrl+C)
# Use manual push instead
./auto-push.sh "Consolidated changes"
```

### Want to squash commits later
```bash
# Squash last 10 commits into one
git reset --soft HEAD~10
git commit -m "Consolidated: Multiple auto-saves"
git push -f origin main
```

## 🎓 Commands Reference

```bash
# Start auto-push watcher
./watch-and-push.sh

# Start in background
nohup ./watch-and-push.sh > watch-and-push.log 2>&1 &

# Check if running
ps aux | grep watch-and-push

# View live logs
tail -f watch-and-push.log

# Stop background process
pkill -f watch-and-push

# Manual push (original)
./auto-push.sh "Your message"

# Check what will be pushed
git status

# View recent commits
git log --oneline -10
```

## 🔗 Links

- GitHub Repository: https://github.com/monaghs/ibm_hackathon
- fswatch Documentation: https://github.com/emcrisostomo/fswatch

---

**Choose your workflow:**
- 🤖 **Automatic**: Run `./watch-and-push.sh` for hands-free pushing
- 👆 **Manual**: Run `./auto-push.sh` when you're ready to push