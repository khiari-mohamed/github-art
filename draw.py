import os
import subprocess
from datetime import datetime, timedelta

PATTERN = [
"##  ##  ####  ##  ##  ###   ####  ###",
"### ### #  #  ##  ## #   #  #     #  #",
"# # # # #  #  ##  ## #   #  #     #   #",
"#  #  # #  #  ####  ##### ####  #   #",
"#  #  # #  #  ##  ## #   #  #     #   #",
"#  #  # #  #  ##  ## #   #  #     #  #",
"#  #  # ####  ##  ## #   #  ####  ###",
]

# 🔑 MUST be a Sunday
START_DATE = datetime(2025, 2, 2)  # Sunday

with open("art.txt", "w"):
    pass

for col in range(len(PATTERN[0])):          # weeks → columns
    for row in range(7):                     # days → rows
        if PATTERN[row][col] == "#":
            date = START_DATE + timedelta(weeks=col, days=row)
            iso = date.strftime("%Y-%m-%dT12:00:00")

            with open("art.txt", "a") as f:
                f.write(iso + "\n")

            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = iso
            env["GIT_COMMITTER_DATE"] = iso

            subprocess.run(["git", "add", "art.txt"], check=True)
            subprocess.run(
                ["git", "commit", "-m", "draw"],
                env=env,
                check=True
            )
