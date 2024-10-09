def leetify(text):
    # Create a dictionary mapping letters to leet equivalents
    leet_dict = {
        'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5', 'T': '7',
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'
    }

    # Replace each character in the text using the leet_dict
    leet_text = ''.join([leet_dict.get(char, char) for char in text])

    return leet_text


# Example usage
input_text = 'That_WaS_Ur_FirsT_FreQuenCy_Attaaack_!'
print(len(input_text))
leetified_text = leetify(input_text)
print(leetified_text)

len = len(leetified_text) - 3
possibilities = pow(36,len)
print(possibilities)
print(possibilities > 100000001)