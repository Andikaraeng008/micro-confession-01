import os

# Two-part micro-confession: a To: line plus one unsent line, exactly as typed.
# Gate: /output/entry.txt must be 1-260 chars; the message line is at most 200.
ENTRY = (
    "To: the neighbour who waters my plants when I'm away\n"
    "I slipped my spare key under your doormat last spring so you'd let yourself in — and I've waited by the door every morning since, just to hear you knock anyway."
)

def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
