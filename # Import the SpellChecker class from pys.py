# Import the SpellChecker class from pyspellchecker
from spellchecker import SpellChecker

# Initialize the SpellChecker
spell = SpellChecker()

# Sample text with spelling errors
text = "The quik brown fox jumps ovver the lazi dog."

# Split the text into words
words = text.split()

# Find misspelled words
misspelled = spell.unknown(words)

# Output the original text
print("Original Text:")
print(text)
print("\nMisspelled Words:")

# Print misspelled words and their suggestions
for word in misspelled:
    print(f"{word} -> {spell.correction(word)}")

# Correct the misspelled words in the text
corrected_text = " ".join([spell.correction(word) if word in misspelled else word for word in words])

# Output the corrected text
print("\nCorrected Text:")
print(corrected_text)
