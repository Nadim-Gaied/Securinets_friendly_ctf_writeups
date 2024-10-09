import string
import random
import matplotlib.pyplot as plt
from collections import Counter
import unicodedata


def process_text(input_text):
    # Normalize input to remove accents, then eliminate spaces, make uppercase, and replace non-alphabetical characters with '?'
    normalized_text = unicodedata.normalize('NFD', input_text)
    cleaned_text = ''.join([char for char in normalized_text if unicodedata.category(char) != 'Mn'])  # Remove accents
    processed_text = ''.join([char.upper() if char.isalpha() else '?' for char in cleaned_text if char != ' '])
    return processed_text


def generate_caesar_mapping():
    # Generate a random mapping of each letter to another letter
    letters = list(string.ascii_uppercase)
    shuffled_letters = letters.copy()
    random.shuffle(shuffled_letters)
    return dict(zip(letters, shuffled_letters))


def encrypt_text(processed_text, caesar_mapping):
    # Encrypt the text using the Caesar cipher mapping
    encrypted_text = ''.join([caesar_mapping[char] if char.isalpha() else '?' for char in processed_text])
    return encrypted_text


def plot_frequencies_combined(original_text, encrypted_text):
    # Count the frequency of each alphabetical character
    original_counter = Counter([char for char in original_text if char.isalpha()])
    encrypted_counter = Counter([char for char in encrypted_text if char.isalpha()])

    letters = string.ascii_uppercase
    original_frequencies = [original_counter[char] for char in letters]
    encrypted_frequencies = [encrypted_counter[char] for char in letters]

    # Create positions for side-by-side bars
    x = range(len(letters))

    # Plot the frequencies before and after encryption
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.bar([pos - 0.2 for pos in x], original_frequencies, width=0.4, label='Original Text', color='b')
    ax.bar([pos + 0.2 for pos in x], encrypted_frequencies, width=0.4, label='Encrypted Text', color='r')

    ax.set_xticks(x)
    ax.set_xticklabels(letters)
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequencies Before and After Encryption')

    ax.legend()

    plt.show()


# Example usage:

text = "From Wikipedia, the free encyclopedia The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down the alphabet. The cipher illustrated here uses a left shift of 3, so that (for example) each occurrence of E in the plaintext becomes B in the ciphertext. In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of posit Securinets{Thiswasyourfirstfrequencyattackwellexecutedboss} ions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence. The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security."
processed_text = process_text(text)
caesar_mapping = generate_caesar_mapping()
encrypted_text = encrypt_text(processed_text, caesar_mapping)

print(f"Processed Text: {processed_text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Caesar Cipher Mapping: {caesar_mapping}")

# Plot the frequency of characters before and after encryption in a single plot
plot_frequencies_combined(processed_text, encrypted_text)
