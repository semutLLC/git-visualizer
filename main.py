import subprocess
from collections import Counter


def get_git_authors():
    result = subprocess.run(
        ["git", "log", "--pretty=format:%an"],
        capture_output=True,
        text=True,
        check=True,
    )

    authors = result.stdout.splitlines()
    return Counter(authors)


def main():
    authors = get_git_authors()

    print("\nTop Contributors\n")
    print("-" * 40)

    for author, count in authors.most_common():
        print(f"{author:<25} {count}")


if __name__ == "__main__":
    main()