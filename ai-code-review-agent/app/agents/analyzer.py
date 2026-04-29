import os

class Analyzer:
    def run(self, repo_path):
        issues = []
        for root, _, files in os.walk(repo_path):
            for f in files:
                if f.endswith(".py"):
                    issues.append({"file": f, "problem": "demo issue", "code": "print('debug')"})
        return issues
