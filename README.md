# Movement Engineering Lab Website

Website for the Movement Engineering Lab at Universidad Católica del Uruguay.

**Live site:** https://ucumovenglab.github.io

## Features

- Automatic publication fetching from ORCID (monthly)
- Bilingual content (Spanish/English)
- Team member profiles
- Research project pages
- Blog for news and updates
- Responsive design with UCU colors

## Local Development

### Prerequisites

- Ruby 3.x
- Python 3.x
- Bundler

### Setup

```bash
# Install Ruby dependencies
bundle install

# Install Python dependencies (for citation generation)
pip install -r _cite/requirements.txt

# Generate citations
python _cite/cite.py

# Run the site locally
bundle exec jekyll serve
```

The site will be available at http://localhost:4000

## Structure

```
├── _config.yaml          # Site configuration
├── _data/                # Data files
│   ├── citations.yaml    # Auto-generated publications
│   ├── orcid.yaml        # ORCID IDs for auto-fetch
│   ├── projects.yaml     # Research projects
│   └── sources.yaml      # Manual publication sources
├── _members/             # Team member profiles
├── _posts/               # Blog posts
├── _includes/            # Reusable components
├── _layouts/             # Page templates
├── _styles/              # Custom styles
├── images/               # Image assets
├── research/             # Research page
├── team/                 # Team page
├── projects/             # Projects page
├── contact/              # Contact page
└── blog/                 # Blog page
```

## Adding Content

### New Team Member

Create a file in `_members/` with:

```yaml
---
name: Full Name
image: images/team/photo.jpg
role: phd  # pi, phd, masters, undergrad, postdoc, staff
links:
  email: email@ucu.edu.uy
  orcid: 0000-0000-0000-0000
  github: username
---

Bio content in Markdown.
```

### New Blog Post

Create a file in `_posts/` named `YYYY-MM-DD-title.md`:

```yaml
---
title: Post Title
author: member-id
tags:
  - news
---

Post content in Markdown.
```

### Publications

Publications are auto-fetched from ORCID profiles listed in `_data/orcid.yaml`. To add manual publications, edit `_data/sources.yaml`.

## Deployment

The site automatically builds and deploys via GitHub Actions when you push to the `main` branch. Publications are refreshed monthly.

## TODO

- [ ] Add team member photos to `images/team/`
- [ ] Add project images to `images/projects/`
- [ ] Add background image
- [ ] Add campus photo for contact page
- [ ] Complete PI bios
- [ ] Add graduate student profiles

## Based On

[Greene Lab Website Template](https://github.com/greenelab/lab-website-template)
