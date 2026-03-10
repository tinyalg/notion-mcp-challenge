# Zero-Friction Publishing: A Human-in-the-Loop Agentic CMS powered by Notion MCP

This is the exact repository where I approved my own submission for the Notion MCP Challenge, triggering a GitHub Actions workflow that automatically published it to dev.to. 

Before hitting merge, the workflow started with this simple conversation:

> **Me:**  Fetch and convert to markdown the draft with the `filename` "posts/notion-mcp-challenge.md" from the Notion database. Open a PR in tinyalg/notion-mcp-challenge repo, targeting `main`, using the branch name specified in its `github_branch` property.
> 
> You MUST properly escape all newlines with `\n`, double quotes with `\"`, and formatting when constructing the JSON payload for the tool. DO NOT pass raw markdown, and DO NOT use `\t` for newlines.
>
> Before executing the tool, you must decode the escaped string in your head back to Markdown and strictly verify that it is a 100% perfect match with the original draft. If you fail to escape it properly, the GitHub action will break. Do it perfectly.
> 
> **Claude:** Got it. Let me read the properties via Notion MCP. I'll format the content with YAML frontmatter, create the branch you specified, and open a Pull Request for you.

## 🏗 Workflow Overview

This diagram shows the overview of the workflow I presented. It defines the interaction between the AI Orchestrator (Claude), the Human Director, and the external systems.

```mermaid
graph TD
 subgraph Legend_Box["Legend"]
        L1["🟧 Thick Orange Line: External System Operation via MCP"]
  end
 subgraph CMS_Phase["CMS & Human Edit"]
        Author(("You: Editor"))
        Notion[("Notion: Structured CMS")]
  end
 subgraph Notion_Structure["Notion Database Schema"]
    direction LR
        Prop1["title"]
        Prop2["Content"]
        Prop3["filename"]
  end
    Input(("You: Director")) == "1. Convey Intent (Natural Language)" ==> Claude["Claude Sonnet 4.5: Orchestrator"]
    Claude == "2. Save Initial Draft" ==> Notion
    Notion == "4. Fetch Edited Content" ==> Claude
    Claude == "6. Create PR" ==> GitHub{{"GitHub: Version Control"}}
    Author -- "3. Refine & Polish Draft" --> Notion
    Claude -- "5. Transform to MD + YAML" --> Claude
    User(("You: Final Approver")) -- "8. Merge (The 'Publish' Signal)" --> GitHub
    GitHub -- "7. Review PR (Diff Check)" --> User
    GitHub -- "9. Actions (Triggered by Merge)" --> devto(("dev.to: Live"))
    Prop1 --- Prop2
    Prop2 --- Prop3
    Notion -.-> Notion_Structure

     Claude:::claudeStyle
    classDef claudeStyle fill:#e6e6fa,stroke:#7b68ee,stroke-width:2px,color:#333
    style L1 fill:#ffffff,stroke:none,color:#333,rx:5,ry:5
    linkStyle 1 stroke:#ff964f,stroke-width:6px,fill:none
    linkStyle 2 stroke:#ff964f,stroke-width:6px,fill:none
    linkStyle 3 stroke:#ff964f,stroke-width:6px,fill:none
```

## 🛠 Setup & Configuration

### 1. Notion Schema

The AI orchestrator relies on this specific schema to manage the publishing lifecycle. 

![Notion Database Schema](notion-database-schema.png)

To make the AI orchestrator act predictably, I defined a strict schema in the Notion Database:

* **title**: The main headline of your post.
* **published**: A boolean to control visibility.
* **description**: Used for SEO and dev.to's summary.
* **tags**: Automates categorization.
* **organization_username**: Allows publishing under a specific dev.to organization when GitHub workflow uses the [Publish to Dev.to Organization Action](https://github.com/marketplace/actions/publish-to-dev-to-organization).
* **canonical_url**: Maintains SEO integrity for cross-posted content.
* **cover_image**: Managed via URL to handle article headers.
* **filename**: The exact ID for the `.md` file in the GitHub repo.
* **github_branch**: Tells the AI which branch to target for the PR.

### 2. MCP Integration

The workflow relies on two core MCP servers:

* **Notion MCP Server**: For structured data I/O.

  Remote MCP servers for Notion in Claude Desktop are configured through Settings → Connectors. See details at https://developers.notion.com/guides/mcp/get-started-with-mcp
* **GitHub MCP Server**: For repository management and PR creation.

  MCP servers for GitHub in Claude Desktop are configured through the  `claude_desktop_config.json` file, with Docker installed on your machine.
  See details at https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md


*Created for the [Notion MCP Challenge](https://dev.to/challenges/notion-2026-03-04).*
