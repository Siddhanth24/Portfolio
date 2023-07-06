import pandas as pd
# Importing the CSV file
raw_csv_data = pd.read_csv("C:\\Users\\Siddhanth\\OneDrive\\Desktop\\project\\Absenteeism-data.csv")

print(type(raw_csv_data))
print(raw_csv_data)

# Making a copy of the dataframe
df = raw_csv_data.copy()

# Removing the column named 'ID' from the DataFrame df.
df = df.drop(['ID'], axis = 1)

# These statements are involved in the process of transforming the 'Reason for Absence' column into a set of dummy variables, which can be used in further analysis or modeling tasks.

reason_columns = pd.get_dummies(df['Reason for Absence'])
reason_columns['check'] = reason_columns.sum(axis=1)
reason_columns = reason_columns.drop(['check'], axis = 1)
reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first = True)

# These operations extract the maximum values from specific ranges of columns in reason_columns and assign them to separate  variables.
df = df.drop(['Reason for Absence'], axis = 1)

reason_type_1 = reason_columns.loc[:, 1:14].max(axis=1)
reason_type_2 = reason_columns.loc[:, 15:17].max(axis=1)
reason_type_3 = reason_columns.loc[:, 18:21].max(axis=1)
reason_type_4 = reason_columns.loc[:, 22:].max(axis=1)

# Concatenate Column Values

column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']

df.columns = column_names 

# Reorder Columns

column_names_reordered = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 
                          'Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']

df = df[column_names_reordered]

# Creating a Checkpoint 

df_reason_mod = df.copy()

df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format = '%d/%m/%Y')

# Extracting the Month Value 

list_months = []

for i in range(df_reason_mod.shape[0]):
    list_months.append(df_reason_mod['Date'][i].month)
    

print(len(list_months))

df_reason_mod['Month Value'] = list_months

print(df_reason_mod['Date'][699].weekday())

def date_to_weekday(date_value):
    return date_value.weekday()

df_reason_mod['Day of the Week'] = df_reason_mod['Date'].apply(date_to_weekday)

df_reason_mod = df_reason_mod.drop(['Date'], axis = 1)
print(df_reason_mod.head())

column_names_upd = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Month Value', 'Day of the Week',
       'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education', 'Children',
       'Pets', 'Absenteeism Time in Hours']
df_reason_mod = df_reason_mod[column_names_upd]

# Creating a Checkpoint 

df_reason_date_mod = df_reason_mod.copy()

# The following statement is replacing specific values in the 'Education' column with new values based on the provided mapping.

df_reason_date_mod['Education'] = df_reason_date_mod['Education'].map({1:0, 2:1, 3:1, 4:1})

# Final Checkpoint 

df_cleaned = df_reason_date_mod.copy()
print(df_cleaned.head(10))