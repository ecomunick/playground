import pandas as pd
import sys
#print(sys.version)
#print('pandas version', pd.__version__)

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', 85)

#df = pd.read_csv('/content/2015_Street_Tree_Census_Trees.csv') # in GColab
df = pd.read_csv('/Users/tapi/Documents/projects/playground/data/2015_Street_Tree_Census_-_Tree_Data.csv')
# seeing the data
df.head()

# number of rows and columns #(359431, 45)
df.shape

# checking data types and null values
df.info()
df.isnull().sum()

# looks like some amount of variable's data are missing
missing_data = []

for value, column in df.items():
  x = column.isnull().sum()
  if x > 0:
    missing_data.append((value, x))  # Append a tuple of (column_name, missing_count)

missing_data

# adding into a df
missing_df = pd.DataFrame(missing_data, columns=['Column Name', 'Missing Count']).sort_values(by='Missing Count', ascending=False)
missing_df

# what are the situation, general feeling of New York's Trees
# So that we can reject some columns that are related w/ location for now.
# let's delete some column
df.columns

df_ohne_location = df[['tree_id', 'tree_dbh', 'stump_diam', 'curb_loc', 'status', 'health', 'spc_latin',
      'steward', 'sidewalk', 'problems', 'root_stone', 'root_grate', 'root_other',
      'trunk_wire', 'trnk_light', 'trnk_other', 'brch_light', 'brch_shoe', 'brch_other']]

df_ohne_location

# figure out numerical values and if there are some null values
df_ohne_location.isnull().sum()

# show all the ones where ' health' is a non value and decide what to do next.
# for now, just exploring the data and seeing a bunch of NaN
df_ohne_location[df_ohne_location['health'].isna()]

df_ohne_location.describe()

# see the distribution
df_ohne_location.hist(bins=60, figsize=(20,10))

# tree_id should be ignored, since id the id of trees and the other one looks like to have some thing weird as maximum values

# let's see some high values for 'tree_dbh' where the dbh is higher than 50 inches
# we got 201 values
big_trees = df_ohne_location[df_ohne_location['tree_dbh'] > 50]
big_trees



# lets visualize that:
big_trees.hist(bins=60, figsize=(20,10))

big_trees[['tree_id', 'tree_dbh']].plot(kind='scatter', x='tree_id', y='tree_dbh', figsize=(20,10))

# see the distribution of differents latin names
df_ohne_location['spc_latin'].value_counts()

# to visualize, transform into a dataframe
pd.DataFrame(df_ohne_location['spc_latin'].value_counts()).plot(kind='bar', figsize=(20,10))

# lets see other variables with missing data like 'steward'
df_ohne_location['steward'].value_counts()

df_ohne_location['sidewalk'].value_counts()

df_ohne_location['status'].value_counts()

df_ohne_location['curb_loc'].value_counts()

# check if there are a mismatching between status == Stump and health; create a new subset
stumps = df_ohne_location[df_ohne_location['status'] == 'Stump']
stumps

deads = df_ohne_location[df_ohne_location['status'] == 'Dead']
deads

# lets check how the problems are distributed
df_ohne_location.columns

tree_problems = df_ohne_location[['root_stone',
       'root_grate', 'root_other', 'trunk_wire', 'trnk_light', 'trnk_other',
       'brch_light', 'brch_shoe', 'brch_other']]
tree_problems

# applying values_counts function to each of the series and then we are able to see the values to all of them
tree_problems.apply(pd.Series.value_counts)

## End exploration

