import pandas as pd


fp = 'nato_phonetic_alphabet.csv'
df = pd.read_csv(fp, sep=',')
#dict_df = df.to_dict()

nato_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}

user_input = input('Enter your name: ')
user_letters = [letter for letter in user_input]
print(user_letters)