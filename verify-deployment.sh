#!/bin/bash

# GitHub Pages Deployment Verification Script
# This script checks if the GitHub Pages site is accessible
#
# Usage: ./verify-deployment.sh
# If you get a permission error, run: chmod +x verify-deployment.sh

# Check if curl is available
if ! command -v curl >/dev/null 2>&1; then
    echo "❌ Error: curl is not installed"
    echo "Please install curl first:"
    echo "  - Ubuntu/Debian: sudo apt-get install curl"
    echo "  - macOS: curl is pre-installed"
    echo "  - Windows: Install from https://curl.se/windows/"
    exit 1
fi

SITE_URL="https://ucumotionlab.github.io/labwebsite/"

echo "🔍 Checking GitHub Pages deployment..."
echo "Site URL: $SITE_URL"
echo ""

# Check if the site is accessible
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -L "$SITE_URL" 2>/dev/null)

if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ SUCCESS! Site is accessible"
    echo "HTTP Status: $HTTP_CODE"
    echo ""
    echo "Your site is live at: $SITE_URL"
elif [ "$HTTP_CODE" = "404" ]; then
    echo "❌ 404 ERROR - Page not found"
    echo ""
    echo "Possible causes:"
    echo "1. GitHub Pages is not enabled in repository settings"
    echo "2. The workflow hasn't completed yet"
    echo "3. DNS hasn't propagated yet (wait a few minutes)"
    echo ""
    echo "To fix:"
    echo "1. Go to https://github.com/UCUmotionlab/labwebsite/settings/pages"
    echo "2. Set Source to 'GitHub Actions'"
    echo "3. Wait a few minutes and try again"
elif [ -z "$HTTP_CODE" ]; then
    echo "⚠️  Could not connect to site"
    echo "This might be a network issue or DNS hasn't propagated yet"
else
    echo "⚠️  Unexpected response: HTTP $HTTP_CODE"
fi

echo ""
echo "To manually verify, visit: $SITE_URL"
