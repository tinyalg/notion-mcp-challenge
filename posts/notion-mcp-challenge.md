---
title: AI-Powered Content Pipeline: Notion → GitHub → dev.to
description: Building a 'human-in-the-loop' content management system with Notion MCP, GitHub, and automated publishing for the Notion MCP Challenge
tags:
  - devchallenge
  - notionchallenge
  - mcp
  - ai
published: false
canonical_url: https://dev.to/challenges/notion-2026-03-04
---

*This is a submission for the [Notion MCP Challenge](https://dev.to/challenges/notion-2026-03-04)*

## What I Built

I built a **human-in-the-loop content publishing pipeline** that empowers creators to focus on **writing and editorial decisions** while automation handles the technical infrastructure.

**The Problem**: Content creators waste time on infrastructure:
- Wrestling with Git commands and Markdown conversion
- Managing deployment pipelines and publishing APIs
- Tracking which files correspond to which articles
- Coordinating between writing tools, version control, and publishing platforms

**The Solution**: A workflow where **you stay in control** while automation handles the rest:

1. **You write in Notion** - Focus on content, not tooling
2. **You review PRs in GitHub** - Maintain quality control and editorial oversight
3. **Automation handles everything else** - Git operations, format conversion, deployment

This isn't about replacing human judgment with AI. It's about **amplifying your productivity** by eliminating tedious technical work, so you can focus on what matters: creating great content and making editorial decisions.

### Key Features

✅ **Conversation-Driven Draft Creation** - Start articles through natural conversation, which creates initial drafts in Notion

✅ **Write & Edit in Notion** - Use Notion's rich editor to refine and polish your content with formatting, collaboration, and organization features

✅ **Conversation-Driven Publishing** - Push to GitHub and create PRs through simple conversation, no Git commands required

✅ **Human Review & Quality Control** - Review PRs to verify everything before it goes live

✅ **Automated Deployment** - Merge a PR to automatically publish to dev.to via GitHub Actions

## How I Used Notion MCP

Notion MCP was the **core enabler** of this workflow:

### 1. Dynamic Schema Evolution

Used `notion-update-data-source` to programmatically add the `filename` property through conversation.

### 2. Content Extraction & Transformation

Used `notion-fetch` to retrieve structured content with properties, then transformed it into Markdown with YAML frontmatter.

### 3. Workflow Orchestration

Combined Notion MCP with GitHub operations: fetch from Notion → create branch → commit file → create PR.

### 4. Human-in-the-Loop Design: You Decide, Automation Executes

This system is intentionally designed with **human decision-making at its core**:

**What YOU do (the important parts):**
- Write and edit content in Notion
- Review PRs to catch issues (typos, formatting, metadata errors)
- Make the final "publish" decision by merging the PR
- Maintain editorial quality and content strategy

**What AUTOMATION does (the tedious parts):**
- Convert Notion content to Markdown with YAML frontmatter
- Create Git branches and commits
- Open pull requests
- Trigger deployment after you approve

**Why this matters:** Fully automated publishing can push mistakes live. Human review creates a **quality gate** where you verify everything looks right before it goes public. This is especially critical for:
- Technical accuracy
- SEO metadata (tags, descriptions, canonical URLs)
- Code examples and syntax
- Brand voice and messaging

You're not removed from the process—**you're elevated above the infrastructure**, free to focus on content quality instead of Git commands.

### 5. Practical Design Decisions

**Notion as Single Source of Truth**: All content editing happens in Notion. GitHub serves as version control and publication staging, not as an editing environment. This keeps the workflow simple and prevents synchronization conflicts.

**Why GitHub as an intermediary?** You might wonder: couldn't Claude just publish directly from Notion to dev.to? Technically yes—Claude can call the Forem API. Here's why GitHub matters anyway:

1. **Version control = Safety net**: GitHub serves as a backup. If something goes wrong with Notion (accidental deletion, formatting issues, or even AI mistakes), you can always restore from GitHub's commit history.

2. **Quality gate**: The PR review step catches errors before they go live. Direct publishing would push mistakes immediately—PR review gives you a checkpoint to verify everything looks right.

3. **Multi-platform foundation**: GitHub creates a platform-agnostic markdown format. The same files can publish to dev.to, Hashnode, Medium, or Zenn without rewriting the workflow.

4. **Team collaboration**: Multiple people can review and approve content before publication, with comments and feedback tracked in the PR.

5. **Audit trail**: GitHub's commit history provides a complete record of all changes—who made them, when, and why. This is invaluable for understanding how content evolved over time.

**Manual sync when needed**: If you make quick fixes directly in GitHub (typos, formatting), you can manually copy-paste back to Notion when needed (Cmd+A, Cmd+C, Cmd+V). This is simpler and more reliable than automated bidirectional sync.

### 6. Automated Publishing (Already Implemented!)

The system includes a GitHub Actions workflow that automatically publishes articles to dev.to when PRs are merged:

- ✅ **Automatic publishing** - Merging to `main` branch triggers publication
- ✅ **Article ID tracking** - Published article IDs are written back to the Markdown files
- ✅ **Selective publishing** - Only changed files in `posts/` directory are processed
- ✅ **Dry run mode** - Test the workflow before actual publication

The complete pipeline: Write in Notion → Push to GitHub → Review PR → Merge → Auto-publish to dev.to

### 7. Future Enhancements

The architecture supports additional capabilities:

**Planned Features**:
- ✅ **Analytics integration** - Pull view counts and reactions from dev.to back to Notion
- ✅ **Multi-platform publishing** - Same workflow for Hashnode, Medium, Zenn, Qiita
- ✅ **Content calendar** - Schedule publishing via Notion date properties

**Explicitly NOT doing**:
- ❌ **GitHub → Notion auto-sync** - Adds complexity without real benefit. Manual copy-paste when needed is simpler and more reliable.

## Want to Try It Yourself?

**Here's the crazy part**: You don't need to write any code.

### The User Experience

You just talk to Claude:

> "Hey Claude, fetch this article from Notion and push it to GitHub"

Claude handles:
- Reading Notion's API documentation
- Formatting your content as Markdown with YAML frontmatter
- Creating Git branches
- Making commits
- Opening pull requests
- All the JSON, schema definitions, and API parameters

**You never see that complexity.** It just works.

### What You DON'T Do

❌ Write JSON  
❌ Write API calls  
❌ Configure webhooks  
❌ Set up CI/CD pipelines  
❌ Write any code

### Setup Required

To get started, you'll need:
1. A Notion database (2 minutes to create)
2. A GitHub repository (30 seconds to create)
3. GitHub Personal Access Token configured in Claude (one-time setup)

**Detailed setup guide coming soon** - will link here once published!

### The Real Value

This isn't about "look how smart I am at writing API calls." It's about:

**"I want to write articles in Notion and publish them to dev.to without thinking about Git, Markdown conversion, or deployment."**

And now you can. Through conversation.

## Technical Highlights

1. **Conversation-Driven Development** - Built entirely through natural language
2. **Zero Manual Configuration** - All schema updates done programmatically
3. **Scalable Architecture** - Works for 1 article or 1,000 articles
4. **No Code Required** - Users write zero JSON, zero API calls. The technical complexity exists but is completely abstracted away
5. **End-to-End Conversation Loop** - Even the demo video was created by feeding the conversation artifacts (Markdown files from GitHub) into NotebookLM. The system's outputs become inputs for the next stage of automation. This complete loop demonstrates true conversation-driven workflow: write in Notion → push to GitHub → generate video → all through natural language interaction

**Repository**: https://github.com/tinyalg/notion-mcp-challenge

**Built with**: Notion MCP, GitHub API, Claude Sonnet 4.5

#devchallenge #notionchallenge #mcp #ai
