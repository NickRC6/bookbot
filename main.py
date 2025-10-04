from stats import report
import sys

if len(sys.argv) != 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main(book_path):
    report(book_path)    
    
main(book_path)

