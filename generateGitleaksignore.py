import json

def print_unique_commit_shas(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        commit_shas = set()

        for run in data.get("runs", []):
            for result in run.get("results", []):
                commit_sha = result.get("partialFingerprints", {}).get("commitSha")
                if commit_sha:
                    commit_shas.add(commit_sha)

        for sha in commit_shas:
            print(sha)

def print_uri_ruleid_startline(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

        for run in data.get("runs", []):
            for result in run.get("results", []):
                rule_id = result.get("ruleId")
                for location in result.get("locations", []):
                    uri = location.get("physicalLocation", {}).get("artifactLocation", {}).get("uri")
                    start_line = location.get("physicalLocation", {}).get("region", {}).get("startLine")
                    if uri and rule_id and start_line:
                        print(f"{uri}:{rule_id}:{start_line}")

# Example usage
print_uri_ruleid_startline('results.sarif')
