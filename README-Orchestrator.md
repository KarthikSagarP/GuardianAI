
# GuardianAI-Orchestrator 🌿🛡️

Welcome! This little repo is a cosy prototype showing how a friendly Orchestrator can ask two specialist AI tools to work together: a Legal Analyst that reads rules, and a Code Auditor that checks code for compliance. Think of it as a tiny, helpful robot friend that looks after your code's safety and accessibility.

Why it's wholesome: it breaks a big, scary compliance task into two clear, human-friendly steps so developers can act on simple, actionable guidance.

## What this repo contains

- `main.py` — The Orchestrator: it asks the Legal Analyst for a developer-friendly technical brief, then asks the Code Auditor to scan a repo and return violations as JSON.
- `contracts.py` — Lightweight contract stubs and mock implementations. Great for prototyping — swap them out for real tools when you're ready.
- `markdown.md` — Project plan, diagrams, and developer notes (a friendly blueprint for next steps).

## Quick start (Windows PowerShell) 🖥️✨

Follow these steps to get a local, playful demo running.

1. Install Python 3.8+ if you don't already have it.

2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install example dependencies

This is a prototype, so the exact packages depend on how you wire up the real tools. Here are some commonly used packages for LLM + RAG flows — adjust as needed:

```powershell
pip install langchain google-generative-ai gitpython pypdf2 chromadb
```

4. Add your Google API key

Set the environment variable the orchestrator expects:

```powershell
$env:GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
```

5. Try the demo

Edit the `regulation_pdf` and `repository_url` values in `main.py` (or add CLI args later), then run:

```powershell
python main.py
```

You should see a friendly technical brief, the mock auditor output, and a final JSON report printed to the console.

## The friendly contract 🤝

These two functions are the heart of the handshake between parts of the system:

- `legal_analyst_tool(pdf_file_path: str, question: str) -> str` — Read a regulatory PDF and return a plain-English technical brief for devs.
- `code_auditor_agent(repo_url: str, technical_brief: str) -> str` — Clone/scan a repo using the brief and return a JSON string of violations.

`contracts.py` currently has playful mock implementations. Replace them with your RAG pipeline (for `legal_analyst_tool`) and repository-auditor (for `code_auditor_agent`) when you're ready to go beyond the prototype.

## Tips, assumptions & next steps 🌱

- Assumptions used for this README:
  - The demo uses a Google generative LLM via `GOOGLE_API_KEY`.
  - The repository's current tools are mocks meant for quick iteration.

- Friendly next steps:
  1. Add a `requirements.txt` with exact packages and versions for reproducibility.
  2. Implement a RAG-based `legal_tool.py` (PDF ingestion → embeddings → retriever → QA) and a robust `code_tool.py` that clones repos and queries the LLM in small chunks.
  3. Add CLI flags to `main.py` so you can run `python main.py --pdf path/to/doc.pdf --repo https://github.com/you/repo`.
  4. Add tests: a unit test for the orchestrator (mock the tools) and a small integration test using sample PDFs and tiny test repositories.

## Privacy & Security ✨

- Never commit secrets (API keys, tokens) to the repo. Use environment variables or a secure secrets manager.
- For private repo scans, prefer short-lived tokens and limited scopes.

## Want help? I'm excited to help further 🎉

If you'd like, I can:

- Build a `requirements.txt` tailored to the exact libraries you'd like to use.
- Implement `legal_tool.py` (RAG pipeline) and `code_tool.py` (repo cloning + chunked LLM queries).
- Add a friendly CLI and a couple of unit/integration tests.

Tell me which provider and libraries you'd like to use and I can start implementing the next piece.

---

Generated on: 2025-10-25

