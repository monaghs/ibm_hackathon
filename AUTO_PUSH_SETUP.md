# 🤖 Auto-Push Setup for Bob-Generated Code

This guide shows you how to automatically push Bob-generated code changes to GitHub.

## 🚀 Quick Setup (Command Line)

### Step 1: Make the Script Executable

```bash
cd /Users/soccerdude/Desktop/bva-generator-agent
chmod +x auto-push.sh
```

### Step 2: Test the Auto-Push Script

```bash
# Push with default commit message
./auto-push.sh

# Or push with custom commit message
./auto-push.sh "Added new feature: dashboard improvements"
```

## 📋 Usage Options

### Option 1: Manual Auto-Push (Recommended)

After Bob makes changes, run:
```bash
cd /Users/soccerdude/Desktop/bva-generator-agent
./auto-push.sh
```

Or with a custom message:
```bash
./auto-push.sh "Bob: Updated calculator logic"
```

### Option 2: Create an Alias (Easier)

Add this to your `~/.bashrc` or `~/.zshrc`:
```bash
alias bob-push='cd /Users/soccerdude/Desktop/bva-generator-agent && ./auto-push.sh'
```

Then reload your shell:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

Now you can just type:
```bash
bob-push
bob-push "Custom commit message"
```

### Option 3: Watch for Changes (Advanced)

Install `fswatch` (macOS):
```bash
brew install fswatch
```

Create a watcher script:
```bash
cd /Users/soccerdude/Desktop/bva-generator-agent
fswatch -o . | xargs -n1 -I{} ./auto-push.sh "Auto-commit: File changes detected"
```

This will automatically push whenever files change (use with caution!).

### Option 4: Git Hooks (Automatic on Commit)

Create a post-commit hook:
```bash
cd /Users/soccerdude/Desktop/bva-generator-agent
cat > .git/hooks/post-commit << 'EOF'
#!/bin/bash
echo "🚀 Auto-pushing to GitHub..."
git push origin main
EOF

chmod +x .git/hooks/post-commit
```

Now every time you commit, it will automatically push!

## 🎯 Recommended Workflow

**For Bob-Generated Code:**

1. Bob makes changes to your code
2. Review the changes
3. Run the auto-push script:
   ```bash
   ./auto-push.sh "Bob: [description of changes]"
   ```

**Example:**
```bash
# After Bob creates new features
./auto-push.sh "Bob: Added interactive dashboard with real-time updates"

# After Bob fixes bugs
./auto-push.sh "Bob: Fixed calculation error in BVA formula"

# After Bob updates documentation
./auto-push.sh "Bob: Updated README with new examples"
```

## 🔐 Authentication Setup

If you haven't set up authentication yet:

### Option A: Personal Access Token (Recommended)

1. Generate token at: https://github.com/settings/tokens
2. Select scope: `repo` (full control)
3. Copy the token
4. Store it securely:
   ```bash
   git config --global credential.helper osxkeychain
   ```
5. Next time you push, use the token as your password

### Option B: SSH Key

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: https://github.com/settings/keys

# Update remote to use SSH
git remote set-url origin git@github.com:monaghs/ibm_hackathon.git
```

## 📊 What the Auto-Push Script Does

1. ✅ Checks for changes in your repository
2. 📝 Shows you what will be committed
3. ➕ Adds all changes (`git add .`)
4. 💾 Commits with timestamp or custom message
5. 🚀 Pushes to GitHub (`git push origin main`)
6. ✨ Provides success confirmation with link

## 🛠️ Troubleshooting

### "Permission denied" error
```bash
chmod +x auto-push.sh
```

### "Authentication failed" error
- Use Personal Access Token instead of password
- Or set up SSH keys (see above)

### "No changes to commit"
- This is normal - the script detected no changes
- Make some changes first, then run the script

### "Failed to push" error
```bash
# Pull latest changes first
git pull origin main --rebase

# Then try pushing again
./auto-push.sh
```

### Script not found
```bash
# Make sure you're in the right directory
cd /Users/soccerdude/Desktop/bva-generator-agent

# Check if script exists
ls -la auto-push.sh
```

## 🎨 Customization

### Change Default Branch
Edit `auto-push.sh` and change `main` to your branch name:
```bash
git push origin your-branch-name
```

### Add Pre-Push Checks
Edit `auto-push.sh` to add tests before pushing:
```bash
# Run tests before pushing
python -m pytest tests/
if [ $? -ne 0 ]; then
    echo "Tests failed! Not pushing."
    exit 1
fi
```

### Exclude Certain Files
Update `.gitignore` to exclude files from auto-push:
```bash
echo "*.log" >> .gitignore
echo "temp/" >> .gitignore
```

## 📚 Quick Reference

```bash
# Basic usage
./auto-push.sh

# With custom message
./auto-push.sh "Your message here"

# Check what would be pushed (dry run)
git status

# View recent commits
git log --oneline -5

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Force push (use carefully!)
git push -f origin main
```

## ✅ Verification

After pushing, verify at:
```
https://github.com/monaghs/ibm_hackathon
```

---

**Pro Tip:** Create a keyboard shortcut in your terminal to run `./auto-push.sh` for even faster pushing!