import pandas

df = pandas.DataFrame(pandas.read_csv("./nato_phonetic_alphabet.csv"))
phonetic_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

def get_phonetic_codes():
    user_name = input("Enter your name? ").upper()

    try:
        phonetic_alphabet_code = [phonetic_dictionary[letter] for letter in user_name]
        print(phonetic_alphabet_code)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        get_phonetic_codes()

get_phonetic_codes()