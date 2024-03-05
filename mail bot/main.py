PLACEHOLDER = "[name]"


with open("invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    print(names)

with open("starting_letter.txt", mode="r") as letter:
    letter_content = letter.read()
    for name in names:
        formatted_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, formatted_name)
        with open(f"letter_for_{formatted_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
            