MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '!': '-.-.--', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    """
    Converts a string of text into its Morse code equivalent.

    Args:
        text (str): The input string to be converted.

    Returns:
        str: The Morse code representation of the input string.
             Letters are separated by a single space.
             Words are separated by a forward slash '/'.
    """
    morse_code = ""
    # Iterate through each character in the input text.
    for char in text.upper():
        if char == ' ':
            # Add a separator for spaces between words.
            morse_code += "/ "
        elif char in MORSE_CODE_DICT:
            # Append the Morse code for the character, followed by a space.
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            # If the character is not in our dictionary (e.g., special symbols),
            # we can choose to ignore it or represent it in some way.
            # Here, we'll just keep the original character.
            morse_code += char + " "
            
    # .strip() removes any trailing space at the end.
    return morse_code.strip()

def main():
    """
    Main function to run the Morse Code Converter program.
    """
    print("--- Morse Code Converter ---")
    print("Enter the text you want to convert, or type 'exit' to close the program.")

    # Loop indefinitely to allow multiple conversions.
    while True:
        # Get input from the user.
        user_input = input("\nYour text: ")

        # Check if the user wants to exit the program.
        if user_input.lower() == 'exit':
            print("Thank you for using the Morse Code Converter. Goodbye!")
            break

        # Convert the input text to Morse code.
        converted_morse = text_to_morse(user_input)

        # Display the result.
        print(f"Morse Code: {converted_morse}")

# This ensures the main() function runs only when the script is executed directly.
if __name__ == "__main__":
    main()