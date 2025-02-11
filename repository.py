import subprocess
import os

class Repository:
    def __init__(self, repo_dir="swift-evolution", proposals_file_name="proposals"):
        self.repo_dir = repo_dir
        self.proposals_file_name = proposals_file_name

    def get_recently_changed_proposals(self, num_files=2):
        result = subprocess.run(
            ["git", "log", "--name-only", "--pretty=format:", "--", self.proposals_file_name],
            cwd=self.repo_dir,
            capture_output=True, text=True
        )

        changed_files = list(dict.fromkeys([
            f.strip() for f in result.stdout.split("\n")
            if f.strip().startswith("proposals/") and f.strip().endswith(".md")
        ]))

        proposals = {}
        for proposal_file in changed_files[:num_files]:
            proposal_path = os.path.join(self.repo_dir, proposal_file)

            if os.path.exists(proposal_path):
                with open(proposal_path, "r", encoding="utf-8") as f:
                    proposals[proposal_file] = f.read()
            else:
                proposals[proposal_file] = "Proposal file not found."

        return proposals  # {"FILE_NAME": "FILE_CONTENTS"}
