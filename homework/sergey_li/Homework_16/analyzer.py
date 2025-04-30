import argparse
import os


def extract_context(line, keyword):
    # Split line to words
    words = line.strip().split()
    # Here I try to find a key word index
    for i, word in enumerate(words):
        if keyword in word:
            # Get key word and 5 words before + 5 words after
            start = max(0, i - 5)
            end = min(len(words), i + 6)
            context = " ".join(words[start:end])
            return context
    return None


def search_logs(folder_path, keyword):
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                for line_number, line in enumerate(file, start=1):
                    if keyword in line:
                        context = extract_context(line, keyword)
                        print(f"File: {filename}, line: {line_number}")
                        print(f"Context: {context}\n")


def main():
    parser = argparse.ArgumentParser(description="Log analyzer")
    parser.add_argument("folder", help="Path to dir with logs")
    parser.add_argument("--text", required=True, help="Text for a search")
    args = parser.parse_args()

    folder_path = args.folder
    keyword = args.text

    if not os.path.isdir(folder_path):
        print("No such folder.")
        return

    search_logs(folder_path, keyword)


if __name__ == "__main__":
    main()
