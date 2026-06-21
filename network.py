import subprocess
from collections import defaultdict
from itertools import combinations

result = subprocess.run(
    [
        "git",
        "log",
        "--name-only",
        "--pretty=format:AUTHOR:%an"
    ],
    capture_output=True,
    text=True,
)

file_authors = defaultdict(set)

current_author = None

for line in result.stdout.splitlines():

    if line.startswith("AUTHOR:"):
        current_author = line.replace("AUTHOR:", "")
        continue

    if not line.strip():
        continue

    file_authors[line].add(current_author)

edges = defaultdict(int)

for filename, authors in file_authors.items():

    for a, b in combinations(sorted(authors), 2):
        edges[(a, b)] += 1

print("\nCollaboration Network\n")

for (a, b), count in sorted(
    edges.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{a} <-> {b} : {count}")