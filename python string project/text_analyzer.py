from string import punctuation


def analyze_text(text):
    """Return common character, word, sentence, and word-frequency statistics."""
    normalized_text = " ".join(text.split())
    words = text.split()

    character_counts = {
        "vowels": 0,
        "consonants": 0,
        "digits": 0,
        "special_characters": 0,
    }

    for character in text:
        if character.isalpha():
            if character.lower() in "aeiou":
                character_counts["vowels"] += 1
            else:
                character_counts["consonants"] += 1
        elif character.isdigit():
            character_counts["digits"] += 1
        elif not character.isspace():
            character_counts["special_characters"] += 1

    sentence_count = 0
    previous_was_terminator = False
    for character in text:
        is_terminator = character in ".!?"
        if is_terminator and not previous_was_terminator:
            sentence_count += 1
        previous_was_terminator = is_terminator

    word_frequencies = {}
    for word in words:
        clean_word = word.strip(punctuation).lower()
        if clean_word:
            word_frequencies[clean_word] = word_frequencies.get(clean_word, 0) + 1

    return {
        "normalized_text": normalized_text,
        "character_count": len(text),
        "word_count": len(words),
        "sentence_count": sentence_count,
        **character_counts,
        "word_frequencies": word_frequencies,
    }


def main():
    text = input("Enter a sentence or paragraph: ")
    results = analyze_text(text)

    print("\n--- Text Analysis ---")
    print(f"Characters (including spaces): {results['character_count']}")
    print(f"Words: {results['word_count']}")
    print(f"Sentences: {results['sentence_count']}")
    print(f"Vowels: {results['vowels']}")
    print(f"Consonants: {results['consonants']}")
    print(f"Digits: {results['digits']}")
    print(f"Special characters: {results['special_characters']}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Text with extra spaces removed: {results['normalized_text']}")

    search_word = input("\nEnter a word to search for: ").strip().lower()
    if search_word in results["word_frequencies"]:
        print(f'"{search_word}" exists in the text.')
    else:
        print(f'"{search_word}" was not found in the text.')

    print("\nWord frequencies:")
    if results["word_frequencies"]:
        for word, frequency in sorted(results["word_frequencies"].items()):
            print(f"{word}: {frequency}")
    else:
        print("No words to count.")


if __name__ == "__main__":
    main()
