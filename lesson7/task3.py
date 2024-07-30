def count_each_letters (word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count
def main():
    word = input("write word: ")
    letter_counts = count_each_letters (word)
    print("letters in word: ")
    for letter, count in letter_counts.items():
        print(f"'{letter}': {count}")

if __name__ == "__main__":
    main()