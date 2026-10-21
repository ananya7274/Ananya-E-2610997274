print("=" * 45)
print("          DOCUMENT ANALYSIS REPORT")
print("=" * 45)
sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0
for char in sentence:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    elif char.isdigit():
        digits += 1

    elif char == " ":
        spaces += 1

    else:
        special_characters += 1
words = len(sentence.split())
total_letters = vowels + consonants
if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0.0
print("\n" + "=" * 45)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 45)

print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")

print("\n--- Character Breakdown ---")
print(f"Words: {words}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special_characters}")

print("\n--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")

print("\n" + "=" * 45)
print("Analysis Complete!")
print("=" * 45)