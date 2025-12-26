#!/usr/bin/env python3
"""
Citation generation script.
Fetches publications from ORCID and other sources, generates citations.yaml.
"""

import os
import sys
import yaml
import json
import requests
from datetime import datetime
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "_data"
SOURCES_FILE = DATA_DIR / "sources.yaml"
CITATIONS_FILE = DATA_DIR / "citations.yaml"


def load_sources():
    """Load the sources.yaml file."""
    if not SOURCES_FILE.exists():
        return []
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def fetch_orcid_works(orcid_id):
    """Fetch works from ORCID API."""
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Warning: Could not fetch ORCID works for {orcid_id}: {e}")
        return None


def extract_doi_from_work(work):
    """Extract DOI from an ORCID work record."""
    external_ids = work.get("external-ids", {}).get("external-id", [])
    for ext_id in external_ids:
        if ext_id.get("external-id-type") == "doi":
            return ext_id.get("external-id-value")
    return None


def fetch_crossref_metadata(doi):
    """Fetch metadata from CrossRef API."""
    url = f"https://api.crossref.org/works/{doi}"
    headers = {"User-Agent": "MovEngLab-Website/1.0 (mailto:pablo.iturralde@ucu.edu.uy)"}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json().get("message", {})
    except requests.RequestException as e:
        print(f"Warning: Could not fetch CrossRef metadata for {doi}: {e}")
        return None


def parse_crossref_authors(authors):
    """Parse authors from CrossRef format."""
    result = []
    for author in authors:
        given = author.get("given", "")
        family = author.get("family", "")
        if given and family:
            result.append(f"{given} {family}")
        elif family:
            result.append(family)
    return result


def create_citation_from_crossref(doi, metadata):
    """Create a citation entry from CrossRef metadata."""
    title = metadata.get("title", [""])[0] if metadata.get("title") else ""

    # Parse date
    date_parts = metadata.get("published", {}).get("date-parts", [[None]])
    if date_parts and date_parts[0]:
        year = date_parts[0][0] or ""
        month = date_parts[0][1] if len(date_parts[0]) > 1 else 1
        day = date_parts[0][2] if len(date_parts[0]) > 2 else 1
        date = f"{year}-{month:02d}-{day:02d}" if year else ""
    else:
        date = ""

    authors = parse_crossref_authors(metadata.get("author", []))

    publisher = metadata.get("container-title", [""])[0] if metadata.get("container-title") else ""

    return {
        "id": f"doi:{doi}",
        "title": title,
        "authors": authors,
        "publisher": publisher,
        "date": date,
        "link": f"https://doi.org/{doi}",
    }


def load_orcid_config():
    """Load ORCID IDs from orcid.yaml."""
    orcid_file = DATA_DIR / "orcid.yaml"
    if not orcid_file.exists():
        return []
    with open(orcid_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    return [item.get("orcid") for item in data if item.get("orcid")]


def main():
    """Main entry point."""
    print("Starting citation generation...")

    # Ensure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    citations = []
    seen_dois = set()

    # Load manually specified sources
    sources = load_sources()
    for source in sources:
        source_id = source.get("id", "")
        if source_id.startswith("doi:"):
            doi = source_id[4:]
            if doi not in seen_dois:
                metadata = fetch_crossref_metadata(doi)
                if metadata:
                    citation = create_citation_from_crossref(doi, metadata)
                    # Merge with source overrides
                    citation.update({k: v for k, v in source.items() if v})
                    citations.append(citation)
                    seen_dois.add(doi)
        else:
            # Non-DOI source, include as-is
            citations.append(source)

    # Fetch from ORCID profiles
    orcid_ids = load_orcid_config()
    for orcid_id in orcid_ids:
        print(f"Fetching works from ORCID: {orcid_id}")
        works_data = fetch_orcid_works(orcid_id)
        if not works_data:
            continue

        groups = works_data.get("group", [])
        for group in groups:
            work_summaries = group.get("work-summary", [])
            if not work_summaries:
                continue

            work = work_summaries[0]  # Take first summary
            doi = extract_doi_from_work(work)

            if doi and doi not in seen_dois:
                metadata = fetch_crossref_metadata(doi)
                if metadata:
                    citation = create_citation_from_crossref(doi, metadata)
                    citations.append(citation)
                    seen_dois.add(doi)

    # Sort by date (newest first)
    citations.sort(key=lambda x: x.get("date", ""), reverse=True)

    # Write citations file
    with open(CITATIONS_FILE, "w", encoding="utf-8") as f:
        yaml.dump(citations, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Generated {len(citations)} citations -> {CITATIONS_FILE}")


if __name__ == "__main__":
    main()
