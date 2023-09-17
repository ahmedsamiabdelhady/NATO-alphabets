import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {
    row.letter:row.code for (index, row) in data.iterrows()
}

username = input("Enter a word: ").upper()
code_list = [nato_dict[letter] for letter in username]
print(code_list)

