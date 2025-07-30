import Pandas as pd

# load in spam csv file
dataframe = pd.read_csv('spam.csv', encoding='ISO-8859-1')

# Rename the columns in neccessary
dataframe = dataframe[['v1', 'v2']]
dataframe.columns = ['label', 'message']

# preview data
print(dataframe.head())

# Check how many spam vs ham messages
print("\nLabel distribution:")
print(dataframe['label'].value_counts())