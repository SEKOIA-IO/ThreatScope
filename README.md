# 🔎 ThreatScope

ThreatScope is a lightweight demo application that lets you explore a simulated **cyber threat landscape**.  
Select your **industry** and **operating countries**, and the app shows relevant **threat actors, malware, and risks**.  

This repository is used for **recruitment exercises**.  
If you're a candidate: welcome 👋 and thank you for your time!

## 📸 Demo

👉 Live app: [https://threatscope-i0tj.onrender.com](https://threatscope-i0tj.onrender.com)  
👉 Live documentation: [https://sekoia-io.github.io/ThreatScope/](https://sekoia-io.github.io/ThreatScope/)  
👉 Live swagger docs: [https://threatscope-i0tj.onrender.com/docs](https://threatscope-i0tj.onrender.com/api)  

Test account:  
* username: alice
* password: secret2

---

## 🚀 How to Get Started

You will receive a **private repository** via **GitHub Classroom**.  
This ensures your work remains private and only visible to you and the reviewers.

You have two options for working on the exercises:

### 🔹 Option 1 — Run in GitHub Codespaces (recommended)
- Click the **“Code” → “Open with Codespaces”** button in your private repo.  
- A ready-to-use cloud development environment will open in your browser.  
- You don’t need to install anything locally.  

### 🔹 Option 2 — Run on your computer
If you prefer to work locally:  
1. Make sure you have **Python 3.11+** installed.  
2. Install [uv](https://github.com/astral-sh/uv) (dependency manager).  
   - macOS/Linux:  
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```  
   - Windows (PowerShell):  
     ```powershell
     irm https://astral.sh/uv/install.ps1 | iex
     ```  
3. Clone your private repo and install dependencies:  
   ```bash
   git clone <your-private-repo-url>
   cd ThreatScope
   uv sync
   ```
4. Run the app
   ```bash
   uv run uvicorn app.main:app --reload
   ```
   * Web UI → http://127.0.0.1:8000   
   * API → http://127.0.0.1:8000/api
   * Swagger docs → http://127.0.0.1:8000/docs

## 📚 Documentation Website

ThreatScope’s documentation is built with MkDocs (Material theme).

* Start docs server:   
```bash
uv run mkdocs serve
```

You’ll see something like:
```nginx
INFO - Serving on http://127.0.0.1:8001/
```
Open the shown URL in your browser.

* Build static docs:
```bash
uv run mkdocs build
```
Output will be in the site/ folder.

## 📝 Exercises

All candidate tasks are described in EXERCISES.md
They cover:
* Microcopy polish (in-app)
* Documentation writing (intro page)
* API docs & OpenAPI
* Creative enhancement
* Data-driven thinking

👉 Please read the “How to Answer” section at the top of EXERCISES.md before starting.
