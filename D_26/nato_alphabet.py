import pandas as pd


fp = 'nato_phonetic_alphabet.csv'
df = pd.read_csv(fp, sep=',')
#dict_df = df.to_dict()

nato_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}

user_input = input('Enter a word: ')
user_letters = [letter.upper() for letter in user_input]
user_nato = [nato_dict[letter] for letter in user_letters if letter in nato_dict]
print(user_nato)