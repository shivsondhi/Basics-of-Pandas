import pandas as pd

pd.set_option('display.expand_frame_repr', False)

path = 'Zoo.csv'
zoo = pd.read_csv(path, delimiter = ',')

path_1 = 'C:\\Users\\Shiv\\Documents\\Datasets\\CSV\\Travel-log.csv'
names = ["date_time", "event", "country", "user_id", "source", "topic"]
df = pd.read_csv(path_1, names = names, delimiter = ';')

print(zoo.head(), end = "\n\n")												#ends with two newline characters
print(df.head(), end = "\n\n")

print("Basic statistics you can check with pandas: \tcount \tsum \tmin \tmax \tmean\tmedian:")
print("Number of elements in Zoo dataset: ", end = "")						#no newline character after print
print(zoo.uniq_id.count())
print("Sum of water needed: ", end = "")
print(zoo.water_need.sum())
print("Min of animal (These functions don't work well with string objects): ", end = "")
print(zoo.animal.min())
print("Max of water needed: ", end = "")
print(zoo.water_need.max())
print("Mean of each attribute: ")
print(zoo.mean())
print("Median of each attribute: ")
print(zoo.median(), end="\n\n")

print("Q. Calculate mean water usage of each animal in the Zoo dataset.")
print(zoo[['animal', 'water_need']].groupby('animal').mean(), end="\n\n")

print("Q. How many logs does country_2 have in each source-topic pairing?")
print(df[df.country == 'country_2'].groupby(['source', 'topic']).count()[['country']])
