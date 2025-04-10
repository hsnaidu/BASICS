---

✅ ** Quick Git operations reference **
---

## 🚀 Setting Up a GitHub Repository and Pushing Code

### 📌 Steps

1. **Create a new repository** on GitHub.
2. **Copy the repository link** (HTTPS or SSH).

### Option A: Clone Directly from GitHub
```bash
git clone <repo-link>
```

### Option B: Create Folder Locally and Initialize Git
```bash
mkdir my-project
cd my-project
git init
```

3. **Add your files, then stage and commit**
```bash
git add .
git commit -m "Initial commit"
```

4. **Add GitHub repository as a remote**
```bash
git remote add origin <repo-link>
```

5. **Rename your branch to main**
```bash
git branch -M main
```

6. **Push code to GitHub**
```bash
git push -u origin main
```

---
