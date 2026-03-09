---
title: Setup Guide: Notion to GitHub Publishing Pipeline
description: Step-by-step guide to set up the AI-powered content publishing workflow using Notion MCP, GitHub, and Claude
tags:
  - ai
published: false
---

# Setup Guide: Notion to GitHub Publishing Pipeline

This guide walks you through setting up an AI-powered content publishing workflow that connects Notion, GitHub, and dev.to.

## What You'll Build

A system where you:
1. Write articles in Notion
2. Push them to GitHub via conversation with Claude
3. Automatically publish to dev.to (or any platform)

**No coding required** - everything is done through conversation.

## Prerequisites

- Notion account (free tier works)
- GitHub account (free tier works)
- Claude.ai account with Notion MCP enabled
- Docker installed (for GitHub MCP server)
- 20-30 minutes for initial setup

## Step 1: Create Notion Database (2 minutes)

1. Open Notion
2. Click "New" → "Database"
3. Add these properties:
   - `title` (Title) - already exists
   - `description` (Text)
   - `tags` (Multi-select)
   - `published` (Checkbox)
   - `filename` (Text)
   - `canonical_url` (URL)

**Screenshot placeholder**: [Notion database with properties]

## Step 2: Create GitHub Repository (30 seconds)

1. Go to github.com
2. Click "New" repository
3. Name it (e.g., `my-blog-content`)
4. Make it Public or Private (your choice)
5. Click "Create repository"

**Screenshot placeholder**: [GitHub repo creation]

## Step 3: Generate GitHub Personal Access Token (5-10 minutes)

**This is the trickiest part**, but you only do it once.

### Why You Need This

Claude needs permission to create branches, commit files, and open PRs on your behalf. GitHub uses Personal Access Tokens (PAT) for this.

### Steps:

1. Go to GitHub Settings → Developer settings
2. Click "Personal access tokens" → "Tokens (classic)"
3. Click "Generate new token (classic)"
4. Name it: "Claude MCP Integration"
5. Set expiration: 90 days (or longer)
6. Select scopes:
   - ☑️ `repo` (Full control of private repositories)
   - ☑️ `workflow` (Update GitHub Actions workflows)
7. Click "Generate token"
8. **IMPORTANT**: Copy the token immediately - you can't see it again!

**Screenshot placeholder**: [GitHub PAT generation screen]

### Security Note

Treat this token like a password. Anyone with this token can access your repositories.

## Step 4: Configure MCP Servers (5-10 minutes)

### 4a. Enable Notion MCP

1. Open Claude.ai
2. Go to Settings → Features
3. Enable "Notion" integration
4. Follow the prompts to connect your Notion workspace

### 4b. Configure GitHub MCP Server

**Important**: This requires editing a configuration file.

1. **Locate your Claude configuration file:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. **Edit the configuration file** and add the GitHub MCP server:

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_PAT_HERE"
      }
    }
  }
}
```

3. **Replace `YOUR_GITHUB_PAT_HERE`** with the Personal Access Token you generated in Step 3

4. **Save the file**

5. **Restart Claude** (quit and reopen the app)

**Note**: This configuration uses Docker. Make sure Docker is installed and running on your system.

**Screenshot placeholder**: [Configuration file example]

## Step 5: Test the Connection (2 minutes)

Now let's make sure everything works:

1. Create a test page in your Notion database
2. Fill in: title, description, filename (e.g., "test-article.md")
3. Talk to Claude:

> "Hey Claude, fetch the article titled '[your title]' from my Notion database and push it to my GitHub repository [repo-name]"

Claude should:
- Fetch the article from Notion
- Create a new branch
- Commit the Markdown file
- Open a pull request

If this works, **you're done!** 🎉

## Troubleshooting

### "Permission denied" error
- Check your PAT has the correct scopes (`repo`, `workflow`)
- Make sure PAT hasn't expired
- Regenerate token if needed

### "Database not found"
- Make sure Notion MCP is connected to your workspace
- Try fetching the database URL first

### "Branch already exists"
- Use a different branch name
- Or delete the existing branch in GitHub

### "MCP server not found"
- Make sure Docker is running
- Check the configuration file syntax (valid JSON)
- Restart Claude after editing the config file

## Next Steps

Once setup is complete:

1. Write articles in Notion
2. Use Claude to push them to GitHub
3. Review the PR
4. Merge to publish
5. (Optional) Set up GitHub Actions for auto-publishing to dev.to

## FAQ

**Q: Do I need to renew the PAT?**  
A: Yes, when it expires. Set a calendar reminder.

**Q: Can I use this with private repositories?**  
A: Yes! The `repo` scope covers both public and private repos.

**Q: What if I want to publish to multiple platforms?**  
A: The same workflow works - just point to different publishing APIs.

**Q: Is my content secure?**  
A: Your Notion content stays in Notion. GitHub repos can be private. Claude doesn't store your content.

**Q: Do I need Docker?**  
A: Yes, the GitHub MCP server runs in a Docker container. Make sure Docker Desktop is installed and running.

## Support

Having issues? Check:
- [Notion MCP Documentation](https://docs.notion.com/)
- [GitHub PAT Guide](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [Claude.ai Help Center](https://support.anthropic.com/)

---

**Related**: [Main Project Post](link-to-challenge-submission)

**Built with**: Notion MCP, GitHub API, Claude Sonnet 4.5
