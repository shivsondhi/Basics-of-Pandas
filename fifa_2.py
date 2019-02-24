'''
More information file.

Demonstrates:- 
	Find data type of a single column 									- df.col.dtype
	Find the number of unique values in a column 						- df.col.unique()
	List data having null values in another attribute of theirs. 		- without using isnull()
	Counts of data samples for every unique value in a column 			- df.col.value_counts()
	Find number of data samples with a null value in an attribute 		- df.col.isnull().sum()
	Find number of samples in a DataFrame or a Series object 			- df.size() / df.col.size()

'''

import pandas as pd 
from fifa_0_splitting import split_fifa
pd.set_option('display.expand_frame_repr', False)

def main():
	#Load miniset of "more information"
	miniset = "more_info"
	df_more = split_fifa(miniset)

	#~~~~~~MORE INFO ANALYSIS ~~~~~~~

	#Find how many different values appear for preferred foot (Right/Left/Other) or (Right/Left)
	print("TYPES of preferred foots:\n", df_more['Preferred Foot'].unique())
	#Samples with preferred foot == NaN
	print("Sample of players with 'nan' as preferred foot:\n", df_more[(df_more['Preferred Foot'] != 'Right') & (df_more['Preferred Foot'] != 'Left') & (df_more.Overall > 60)].sample(5), end="\n\n")
	#List all the different positions and how many players in each position
	print("Positions with COUNTS of players in each:\n", df_more.Position.value_counts(ascending=True), end="\n\n")					#Default is ascending=False
	#List the samples containing the position which occurs the least
	print("Players playing the position which occurs least in the game: ")
	print(df_more[df_more.Position == df_more.Position.value_counts(ascending=True).keys()[0]], end="\n\n")

	#Find International Reputation stats
	print("CHANGING TYPE of International Reputation column (float64)...")
	df_more['International Reputation'] = df_more['International Reputation'].fillna(0).astype(int)
	print("New dtype of International Reputation column = ", df_more['International Reputation'].dtype)
	#Here dtype shows as float because of mean and std calculation
	print("Mean and spread of International Reputation:\n", df_more['International Reputation'].describe(), end="\n\n")
	#Players above 22 with unknown quality of weaker foot
	#isnull() returns True for null values and False otherwise; and sum adds up the True and False values treating True as 1 and False as 0
	print("Players above 22 years of age with unknown weaker foot stat = ", df_more['Weak Foot'][df_more.Age > 22].isnull().sum())

	#TEAM SPECIFIC

	#Find team-size (Size returns the number of elements!!)
	team = 'Manchester United'
	print("Size of {0} squad: ".format(team), df_more.Club[df_more.Club == team].size)
	print("Number of elements in entire team DataFrame: ", df_more[df_more.Club == team].size, end="\n\n")

def test():
	#function to do rough work.
	#Change the main() to test() in the if statement right at the bottom to run only this.
	#Used to help me sanity-check myself or test small lines of code without disrupting the main function.
	l = [0, 1, 2, 3]
	s = pd.Series(l)
	print(s.size())															#Won't work

if __name__ == "__main__":
	main()