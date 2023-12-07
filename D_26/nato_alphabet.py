import pandas as pd


fp = 'nato_phonetic_alphabet.csv'
df = pd.read_csv(fp, sep=',')
dict_df = df.to_dict()
print(dict_df)