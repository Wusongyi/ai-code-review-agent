class Generator:
    def run(self, issue):
        return {"file": issue["file"], "fix": "# fixed code"}
