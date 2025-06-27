with open("./Input/Letters/starting_letter.txt") as doc:
    letter = doc.read()

with open("./Input/Names/invited_names.txt") as names:
    names = list(names.readlines())
    final_names = []
    for name in names:
        final_names.append(name.replace("\n", ""))

    for name in final_names:
        new_letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as send:
            send.write(new_letter)