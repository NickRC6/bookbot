def total_words(path):
    with open(path, "r", encoding="utf-8") as f:
        num_words = len(f.read().split())
    return num_words

def character_repetition(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    counts = {}

    for char in content: 
        if char.isalpha():
            char = char.lower()
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    return counts

def sort_dict(book_path):

    counts = character_repetition(book_path)
    result = []

    for char, num in counts.items():
        result.append({"char": char, "num": num})
    result.sort(reverse=True, key=lambda x: x["num"])

    return result

def report(book_path):
    count = sort_dict(book_path)
    words = total_words(book_path)
    print ("============ BOOKBOT ============")
    print (f"Book:Analyzing book found at {book_path}")
    print ("----------- Word Count ----------")
    print (f"Found {words} total words")
    print ("--------- Character Count -------")
    for entry in count: 
        print(f"{entry['char']}: {entry['num']}")