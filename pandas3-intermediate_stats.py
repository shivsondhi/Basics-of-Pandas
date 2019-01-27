pd.set_option('display.expand_frame_repr', False)												#To show full view as opposed to summary view
import pandas as pd

path = 'Cars.csv'
df = pd.read_csv(path, delimiter = ';', na_values = ['0', ''], skiprows = range(1,2))			#na_values for handling empty values etc.

print(df.head(10), end="\n\n")

print("Summary of the data:")
print(df.describe(include = 'all'), end="\n\n")													#include can be ['object'] or ['number'] or 'all'

print("Correlation between attributes:")
print(df.corr(), end="\n\n")

print("Covariance of each attribute pair:")
print(df.cov())
