import subprocess
from collections import defaultdict

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

expertise = defaultdict(lambda: defaultdict(int))

current_author = None

for line in result.stdout.splitlines():

    if line.startswith("AUTHOR:"):
        current_author = line.replace("AUTHOR:", "")
        continue

    if not line.strip():
        continue

    expertise[current_author][line] += 1

for author in expertise:

    print(f"\n{author}")

    top_files = sorted(
        expertise[author].items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    for filename, count in top_files:
        print(f"  {filename:<30} {count}")