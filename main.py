import os
import pandas as pd
import numpy as np
import string
import re

texts = [file for file in os.listdir('text') if file.endswith('.txt')]

def get_text(chapter):
    with open('text/' + texts[chapter], 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def remove_punctuation(text):
    return "".join([char for char in text if char not in string.punctuation])

text = " ".join([get_text(chapter) for chapter in range(len(texts))])

df = pd.DataFrame(text.split('\n'), columns=['text'])
df.text = text.split('\n')

df['clean_text'] = df['text'].apply(lambda x: ' '.join(re.sub("(w+://S+)", " ", x).split()))
# print(df[['text', 'clean_text']].iloc[200])

df['clean_text'] = df['clean_text'].apply(lambda x: ' '.join(remove_punctuation(x).split()))
print(df[['text', 'clean_text']].iloc[3])

# print(text[:1000])






# df.info()
# df.clean_text

# data  = [['v1', 'v2']]
# data.head()

# data['v1'].value_counts()


# data['no_punc'] = remove_punctuation(get_text(0))
# data.head()

# There are 28 different texts
# print(get_text(26))

# pd.set_option('display.max_colwidth')
# data.head()
