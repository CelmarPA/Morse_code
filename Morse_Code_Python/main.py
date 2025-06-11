# Import libraries
from unicodedata import normalize

# Dict with the Morse Code
MORSE_CODE_DICT = {
    # Letters
    "A": ".-", "B": "-...",
    "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.",
    "G": "--.", "H": "....",
    "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.",
    "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-",
    "U": "..-", "V": "...-",
    "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",

    # Numbers
    "1": "·----", "2": "··---",
    "3": "···--", "4": "····-",
    "5": "·····", "6": "-····",
    "7": "--···", "8": "---··",
    "9": "----·", "0": "-----",

    # Common Punctuations
    ".": "·-·-·-", ",": "--··--",
    "?": "··--··", "'": "·----·",
    "!": "-·-·--", "/": "-··-·",
    "(": "-·--·", ")": "-·--·-",
    "&": "·-···", ":": "---···",
    ";": "-·-·-·", "=": "-···-",
    "-": "-····-", "_": "··--·-",
    '"': "·-··-·", "$": "···-··-",
    "@": "·--·-·"
}


def normalize_text(t):
    """
    :param t: string text
    :return: return the string text without accentuation
    """
    return normalize('NFKD', t).encode('ASCII', 'ignore').decode('ASCII')


def is_morse_like(s):
    """
    :param s: String containing the morse code
    :return: return True if s is morse code and False otherwise
    """
    return all(c in ".-· " for c in s)


def encode_text(text):
    """
    :param text: The text to be encoded to Morse Code
    :return: Return the Morse Code for the text
    """
    text = normalize_text(text.upper()) # Transform  accentuated letters in normal letters
    morse_code = ""

    for letter in text:
        #  If letter different of space get the morse code in the dict and add three spaces after
        if letter != " ":
            morse_code += MORSE_CODE_DICT.get(letter, "") + "   "
        else: # If the letter is a space add seven spaces between the worlds
            morse_code += "    "

    return morse_code


def decode_code(morse):
    """
    :param morse: The Morse Code to be decoded into text
    :return: Retorn the decoded text
    """
    decode_text = ""
    # Get every code in the Morse Code and get the key (letter or number of symbol) in the dict
    for code in morse.split("   "): # Separates the code taking into account the three spaces between letters
        if code != "":  # If code is different from an empty string ("")
            for key, value in MORSE_CODE_DICT.items():
                if value == code.replace(" ", ""):
                    decode_text += key
        else:   # The empty string represents the seven spaces between words só add the space in the text
            decode_text += " "

    return decode_text


def main():
    """
    The function main to execute the code inside the while loop.
    :return: None
    """
    print(f"======= Welcome to Morse Code Convertor ========")
    while True:
        option = input("Enter 1 to convert text into morse code, 2 for convert morse code into text and q or quit to exit:\n").upper()

        if option == "1":
            raw_text = input("Enter the text to be converted into Morse Code:\n")

            if len(raw_text) == 0:
                print("A text must be entered for conversion!")
            else:
                print(encode_text(raw_text))

        elif option == "2":
            morse_text = input("Enter the Morse Code to be converted into text:\n")

            if not is_morse_like(morse_text):
                print("The input must be valid Morse Code (only '.', '-' and spaces)")
            else:
                print(decode_code(morse_text))

        elif option[0] == "Q":
            print("Thank You!")
            return
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
