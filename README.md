# About

Matching CISA KEV with CVEs from GitHub Advisories, for npm ecosystem.

Based on [Exploring the GitHub Advisory Database for fun and (no) profit](https://blog.aquia.us/blog/2024-02-27-gh-advisory-db/)

## Setup

Clone a bare-bones version of the GitHub Advisory Database:

```bash
git clone git@github.com:github/advisory-database.git --depth 1
```

Then setup a Python environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash

python3 app.py
```

## Output

```bash
17052
{'ecosystem': 'npm', 'name': 'electron'}
{'ecosystem': 'npm', 'name': 'electron'}
{'ecosystem': 'npm', 'name': 'mongo-express'}
{'ecosystem': 'npm', 'name': 'systeminformation'}
{'ecosystem': 'npm', 'name': 'puppeteer'}
['npm']
```
