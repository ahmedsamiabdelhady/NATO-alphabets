import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {
    row.letter:row.code for (index, row) in data.iterrows()
}

Error= True
while Error:
    username = input("Enter a word: ").upper()
    try:
        code_list = [nato_dict[letter] for letter in username]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
    else:
        print(code_list)
        Error=False

