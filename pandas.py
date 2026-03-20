import pandas as pd
df=pd.DataFrame([11,22,33],columns=['Col_Name'])
print(df)

#using dictionary of lists
data={
      'Name':['Madhav','Vishakha','Lalita','Rishabh'],
      'Age':[16,17,18,19],
      'Salary':[9000,7000,5000,3000]
}

df=pd.DataFrame(data)
print(df)

#basic dataframe understanding
df.head(2)#top rows
df.tails(2)#last rows
df.shape #returns a tuple containing the shape of the dataframe
df.columns #list of column in a dataframe 
df.Index(['Name','Age','Salary'],dtype='object')
df.rename(columns={'Salary':'Monthly_Salary'},inplace=True) #rename column name
df.info()

#save and load data from csv
df.to_csv('test_data.csv',index=False)#save file -export data frame
load_df=pd.read_csv('test_data.csv')#load file-import dataframe


#rows and columns selection  
df[['Name','Monthly_Salary']]
df.loc[df.Name=='Mahadev']
df.loc[df.Name=='Mahadev']&df.loc[df.Monthly_Salary>=50000]
df.loc[0:2]

#filter dataframe

df_age_filter=df[df['Age']>=18]
df[df['Age']>=18 & (df['Monthy_Salary']>=5000)]
df.where(df['Age']>=18,other='Not Eligible') 

#Rows and Columns - Operation(Add,update,delete)

df['Team']=['CEO','HR','CTO','DA']#add new columns
df['Bonus']=df['Monthly_Salary']*0.20 #Add new columns using existing column
df.loc[len(df)]=['ABC',21,21000,'IT',2000]#Add new row - at end of dataframe
df.loc[0,'Monthly_Salary']=95000# update value in dataframe using column-value
df.loc[df.Name=='Madhav','Monthly_Salary']=90000# update value in dataframe using column-value

#delete value-row and columns
df=df.drop(df[df.Name=='ABC'].index)#delete row,axis=0
df.drop(1,axis=0)
df.drop('Bonus',axis=1,inplace=True)# delete one column

df.rename(columns={'Monthly_Salary':'Salary'},inplace=True)
df.sort_values('Salary')
df.sort_values('Salary',ascending=False)


#Working with DATE value
df['DOJ']=['2024-01-01','2024-01-15','2024-03-38','2024-03-03']
df['DOJ'].dtype#object type value
df.dtype('O')
df['DOJ']=pd.to_datetime(df['DOJ'])# change to date-time type
df['DOJ'].dtype #day-time type

# handling missing values

df.isnull()#Detect missing values
df.isnull().sum()#cuont all null values 
df.fillna(0)#fill values with 0

#aggregation and group by
df['Months'].value_count()#count of frequency
df.grouppby('month')['Salary']
