---
title: "Zero-Friction Publishing: A Human-in-the-Loop Agentic CMS powered by Notion MCP"
published: false
description: "Discover how to build a zero-friction, human-in-the-loop publishing pipeline. Turn Notion into an AI-powered Headless CMS using Notion MCP and GitHub."
tags: ["devchallenge","notionchallenge","mcp","ai"]
organization_username: ""
canonical_url: ""
cover_image: "https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5lldnomk3p2s30rfymva.png"
---

*This is a submission for the [Notion MCP Challenge](https://dev.to/challenges/notion-2026-03-04)

## What I Built

> **Me:** I intend to submit to the Notion MCP challenge. Will the workflow below be a good application?
>
> **Claude:** This is a strong submission concept! Let me break down how it stacks up against the judging criteria...
>
> **Me:** Can you draft my submission using the template below and store it to the Notion database using the filename `notion-mcp-challenge.md`?
>
> **Claude:** First, let me search for the publishing database in your Notion workspace to store this in...
> *(Claude uses Notion MCP to connect to the database)*
> Done! The initial draft has been saved directly to your Notion CMS.

This actual conversation is how this entire project—and the very article you are reading—started. 

While AI can generate content instantly, maintaining high quality, personal voice, and strict formatting requires a "Human-in-the-loop" approach. I built a **Zero-Friction Agentic Publishing Pipeline** that turns Notion into a collaborative Headless CMS between a human creator and an AI orchestrator. 

Instead of juggling multiple tabs, manually converting formats, or dealing with Git commands, this workflow allows me to focus entirely on directing and editing. I simply converse with my AI agent (Claude), and it handles the heavy lifting of database management, file transformation, and version control via Notion MCP.

Here is the architecture of the workflow we established:

![Workflow Overview](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3jab950a9d31kvn8jws2.png)

**The Process:**
1. **Director Phase:** I initiate the idea via natural language.
2. **Drafting Phase:** The AI orchestrator generates the initial draft and saves it directly to a structured Notion database (mapping properties like `title`, `filename`, and metadata) using Notion MCP.
3. **Refinement Phase (Human-in-the-loop):** I jump into Notion—the best UI for writing—and refine the draft, adding my personal touch.
4. **Publishing Pipeline:** I tell the AI to finalize it. It fetches the updated content from Notion via MCP, transforms it into Markdown with YAML frontmatter internally, and creates a Pull Request on GitHub.
5. **Approval:** I review the PR diff and hit merge, triggering GitHub Actions to deploy the article live to [dev.to](http://dev.to).

## Video Demo

{% youtube xAelmJ6MLMs %}

This short presentation (generated via NotebookLM based on my initial drafts) explains the philosophy behind this setup. As highlighted in the video, this is **Conversation-driven development**. You will see how I can orchestrate a complex Notion-to-GitHub pipeline without writing a single line of traditional code—relying entirely on the system architecture (the Mermaid diagram) and natural language prompts.

## Show us the code

The absolute beauty of this Agentic Workflow is that it requires **zero traditional middleware code**. By leveraging standard MCP servers, the "code" shifts from writing brittle API wrappers to defining CI/CD pipelines and database schemas.

**1. The Repository & CI/CD Pipeline**

The GitHub repository is the central hub where the AI and I collaborate. 

- **AI Opens PRs:** Claude, via the GitHub MCP server, dynamically opens Pull Requests and pushes updates based on the Notion drafts.
- **Human Approval:** I review the Markdown and YAML frontmatter in the PR diff. This is the crucial "Human-in-the-loop" checkpoint.
- **Automated Deployment:** Once I hit "Merge", a GitHub Action automatically triggers and publishes the article to [dev.to](http://dev.to). 

You can explore the actual repository powering this workflow here:

👉 [https://github.com/tinyalg/notion-mcp-challenge](https://github.com/tinyalg/notion-mcp-challenge)

**2. The Notion Schema (The "Data Model" for Frontmatter)**

When Claude opens a Pull Request, it extracts the draft from Notion and transforms it into a standard Markdown file. During this process, it generates the YAML frontmatter using the exact properties stored in the Notion database. 

This strict schema is the secret sauce that allows the AI to act predictably:

![Notion Schema](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ja6ct9klj4y5xx9ovoyo.png)

- **`title`**: The main headline of your post.
- **`published`**: A boolean to control visibility.
- **`description`**: Used for SEO and dev.to's summary.
- **`tags`**: Automates categorization.
- **`organization_username`**: Allows publishing under a specific [dev.to](http://dev.to) organization when GitHub workflow uses the [Publish to Dev.to Organization Action](https://github.com/marketplace/actions/publish-to-dev-to-organization).
- **`canonical_url`**: Maintains SEO integrity for cross-posted content.
- **`cover_image`**: Managed via URL to handle article headers.
- **`filename`**: The exact ID for the `.md` file in the GitHub repo.
- **`github_branch`**: Tells the AI which branch to target for the PR.
- **`Content`**: (The page body) The shared canvas for AI generation and human editing.

### 3. The AI's Toolkit (Overcoming the JSON Escape Hell)

During testing, I hit a physical limit of current LLMs: the "Stringification Hell." When Claude tried to pass the final, complex Markdown (with YAML, Mermaid diagrams, and newlines) to the GitHub MCP, it struggled to perfectly escape the massive JSON payload. At one point, to avoid syntax errors, the AI even "cheated" by silently stripping out every single newline character—resulting in a completely flattened file!

To solve this without breaking the "Zero-Friction" philosophy, I added a simple, deterministic Python script ([`escape_mcp_payload.py`](https://github.com/tinyalg/notion-mcp-challenge/blob/main/escape-mcp-payload.py)) directly into the repository.

Now, instead of wrestling with prompt engineering for JSON escaping, my natural language instruction is simply:

> Fetch and convert to markdown the draft with the `filename` "notion-mcp-challenge.md" from the Notion database. Then, feed the markdown to the python script `escape_mcp_payload.py` and use the OUTPUT FROM THE SCRIPT for generating the JSON payload. Finally, create a PR targeting `main`, using the branch name specified in its `github_branch` property.

This is a paradigm shift: **The repository is no longer just a storage space; it is a literal toolbox.** By committing utility scripts to the repo, the AI agent can autonomously fetch and execute the deterministic tools it needs to overcome its own probabilistic limitations!

## How I Used Notion MCP

Notion MCP is the absolute core of this Agentic Workflow. It acts as the critical bridge that transforms Notion from a passive knowledge base into an active, collaborative workspace for AI and humans.

- **MCP Write:** I utilized the MCP to allow the LLM to dynamically create pages within my "Publishing CMS" database. It maps its generated ideas perfectly to the `title`, `filename`, and all metadata properties needed for production.
- **MCP Read:** After human intervention (my edits), the LLM uses MCP to read the exact Notion page, ensuring that the final output perfectly preserves human nuance before transforming it into strict Markdown/YAML for developers.

**What it unlocks:**

This integration completely eliminates "context switching" and "cognitive load." By leveraging Notion MCP, I don't have to copy-paste between a chat window, a text editor, and a terminal. The AI orchestrates the mundane system operations (formatting, API calls, Git commands), while I retain 100% creative control inside Notion's beautiful editing environment. This is the ultimate "human-in-the-loop" scaling system for any modern creator or developer!
