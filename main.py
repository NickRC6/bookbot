def main():
    get_book_text("books/frankenstein.txt")

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    print(content)

main()

