# ⚡ Quick Commands for Auto-Push

## 🚀 One-Time Setup (Copy & Paste)

```bash
cd /Users/soccerdude/Desktop/bva-generator-agent && chmod +x auto-push.sh
```

## 📤 Push Bob's Changes to GitHub

### Basic Push (with auto-generated message)
```bash
cd /Users/soccerdude/Desktop/bva-generator-agent && ./auto-push.sh
```

### Push with Custom Message
```bash
cd /Users/soccerdude/Desktop/bva-generator-agent && ./auto-push.sh "Bob: Your custom message here"
```

## 🎯 Create Easy Alias (Optional but Recommended)

### For Bash users:
```bash
echo 'alias bob-push="cd /Users/soccerdude/Desktop/bva-generator-agent && ./auto-push.sh"' >> ~/.bashrc && source ~/.bashrc
```

### For Zsh users (macOS default):
```bash
echo 'alias bob-push="cd /Users/soccerdude/Desktop/bva-generator-agent && ./auto-push.sh"' >> ~/.zshrc && source ~/.zshrc
```

After setting up the alias, just type:
```bash
bob-push
# or
bob-push "Custom message"
```

## 🔄 Auto-Push on Every Commit (Git Hook)

```bash
cd /Users/soccerdude/Desktop/bva-generator-agent && cat > .git/hooks/post-commit << 'EOF'
#!/bin/bash
echo "🚀 Auto-pushing to GitHub..."
git push origin main
EOF
chmod +x .git/hooks/post-commit
```

Now every `git commit` will automatically push!

## ✅ Test It Now

```bash
cd /Users/soccerdude/Desktop/bva-generator-agent && ./auto-push.sh "Test: Setting up auto-push"
```

---

**That's it!** Your code will now automatically push to:
https://github.com/monaghs/ibm_hackathon