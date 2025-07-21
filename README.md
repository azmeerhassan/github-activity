# 📊 GitHub User Activity CLI

A simple command line tool to fetch and display the recent activity of any GitHub user using the GitHub public API — built without any external libraries.

---

## 🧠 Features

- Fetches recent public events from a GitHub user
- Parses and displays them in a human-readable format
- Handles errors like invalid usernames, rate limits, and network failures
- Lightweight: built using only Python’s standard library

---

## 🚀 How to Use

### 1. Clone this repository

```bash
git clone https://github.com/your-username/github-activity.git
cd github-activity
````

### 2. Run the script

```bash
python github_activity.py <github_username>
```

**Example:**

```bash
python github_activity.py torvalds
```

---

## ✅ Output Example

```
📋 Recent Activity:
📌 Pushed 3 commit(s) to torvalds/linux
🐛 Opened issue in torvalds/linux
⭐ Starred torvalds/linux
```

---

## 🛠️ Tech Used

* Python 3.x
* `sys`, `urllib.request`, `json`

---

## ⚠️ Notes

* Only shows **public** events (private activity is not accessible)
* API limit: 60 requests/hour (unauthenticated)

---

## 📂 Project Structure

```
github-activity/
├── github_activity.py
└── README.md
```

---

## 🙌 Author

Built with 💻 by Azmeer Hassan Ammad

````

---

### ✅ Final Steps

1. Save this file as `README.md` in your project folder
2. Then run:

```bash
git add README.md
git commit -m "📝 Added README with usage instructions and output example"
git push
````

---

