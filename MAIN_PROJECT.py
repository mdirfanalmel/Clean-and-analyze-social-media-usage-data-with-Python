import pandas as pd
import numpy as np
import random
categories= pd.Series(["Food", "Travel", "Fashion", "Fitness", "Music", "Culture", "Family", "Health"])
n=500
data = {
     'Date': pd.date_range('2013-08-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}

#print dataframe
df=pd.DataFrame(data)
print("data farme Head")
print(df.head(10))

# Print DataFrame Information
print("data frame information ")
print(df.info())

# Print DataFrame Description
print("data frame discription")
print(df.describe())

# Print the count of each 'Category' element
category_counts = df['Category'].value_counts()
print("\nCount of each 'Category' element:")
print(category_counts)