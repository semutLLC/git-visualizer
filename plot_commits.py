import subprocess
from collections import Counter
import matplotlib.pyplot as plt


result = subprocess.run(
    ["git", "log", "--pretty=format:%an"],
    capture_output=True,
    text=True,
)

authors = result.stdout.splitlines()
counts = Counter(authors)

top = counts.most_common(10)

names = [x[0] for x in top]
values = [x[1] for x in top]

plt.figure(figsize=(10, 6))
plt.barh(names, values)
plt.xlabel("Commits")
plt.ylabel("Author")
plt.title("Top Contributors")
plt.tight_layout()
plt.show()