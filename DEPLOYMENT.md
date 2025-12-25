# GitHub Pages Deployment Guide

This repository is configured to deploy automatically to GitHub Pages using GitHub Actions.

## Deployment URL

The site is accessible at: **https://ucumotionlab.github.io/labwebsite/**

Note: Since the repository is named `labwebsite` (not `UCUmotionlab.github.io`), this is a "project site" and will be accessible at the `/labwebsite/` path.

## How It Works

1. **GitHub Actions Workflow**: The `.github/workflows/jekyll.yml` workflow automatically builds and deploys the site whenever changes are pushed to the `main` branch.

2. **Build Process**: The workflow uses Jekyll to build the static site from the markdown files and templates.

3. **Deployment**: After building, the site is automatically deployed to GitHub Pages.

## First-Time Setup

If this is the first deployment, you need to enable GitHub Pages in the repository settings:

1. Go to the repository on GitHub
2. Click on **Settings**
3. Navigate to **Pages** in the left sidebar
4. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
5. Save the settings

Once GitHub Pages is enabled with "GitHub Actions" as the source, the workflow will automatically deploy on every push to `main`.

## Manual Deployment

You can also trigger a deployment manually:

1. Go to the **Actions** tab in the repository
2. Select the "Deploy Jekyll site to Pages" workflow
3. Click "Run workflow"
4. Select the `main` branch
5. Click "Run workflow"

## Troubleshooting

### 404 Error

If you get a 404 error when accessing the site:

1. **Check GitHub Pages is enabled**: Go to Settings → Pages and ensure the source is set to "GitHub Actions"
2. **Check workflow status**: Go to the Actions tab and verify the latest workflow run completed successfully
3. **Wait a few minutes**: Sometimes it takes a few minutes for changes to propagate after deployment
4. **Verify the URL**: Make sure you're accessing `https://ucumotionlab.github.io/labwebsite/` (note the trailing slash and `/labwebsite/` path)

### For Organization Root URL

If you want the site to be accessible at `https://ucumotionlab.github.io/` (without the `/labwebsite/` path), you would need to:

1. Rename this repository to `UCUmotionlab.github.io` or `ucumotionlab.github.io`
2. This would make it an "organization site" instead of a "project site"

## Testing Locally

To test the site locally before deploying:

```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000 in your browser
```

## Site Structure

- `index.md` - Home page
- `about.md` - About page
- `research.md` - Research page
- `team.md` - Team page
- `_layouts/` - Page templates
- `_includes/` - Reusable components
- `_config.yml` - Jekyll configuration
