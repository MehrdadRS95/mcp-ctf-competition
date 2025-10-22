# Competition Overview

With the growing capabilities of Large Language Models (LLMs), AI systems are now able to identify software
vulnerabilities, analyze binaries, and even generate exploit code — skills traditionally honed through Capture the
Flag (CTF) competitions.

In this event, participants will design and deploy autonomous AI agents capable of solving security challenges with
human assistance. Your goal is to build or extend an agentic system powered by LLMs and MCP servers that can reason,
plan, and execute commands to solve multiple CTF domains.

Participant's must find the flags in their interactions with LLM.

## Objective

Develop an AI agent that autonomously analyzes, reasons, and interacts with CTF challenges to discover hidden flags.
Participants may:

Bring their own agent framework, or 
Enhance the provided baseline agent built with Model Context Protocol (MCP) components.

Agents can use:

Hosted models (e.g., GPT, Claude, Gemini), or

Local open-source models integrated via MCP servers or APIs.

Technical documentation and starter examples (including sample MCP servers) will be provided to help you get started.

## Challenge Categories

Your AI agent will face tasks drawn from standard CTF categories, such as:

#### Crypto – Cryptographic puzzles, weak key generation, or message recovery.

#### Forensics – Memory dumps, packet captures, or file-system investigations.

#### Pwn / Binary Exploitation – Stack-based, heap-based, or ROP-style challenges.

#### Reverse Engineering – Decompiled binaries or obfuscated scripts.

#### Web Exploitation – Logic flaws, injection, and authentication bypass.

#### Miscellaneous – Combined or unconventional problems requiring creative reasoning.

## Repository Structure

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
├── mcp-shell-server/            # Example reference MCP server
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

## Challenge 1 — Browser-Check

Here is an example of an agent developed using the mcp-shell-server to solve a web CTF challenge. Participants are
expected to develop similar autonomous agents based on this example to tackle their own CTF challenges.

### 🧠 Objective

Build or adapt an MCP server that **interfaces with a simulated browser** to verify certain conditions (e.g., content
parsing, HTTP response validation, or tool-based execution).

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

## Building and Running MCP Servers

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
        "properties": {
          "cmd": {
            "type": "string"
          }
        },
        "required": [
          "cmd"
        ]
      },
      "output_schema": {
        "type": "object",
        "properties": {
          "stdout": {
            "type": "string"
          },
          "stderr": {
            "type": "string"
          }
        }
      }
    }
  ]
}
```

---

## Challenge Workflow

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

## Rules & Guidelines

* Each team may submit multiple MCP servers.
* Each challenge must be solved by a separate MCP server instance.
* Secure coding practices are mandatory — e.g., no unrestricted shell access.
* Solutions must demonstrate correct use of the **MCP spec** (tool schemas, request-response structure).
* Use of AI-assisted tools is allowed if the code follows MCP logic.

---

What We Collect as Proof

🧩 The flag found

- All steps (tool calls, outputs, LLM reasoning steps if logged)

- A digital signature or hash proving no one changed the logs

- Optional replay video or script showing the same result

## 🏁 Scoring and Evaluation

### RULES

**Team Participation**: Teams of up to 3 people are allowed. Individual participation is also possible, but teamwork is
highly recommended.

**Evaluation**: will be based entirely on the number of challenges successfully solved by the autonomous agent. Each
correctly solved challenge contributes to the team’s final score, with no partial credit. The accuracy of the extracted
flag, as verified against the ground truth, is the sole criterion for success.

**Submissions**: For each solved CTF challenge, participants must submit the full trajectory generated by their
autonomous agent, including the agent’s thoughts, actions, observations, and the final flag, in a machine-loadable
format (e.g., JSON or structured log). The extracted flag must exactly match the ground-truth flag provided in the
metadata. Manual editing or tampering of the agent outputs is strictly prohibited and will result in disqualification.
In addition, participants must provide a well-documented Git repository containing the complete codebase of their
agentic framework. Open-source is encouraged, but a private repository shared with the organizer is also doable. This
repository should include all dependencies, configurations, and tools used, along with detailed technical documentation
outlining the participant’s approach—such as prompting techniques, model usage, agent architecture, tool integration,
and any other implementation details. If a custom or fine-tuned model is used, training code and model weights should
also be provided for validation. ​Submissions are now open.

## Judging

100 points in total, the final grade would be the weighted sum of all the judging criteria

### Challenge Solved (50%):

The number of CTF challenges solved by the participants, based on the score of each puzzle.

- **Definition**: The number and difficulty of CTF challenges solved autonomously by the team’s AI agent(s).

- **Scoring**: Based on the cumulative flag points earned across all domains (e.g., Web, Pwn, Forensics, Crypto, AI
  Security).

- **Requirements**: Flags must be discovered through the MCP-based automation framework (not manually entered).

### Creativity (30%):

- The methods used for finding the vulnerabilities and solving the challenges. Adding innovative
  features to the framework, and trying unique approaches are all vectors for evaluation. Ultimately, be sure to include
  a
  summary about how the puzzle was solved by the LLM. Using your own agent instead of the agent provided in the
  competition will give contestants a bonus under that judging criteria.


- ### Penalty items (deduction of 10% of the challenge score for each rule violation): The final solution must be provided
    - By the automation framework with prompt engineering techniques, even if the participants come up with the proper
      solutions by themselves. Penalty items will be applied if the final solution does not come from the generative AI,
      even if
      participants find the correct solution independently. No points will be awarded for this challenge when
      participants
      use online writeups and source code to form or train the agent.

## 🧑‍💻 Organizers

Maintained by:
**Mehrdad Rostamzadeh** — Old Dominion University
*Research focus: MCP Security, LLM Agents, and Autonomous CTF frameworks.*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
