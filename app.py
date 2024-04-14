import pandas as pd
import glob
import json
import csv

kev_data = pd.read_csv('https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv')

kev_cves = set(kev_data['cveID'])

repo_path = 'advisory-database/advisories/github-reviewed/**/*.json'
json_files = glob.glob(repo_path, recursive=True)

data = []

# print the count of json_files that loaded using glob matching:
print(len(json_files))

for file in json_files:
    with open(file, 'r') as f:
        json_data = json.load(f)
        if any(cve in json_data.get('aliases', []) for cve in kev_cves):
            if json_data['affected'][0]['package']['ecosystem'] == 'npm':
                data.append(json_data['affected'][0]['package']['ecosystem'])
                print(json_data['affected'][0]['package'])

npm_ecosystems = list(set(data))
print(npm_ecosystems)

