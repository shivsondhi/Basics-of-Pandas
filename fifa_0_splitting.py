'''
Loads the fifa dataset and splits it into smaller datasets according to the data; for ease of viewing and analysis. 
Can return either a single split or all the splits when run from main()

Demonstrates:-
	Read data from a .csv file 												- pandas.read_csv(filepath)
	Drop a list of columns from the DataFrame 								- df.drop()
	Split a DataFrame into a DataFrame containing only a list of columns 	- df[list_of_cols]

Changes:
	Efficiency of space and time.
'''

import pandas as pd
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_columns', 15)															#Displays a maximum of 15 columns only, rest are ...

def main():
	#SELECT an appropriate miniset value. Default = 'all'
	miniset = 'all'
	minisets = ['basic_info', 'more_info', 'positions', 'basic_abilities', 'attack_abilities', 'def_abilities', 'adv_abilities']

	if miniset == 'all':
		for m in minisets:
			d = split_fifa(m)
	else:
		d = split_fifa(m)

def split_fifa(miniset='all', show_original=False, show_current=True):
	#Load dataset and drop unnecessary columns
	path = 'fifa19.csv'																				#Your file path
	df = pd.read_csv(path, index_col = 'ID')														#index_col is set to the ID column.
	to_drop = ['Photo', 'Flag', 'Club Logo', 'Real Face']											#drop columns with image urls etc. 
	df.drop(to_drop, axis=1, inplace=True)															#inplace ensures the calling df is modified rather than returning a df copy.

	if show_original:
		#print the original dataset
		print("Original complete dataset:\n", df.head(6), end="\n\n")
		#Find shape of the data
		print("Number of rows = ", df.shape[0], "\nNumber of columns (after dropping) = ", df.shape[1], end="\n\n")
		#Display the column names as a list
		print("List of all the columns are-\n", list(df), end="\n\n")

	#Manually grouping the minisets - create a dictionary
	minisets = {
		'basic_info' : ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Jersey Number', 'Value', 'Wage', 'Body Type', 'Joined', 'Loaned From', 'Contract Valid Until', 'Height', 'Weight', 'Release Clause'],
		'more_info' : ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Potential',  'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate', 'Position'],
		'positions' : ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'],
		'basic_abilities' : ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'ShortPassing', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Jumping', 'Stamina', 'Strength', 'Aggression'],
		'attack_abilities' : ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Crossing', 'Finishing', 'HeadingAccuracy', 'Volleys', 'ShotPower', 'LongShots'],
		'def_abilities' : ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Interceptions', 'Positioning',  'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes'],
		'adv_abilities' : ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Dribbling', 'Curve', 'Reactions', 'Balance', 'Vision', 'Penalties', 'FKAccuracy', 'Composure']
	}

	#Splitting the data into the mini-dataset
	df_mini = df[minisets[miniset]]
	if show_current:
		#print sample of current miniset
		print("Sample of the miniset, {}:\n".format(miniset), df_mini.sample(5))
		#Shape of this miniset
		print("Number of rows = ", df_mini.shape[0], "\nNumber of columns = ", df_mini.shape[1], end="\n\n")

	del df
	return df_mini

if __name__ == "__main__":
	main()