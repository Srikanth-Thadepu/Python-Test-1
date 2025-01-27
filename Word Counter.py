def count_words(sentence):
    word_counts = {}
    words = sentence.split()
    for word in words:
        word = word.lower().strip(".,!?")
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def main():
    sentence = input("Enter a sentence: ")
    word_counts = count_words(sentence)
    print("\nWord occurrences:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

main()
