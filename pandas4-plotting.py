import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
pd.set_option('display.expand_frame_repr', False)

#Cars 
path = 'Cars.csv'
df_cars = pd.read_csv(path, delimiter = ';', skiprows = range(1,2))
print("Cars dataset sample:\n", df_cars.sample(5), end="\n\n")
#Zoo
path_1 = 'Zoo.csv'
df_zoo = pd.read_csv(path_1, delimiter = ',')
print("Zoo dataset sample:\n", df_zoo.sample(5), end="\n\n")

#Scatter plot
scatter_df = scatter_matrix(df_cars, alpha=0.25)
plt.suptitle("Plot 1/5. Scatter plot of each attribute of the Cars dataset.")			#Set the main title using suptitle
plt.show()

#Histogram
df_zoo.water_need.plot(kind = 'hist', bins = 100, figsize = (12,6))						    #kind can also be (='scatter', x='', y='')
plt.title("Plot 2/5. Histogram plot of water_needs in Zoo dataset.")
plt.xlabel("Amount of water required by each animal")
plt.ylabel("Frequency")
plt.show()

#Box and Whisker
df_zoo.water_need.plot(kind = 'box')													#kind = 'kde'
plt.title("Plot 3/5. Box and Whisker plot of water_needs.")
plt.show()

#Area plot
df_zoo.water_need.plot.area(alpha = 0.1)
plt.title("Plot 4/5. Area plot of water_needs.")
plt.xlabel("Index number of animal")
plt.ylabel("Amount of water required by each animal")
plt.show()

#Line graph 
df_zoo.water_need.plot.line()
plt.title("Plot 5/5. Line plot of water_needs.")
plt.show()
