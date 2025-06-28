import pandas

df = pandas.DataFrame(pandas.read_csv("./nato_phonetic_alphabet.csv"))
phonetic_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

user_name = input("Enter your name? ").upper()

phonetic_alphabet_code = [phonetic_dictionary[letter] for letter in user_name]
print(phonetic_alphabet_code)