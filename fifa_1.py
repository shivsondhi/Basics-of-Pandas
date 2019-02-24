'''
Basic information file.

Demonstrates:-
	List data types of all columns								- df.dtypes
	Change data type of a column 								- df.col.astype()
	Fill desired values in place of default null values 		- df.col.fillna()
	Map a function to a DataFrame 								- df.apply(fn)
	Map a function to a Series 									- s.map(fn)
	Rename a column 											- df.col.rename()
	Select certain data from a DataFrame based on conditions 	- df[*conditional*]		"|","&" used in conditionals as opposed to "or","and"
	Sorting values in a column 									- df.sort_values()
	Grouping the data by certain attributes 					- df.groupby()
	How to print the groups after the groupby.
	The apparent immutability of Series and DataFrames 			- Solved by assigning a modified df to itself or by using the inplace argument wherever applicable.

Changes
	Try doing the same for "Value" that is done for "Wages"
'''

import pandas as pd
from fifa_0_splitting import split_fifa
pd.set_option('display.expand_frame_repr', False)
pd.set_option('chained', None)																		#For SettingWithCopyWarning while replacing rows/columns in current dataframe


def val_to_int(money_str):
	if money_str != "Nil":
		if money_str[-1] == "M":
			return float(money_str[1:-1]) * 1000
		elif money_str[-1] == "K":
			return float(money_str[1:-1])
	return


def main():
	#Choose from: basic_info | more_info | positions | basic_abilities | attack_abilities | def_abilities | adv_abilities
	miniset = "basic_info"
	#Load the basic info miniset
	df_basic = split_fifa(miniset)																	#Make second argument False to not display the original dataset

	#~~~~~~~BASIC INFO ANALYSIS~~~~~~~~~
	
	# 1. Make changes 
	#Check dtypes of all attributes
	print(df_basic.dtypes, end="\n\n")
	#Change 'Jersey Number' from float to int
	df_basic['Jersey Number'] = df_basic['Jersey Number'].fillna(0).astype(int)						#Must use = to assign the series to itself! Generates warning (false positive) 
	#convert 'Wage' to int() datatype
	df_basic.Wage = df_basic.Wage.apply(val_to_int)													#Applies the function to every sample of the df
	#Rename the column to indicate they're multiples of 1000 Pounds
	df_basic.rename(columns={'Wage':'Wage(KP)'}, inplace = True)
	#Check dtypes again to reflect changes
	print("Changed types:\nJersey Number \t\t\t", df_basic['Jersey Number'].dtype, "\nWage(KP)  \t\t\t\t", df_basic['Wage(KP)'].dtype, end="\n\n")

	# 2. Basic Analysis
	#Find max player of any attribute
	print("MAX OVR in game = ", df_basic.Overall.max(), "\n", df_basic[df_basic.Overall == df_basic.Overall.max()], end="\n\n")
	#Describe an attribute
	print("Analysis of the AGE of all players:\n", df_basic.Age.describe(), end="\n\n")
	
	# 3. TEAM SPECIFIC
	#select team and extract samples of desired team
	team = 'Arsenal'
	df_team = df_basic[df_basic.Club == team]														#Conditional operations on DataFrame
	print("Players of {0}:\n".format(team), df_team.sample(4), end="\n\n")

	# 3.a. Team analysis
	#Tallest Player
	print("TALLEST PLAYER of the Team:\n", df_team[df_team.Height == df_team.Height.max()].Name, end="\n\n")
	#Sort by Age
	print("Team Players Sorted by their WAGES:\n", df_team.sort_values(by='Wage(KP)', ascending=True), end="\n\n")
	#MultiIndex with Body Type  -->  It's a pain to print groupby objects!
	d = df_team.groupby('Body Type')
	print("Grouping by BODY TYPE.\n")
	for key, item in d:
	    print("BODY TYPE: {0}".format(key), d.get_group(key), "\n\n")


if __name__ == "__main__":
	main()