from agents.analyzer import Analyzer
from agents.generator import Generator
from agents.validator import Validator
from agents.risk_agent import RiskAgent

class Orchestrator:
    def __init__(self):
        self.analyzer = Analyzer()
        self.generator = Generator()
        self.validator = Validator()
        self.risk = RiskAgent()

    def run(self, repo_path):
        issues = self.analyzer.run(repo_path)
        results = []

        for issue in issues:
            fix = self.generator.run(issue)
            if self.risk.evaluate(fix) == "high":
                continue
            if self.validator.run(fix):
                results.append(fix)

        return results
