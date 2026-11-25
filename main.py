import os

# Two-part micro-confession: a To: line plus one unsent line, exactly as typed.
# Gate: /output/entry.txt must be 1-260 chars; the message line is at most 200.
ENTRY = (
    "To: the man who bought my childhood house\n"
    "I still drive past on Sundays to check whether you kept the treehouse, and I have never once knocked."
)

def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
