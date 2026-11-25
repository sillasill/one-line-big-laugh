import os

# One line, big laugh: the whole entry is a single self-contained joke.
LINE = "My resume says I'm a team player, which is corporate for 'I once hit reply-all and survived.'"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
