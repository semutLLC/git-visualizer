import subprocess
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

result = subprocess.run(
    [
        "git",
        "log",
        "--date=short",
        "--pretty=format:%ad"
    ],
    capture_output=True,
    text=True,
)

dates = result.stdout.splitlines()

months = []

for d in dates:
    dt = datetime.strptime(d, "%Y-%m-%d")
    months.append(dt.strftime("%Y-%m"))

counts = Counter(months)

x = sorted(counts.keys())
y = [counts[m] for m in x]

plt.figure(figsize=(12, 6))
plt.plot(x, y)
plt.xticks(rotation=45)
plt.title("Repository Activity Over Time")
plt.xlabel("Month")
plt.ylabel("Commits")
plt.tight_layout()
plt.show()