# 🧠 Git & GitHub Cheat Sheet
_Link to Course: [Git & GitHub by Google on Coursera](https://www.coursera.org/learn/introduction-git-github/home/module/1)_

---

---

## 🔄 Version Control System (VCS)
- Keeps **historical copy** of your code.
- Tracks every small code change.
- Shows the **difference between files**.

## 🛠️ CLI Commands
| Task | Command |
|------|---------|
| Compare two files | `diff` file1.py file2.py |
| Unified diff (shows changes) | `diff` -u file1 file2 |
| View file contents | `cat` filename |

## 🚫 Main Branch Safety
> ❗ Never commit directly to the **main** branch

---

## 📦 Basic Git Workflow

### 1️⃣ Initialize Repo
```bash
git init
```

### 2️⃣ Add Remote Repo
```bash
git remote add origin <LINK>
```

### 3️⃣ Check Remote Connection
```bash
git remote -v
```

### 4️⃣ Remove Remote Connection
```bash
git remote rm origin
```

### 5️⃣ Add Files to Staging
```bash
git add .                # Add all files
git add filename.ext     # Add specific file
```

### 6️⃣ Create New Branch
```bash
git branch branch_name
```

### 6.1️⃣ Rename Current Branch to Main
```bash
git branch -M main
```

### 6.2️⃣ Push to Main Branch
```bash
git push -u origin main
```

### 7️⃣ Switch Branch
```bash
git checkout branch_name
```

### 8️⃣ View Git Logs
```bash
git log
```

### 9️⃣ Push Code
```bash
git push origin branch_name
git push origin main -f      # Force push
```

### 🔟 Pull Code
```bash
git pull <REPO_LINK>
git pull origin <repo_link>
```

---

## 🧹 Cleanups & Reset

### 🗑️ Remove Commit (Soft Reset)
```bash
git reset <commit_address>
```

### ❌ Delete Files
```bash
git rm filename
git rm -rf filename
```

---

## 📝 Git Stash (Temporary Storage)
```bash
git stash          # Hide uncommitted changes
git stash pop      # Restore them
git stash clear    # Delete all stashed changes
```

## 🌳 Branch Visualization Tool
[Learn Git Branching (Interactive)](https://learngitbranching.js.org/?NODEMO)

## 🔀 Merging & Forking

### 🔃 Merge with Main
```bash
git merge main
```

### 🍴 Forking Concept
> A "fork" is your own copy of someone else's repo. The original repo is called the **upstream**.

### 🧬 Clone a Repo
```bash
git clone <LINK>
```

---