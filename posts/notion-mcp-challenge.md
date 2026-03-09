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

I built an **AI-powered content publishing pipeline** that transforms Notion into a powerful CMS (Content Management System) for technical writing, with seamless integration to GitHub version control and automated publishing to dev.to.

**The Problem**: Content creators often struggle with:
- Managing drafts and published content across multiple platforms
- Maintaining version history of articles
- Coordinating between writing, review, and publishing workflows
- Keeping track of which files correspond to which articles

**The Solution**: A fully automated workflow where:
1. **Write in Notion** - Use Notion's rich editing experience with a structured database
2. **Version control in GitHub** - Every article becomes a versioned Markdown file with pull request reviews
3. **Automated publishing** - Content flows to dev.to (or any platform) with proper metadata
4. **Feedback loop** - Publishing status flows back to Notion for tracking

### Key Features

✅ **Schema Evolution via Conversation** - Added database fields (like `filename`) through natural language, no UI clicking required

✅ **Automated Git Workflow** - Branch creation, commits, and PR generation from Notion content

✅ **Human-in-the-Loop** - PR review process ensures quality control before publishing

✅ **Bidirectional Tracking** - Notion properties link to GitHub files, enabling updates and republishing

✅ **Multi-Platform Ready** - The same pipeline can publish to dev.to, Hashnode, Medium, Zenn, or any platform with an API

## How I Used Notion MCP

Notion MCP was the **core enabler** of this workflow:

### 1. Dynamic Schema Evolution

Used `notion-update-data-source` to programmatically add the `filename` property through conversation.

### 2. Content Extraction & Transformation

Used `notion-fetch` to retrieve structured content with properties, then transformed it into Markdown with YAML frontmatter.

### 3. Workflow Orchestration

Combined Notion MCP with GitHub operations: fetch from Notion → create branch → commit file → create PR.

### 4. Human-in-the-Loop Design

PR review ensures quality control while AI handles the tedious parts.

### 5. Practical Design Decisions

**Notion as Single Source of Truth**: All content editing happens in Notion. GitHub serves as version control and publication staging, not as an editing environment. This keeps the workflow simple and prevents synchronization conflicts.

**Manual sync when needed**: If you make quick fixes directly in GitHub (typos, formatting), you can manually copy-paste back to Notion when needed (Cmd+A, Cmd+C, Cmd+V). This is simpler and more reliable than automated bidirectional sync.

### 6. Automated Publishing (Already Implemented!)

The system includes a GitHub Actions workflow that automatically publishes articles to dev.to when PRs are merged:

- ✅ **Automatic publishing** - Merging to `test-workflow` branch triggers publication
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
