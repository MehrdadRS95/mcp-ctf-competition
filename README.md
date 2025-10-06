# mcp-ctf-competition
Here’s a **comprehensive `README.md`** tailored for your repository structure and competition concept — where participants must develop and deploy multiple **MCP servers** to solve different **CTF-style challenges** (with `Browser-Check` being the first challenge already included).

You can copy this directly into your repo’s root `README.md`:

---

# 🧩 MCP CTF Competition

Welcome to the **MCP CTF Competition** — a hands-on challenge series designed to test your skills in **Model Context Protocol (MCP)** server development, security reasoning, and AI integration.

In this competition, participants will **develop multiple custom MCP servers** to solve a series of CTF-style challenges.
Each challenge targets a unique aspect of **MCP interoperability, security, and reasoning**, pushing participants to think like both **AI developers** and **security researchers**.

---

## 🚀 Overview

### 🔹 Goal

Your mission is to **create MCP servers** that can:

* Correctly register and interact with an MCP client.
* Expose one or more tools (`/tools/...`) or capabilities that solve the given challenge logic.
* Follow secure design principles while enabling the client (and LLMs) to use your server to extract or compute the solution.

Each challenge provides:

* A pre-defined environment (e.g., Docker setup, certificates, and config files)
* A short problem description
* Reference input/output expectations

You must implement or modify an MCP server that **passes the challenge verification tests**.

---

## 🧱 Repository Structure

```bash
mcp-ctf-comp/
│
├── Browser-Check/               # 🧩 Challenge 1: Browser Interaction
│   ├── chall.py                 # Challenge logic (client or verifier)
│   ├── docker-compose.yml       # Challenge container setup
│   ├── Dockerfile               # Environment definition
│   ├── cert.pem / key.pem       # SSL certificate pair for secure comms
│   ├── requirements.txt         # Python dependencies
│   └── README.md                # Challenge-specific instructions
│
├── mcp-shell-server/            # 🧠 Example reference MCP server
│   ├── src/                     # Core implementation (tools, routes, etc.)
│   ├── tests/                   # Unit and integration tests
│   ├── Dockerfile               # Build definition
│   ├── Makefile                 # Build & test automation
│   ├── LICENSE, README.md       # Documentation
│   └── pyproject.toml           # Project metadata
│
├── mcp-use/                     # Example MCP client / runner setup
│   ├── mcp_shell_server.py      # Example script to invoke servers
│   ├── mcp-shell-server.json    # Config for connecting to a server
│   └── README.md                # Usage guide
│
├── LICENSE
└── .gitignore
```

---

## 🎯 Challenge 1 — Browser-Check

### 🧠 Objective

Build or adapt an MCP server that **interfaces with a simulated browser** to verify certain conditions (e.g., content parsing, HTTP response validation, or tool-based execution).

Your MCP server must:

* Register with a valid `mcp_server.json` manifest.
* Expose at least one `check_browser` or equivalent tool endpoint.
* Respond correctly to the validation script `chall.py`.

### 🧩 How to Run

```bash
cd Browser-Check
docker compose up --build
```

Then, in a separate terminal, test your MCP server:

```bash
python chall.py
```

---

## 🛠️ Building and Running MCP Servers

Each MCP server should:

1. **Expose a valid schema** (JSON manifest) with routes and input/output definitions.
2. **Follow the MCP specification** for tool invocation, context handling, and responses.
3. **Communicate over a secure channel** (TLS if required, using `cert.pem` and `key.pem`).

Example minimal manifest (`mcp-shell-server.json`):

```json
{
  "name": "mcp-shell-server",
  "id": "urn:mcp:shell:1",
  "version": "1.0.0",
  "description": "Example MCP server exposing shell commands",
  "tools": [
    {
      "name": "run_command",
      "route": "/tools/run_command",
      "description": "Executes a shell command",
      "input_schema": {
        "type": "object",
        "properties": { "cmd": { "type": "string" } },
        "required": ["cmd"]
      },
      "output_schema": {
        "type": "object",
        "properties": { "stdout": { "type": "string" }, "stderr": { "type": "string" } }
      }
    }
  ]
}
```

---

## 🧩 Challenge Workflow

1. **Clone this repository**

   ```bash
   git clone https://github.com/MehrdadRS95/mcp-ctf-competition.git
   cd mcp-ctf-competition
   ```

2. **Explore challenges**
   Each folder inside the repository (like `Browser-Check/`) represents one CTF challenge.

3. **Develop your MCP server**
   You can start from the provided template in `mcp-shell-server/` or build one from scratch.

4. **Test locally**
   Each challenge includes a test or validation script (like `chall.py`) to verify correct responses.

5. **Submit your solution**
   Depending on competition setup, submit your Docker image, source code, or server endpoint as instructed.

---

## 🧠 Example Development Flow

```bash
# 1. Start from template
cp -r mcp-shell-server my-custom-server

# 2. Implement your logic
nano my-custom-server/src/main.py

# 3. Build and run
docker build -t my-custom-server .
docker run -p 8080:8080 my-custom-server

# 4. Test with the challenge script
python Browser-Check/chall.py
```

---

## 🧾 Rules & Guidelines

* ✅ Each team may submit multiple MCP servers.
* 🧩 Each challenge must be solved by a separate MCP server instance.
* 🔐 Secure coding practices are mandatory — e.g., no unrestricted shell access.
* 🧠 Solutions must demonstrate correct use of the **MCP spec** (tool schemas, request-response structure).
* 🧰 Use of AI-assisted tools is allowed if the code follows MCP logic.

---

## 🏁 Scoring and Evaluation

| Criteria          | Description                                   | Points |
| ----------------- | --------------------------------------------- | ------ |
| ✅ Correctness     | Challenge solved as intended                  | 40     |
| ⚙️ MCP Compliance | Follows protocol spec and manifests correctly | 20     |
| 🧩 Innovation     | Creative or efficient server design           | 20     |
| 🔒 Security       | Proper sandboxing, validation, error handling | 20     |

---

## 🧑‍💻 Organizers

This repository is part of the **LLM-for-CTF initiative**, exploring how **LLMs interact with modular MCP servers** in secure sandboxed environments.

Maintained by:
**Mehrdad Rostamzadeh** — Old Dominion University
*Research focus: MCP Security, LLM Agents, and Autonomous CTF frameworks.*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Would you like me to extend this README with a **“Challenge Template Specification”** section (i.e., how to define a new challenge directory, its required files, and `chall.py` validation format)? That would make it easier for future contributors to add more challenges like `Cookie-Monster`, `Port-Scanner`, etc.
