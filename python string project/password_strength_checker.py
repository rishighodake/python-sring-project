def check_password_strength(password):
    """Return the strength label and the password requirements that are met."""
    checks = {
        "At least 8 characters": len(password) >= 8,
        "An uppercase letter": any(character.isupper() for character in password),
        "A lowercase letter": any(character.islower() for character in password),
        "A digit": any(character.isdigit() for character in password),
        "A special character": any(
            not character.isalnum() for character in password
        ),
    }

    score = sum(checks.values())
    if score == len(checks):
        strength = "Strong"
    elif score >= 3:Python String Assignments (Using String Methods)
1. Take a string input and convert it to uppercase.
2. Take a string input and convert it to lowercase.
3. Count the total number of characters in a string.
4. Count the number of vowels in a string.
5. Count the number of consonants in a string.
6. Check whether a string starts with a given substring.
7. Check whether a string ends with a given substring.
8. Remove leading and trailing spaces from a string.
9. Replace all spaces in a string with hyphens (-).
10. Find the index of a given character in a string.
11. Count how many times a particular character appears in a string.
12. Split a sentence into words using split().
13. Join a list of words into a single string.
14. Check whether a string is alphanumeric.
15. Check whether a string contains only alphabets.
16. Check whether a string contains only digits.
17. Capitalize the first character of a string.
18. Convert the first character of each word to uppercase.
19. Swap uppercase characters to lowercase and vice versa.
20. Remove all occurrences of a given character from a string.
21. Find the length of a string without using len().
22. Reverse a string using string methods.
23. Check whether a string is a palindrome.
24. Extract only digits from a string.
25. Extract only alphabets from a string.
26. Find the first and last occurrence of a character.
27. Check whether a word exists in a sentence.
28. Count the number of words in a sentence.
29. Replace a word with another word in a sentence.
30. Check whether a string is in title case.
31. Remove punctuation marks from a string.
32. Check whether all characters in a string are lowercase.
33. Check whether all characters in a string are uppercase.
34. Find the ASCII value of each character in a string.
35. Convert a string into a list of characters.
36. Remove duplicate characters from a string.
37. Find the longest word in a sentence.
38. Find the shortest word in a sentence.
39. Check whether a string is a valid identifier.
40. Count uppercase and lowercase letters separately.
41.
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, checks


def main():
    password = input("Enter a password to check: ")
    strength, checks = check_password_strength(password)

    print(f"\nPassword strength: {strength}")
    print("Requirements:")
    for requirement, is_met in checks.items():
        status = "Yes" if is_met else "No"
        print(f"- {requirement}: {status}")


if __name__ == "__main__":
    main()
