import pandas as pd 
pd.set_option('display.expand_frame_repr', False)													#To show all columns when priting dataframe.

path = 'C:\\Users\\Shiv\\Documents\\Datasets\\CSV\\Cars.csv'
#names = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9']
countries_df = pd.read_csv(path, delimiter = ';', skiprows = range(1,2))

print("Q. Print the data type of the Model attribute in the dataset.")
print(countries_df['Model'].dtypes)

print("Q. Print the 9th car name in the dataset.")
print(countries_df['Car'][9], end="\n\n")															#access through [col_name][row_num]
#print(countries_df['Model'][1] + countries_df['Model'][350])

print('Q. Print any 10 Origin-Car pairs from the dataset.')
print(countries_df[['Origin','Car']].sample(10), end="\n\n")										#sample() / head() / tail() | Two brackets because inner brackets form a list of items

print("Q. Print the first 5 data entries having Origin = Japan.")
print(countries_df[countries_df.Origin == 'Japan'].head(), end="\n\n")								#You can use df.col_name instead of []. countries_df.Car[9] will print the 9th car

print("Q. Print the last 5 Cars and Model-number entries in the dataset, originating in Europe.")
print(countries_df[['Origin', 'Car', 'Model']][countries_df.Origin == 'Europe'].tail())				#Any order is allowed