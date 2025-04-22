#Importing Data
import pandas as pd
import pylab as pl

widge1 = pd.read_csv("/Users/gabealvarez/Downloads/python_project_data_sp2023.csv")
#Getting Total Number of Passengers and Column Names
widge1.info()
#Getting proportions of passengers who survived and died
my_tab = pd.crosstab(index=widge1["Survived"],
                     columns="count")
print(my_tab)
widge1["Survived"].value_counts()
#relative frequency
my_tab/my_tab.sum()
#Percentages
my_tab/my_tab.sum()*100
#importing packages
import matplotlib.pyplot as plt
#create pie chart for passenger survival
Survived = ["Died", "Survived"]
Survivedfreq= [1496, 712]
Surivedcol=["Grey", "Green"]
plt.pie(Survivedfreq, colors=Surivedcol, autopct= '%1.1f%%')
plt.legend(Survived)
plt.title("Pie Chart of Passenger Survival n=2208", loc='center')
plt.show()
#Creating Bar Plot for passenger survival
print(my_tab)
Survived = ["Died", "Survived"]
Survivedfreq= [1496, 712]
plt.bar(Survived,Survivedfreq, color='orange')
plt.xlabel("Passenger Survival")
plt.ylabel("Number of Passengers")
plt.title("Bar Chart of Passenger Survival n=2208", loc='center')
plt.show()
#Creating frequency for passenger class
my_tab1 = pd.crosstab(index=widge1["Class"],
                     columns="count")
print(my_tab1)
my_tab1/my_tab1.sum()
my_tab1/my_tab1.sum()*100
#creating pie chart for passenger class
Class = ["1", "2", "3", "D", "E", "R", "V"]
Classfreq= [324, 285, 710, 66, 323, 69, 431]
Classcol = ["Pink", "Blue", "Red", "Orange", "Yellow", "Purple", "Green"]
plt.pie(Classfreq, colors=Classcol, autopct= '%1.1f%%')
plt.legend(Class)
plt.title("Pie Chart of Passenger Class n=2208", loc='center')
plt.show()
#creating bar chart for passenger class
print(my_tab1)
Class = ["1", "2", "3", "D", "E", "R", "V"]
Classfreq= [324, 285, 710, 66, 323, 69, 431]
plt.bar(Class,Classfreq, color='blue')
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Bar Chart of Passenger Class n=2208", loc='center')
plt.show()
#Interpreting class code
my_tab2 = pd.crosstab(index=widge1["Class_Dept"],
                     columns="count")
print(my_tab2)
widge1["Class_Dept"].value_counts()
#Creating frequency for men, women, and children
my_tab2 = pd.crosstab(index=widge1["MWC"],
                     columns="count")
print(my_tab2)
my_tab1/my_tab2.sum()
my_tab1/my_tab2.sum()*100
#Creating pie chart for Men, Women, Children
MWC= ["Men", "Women", "Children"]
MWCfreq = [1652,432,124]
MWCcol= ["Blue", "Pink", "Green"]
plt.pie(MWCfreq, colors=MWCcol, autopct= '%1.1f%%')
plt.legend(MWC)
plt.title("Pie Chart of Passenger Identity n=2208", loc='center')
plt.show()
#Creating Bar Chart for Men, Women, Children
print(my_tab2)
Class = ["Men", "Women", "Children"]
Classfreq= [1652,432,124]
plt.bar(Class,Classfreq, color='green')
plt.xlabel("Passenger Identity")
plt.ylabel("Number of Passengers")
plt.title("Bar Chart of Passenger Identity n=2208", loc='center')
plt.show()
#Creating Frequency of Class Departments
my_tab2 = pd.crosstab(index=widge1["Class_Dept"],
                     columns="count")
print(my_tab2)
widge1["Class_Dept"].value_counts()
#Installing packages
import statistics as stat
#Table of descriptive stats for age
stat.quantiles(widge1['Age'])

widge1['Age']. describe(percentiles = [.25,0.5,0.75])
#Histogram of passenger age
plt.hist(widge1['Age'])
plt.show()
#format histogram
plt.hist(widge1['Age'], color="red", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title('Histogram of Age of the Passengers n=2208')
plt.show()
#Boxplot of Passenger Age
print(widge1.isnull().sum())
print(widge1['Age'].describe())
widge1['Age'] = widge1['Age'].fillna(widge1['Age'].median())
plt.boxplot(widge1['Age'])
plt.ylabel("Age")
plt.title('Boxplot of Age of the Passengers n=2208')
plt.show()
#Descriptive Statistics for Ticket Prices
stat.quantiles(widge1['Paid'])

widge1['Paid']. describe(percentiles = [.25,0.5,0.75])
#Histogram for Passengers' Ticket Prices
plt.hist(widge1['Paid'])
plt.show()
#format histogram
plt.hist(widge1['Paid'], color="green", edgecolor="black")
plt.xlabel("Paid")
plt.ylabel("Number of Passengers")
plt.title('Histogram of the Passengers Ticket Prices n=2208')
plt.show()
#Boxplot of Ticket Prices
print(widge1.isnull().sum())
print(widge1['Paid'].describe())
widge1['Paid'] = widge1['Paid'].fillna(widge1['Paid'].median())
plt.boxplot(widge1['Paid'])
plt.ylabel("Paid")
plt.title('Boxplot of the Passengers Ticket Prices n=2208')
plt.show()
#Bivariate Analysis of Class and Survival
bivar_freq = pd.crosstab(widge1['Class'],
                         widge1['Survived'],
                         margins=False)
print(bivar_freq)
#importing Numpy package
import numpy as np
#Side-by-Side Bar Plot for class and survival
(widge1.groupby('Survived')['Class'].value_counts(normalize=True)
 .unstack('Class').plot.bar(stacked=True))
plt.legend(loc="upper left", ncol=2)
plt.xlabel("Survived")
plt.ylabel("Percentage")
plt.title("100% Stacked Bar Chart of Passenger Survival by Class", loc='center')
plt.show()
#Bivariate Anaylsis of MWC and survival
bivar_freq = pd.crosstab(widge1['MWC'],
                         widge1['Survived'],
                         margins=False)
print(bivar_freq)
#creating side by side barplot of MWC and survival
#Establishing Bar Values
(widge1.groupby('Survived')['MWC'].value_counts(normalize=True)
 .unstack('MWC').plot.bar(stacked=True))
plt.legend(loc="upper left", ncol=2)
plt.xlabel("Survived")
plt.ylabel("Percentage")
plt.title("100% Stacked Bar Chart of Passenger Survival by Men, Women, and Children", loc='center')
plt.show()
#Descriptive Stats for Age and Survival
widge1.groupby('Survived')['Age'].describe()

#importing package
import matplotlib.pyplot as plt
import seaborn as sns
#side by side histogram for age and survival
fig, ax = plt.subplots(figsize=(8,4))
widge1.hist(column='Age', by='Survived', grid=True, xlabelsize=None, xrot=None, ylabelsize=None,
            yrot=None, ax=ax, sharex=True, sharey=True, figsize=None, layout=None, bins=7,
            backend=None)
fig.suptitle('Side by Side Histogram of Survival by Age')
plt.xlabel('Age')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
#descriptive stats for ticket prices and survival
widge1.groupby('Survived')['Paid'].describe()
#side by side histogram for ticket price and survival
fig, ax = plt.subplots(figsize=(8,4))
widge1.hist(column='Paid', by='Survived', grid=True, xlabelsize=None, xrot=None, ylabelsize=None,
            yrot=None, ax=ax, sharex=True, sharey=True, figsize=None, layout=None, bins=7,
            backend=None)
fig.suptitle('Side by Side Histogram of Survival by Ticket Price')
plt.xlabel('Ticket Price')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
#Scatterplot of Age and Ticket Price
plt.scatter(widge1['Age'], widge1['Paid'], marker='o')
plt.ylabel('Ticket Price')
plt.xlabel("Age")
plt.title("Scatterplot of Ticket Price by Age", loc='center')
plt.show()
#more complex plot
sns.lmplot(x='Age', y='Paid', data=widge1,fit_reg=True)
plt.ylabel('Ticket Price')
plt.xlabel("Age")
plt.title("Scatterplot of Ticket Price by Age", loc='center', fontsize=14)
plt.tight_layout()
plt.show()
#calculating correlation coefficient for Age and Ticket Price
widge1['Age'].corr(widge1['Paid'])
#New Variables
widge1['Class'].value_counts()
#Writing function to apply new variable name
def Class_Name(series):
    if series == 'D':
        return 'Crew'
    elif series == 'E':
        return  'Crew'
    elif series == 'V':
        return  'Crew'
    elif series == 'R':
        return  'Crew'
    elif series == "1":
        return 'First'
    elif series == '2':
        return 'Second'
    elif series == '3':
        return 'Third'
    else:
        return series
#applying names
widge1['Class'] = widge1['Class'].apply(Class_Name)
#Strip and check recode
widge1['Class'].value_counts()
widge1.head()
widge1['Class'] = widge1['Class'].str.strip()

#Seperating age into classes
widge1['Age'].describe().round(2)
def Age_levels(series):
    if series <= 3:
     return "Baby"
    elif 4 <= series < 12:
        return "Child"
    elif 13 <= series < 17:
        return "Teenager"
    elif 18 <= series < 24:
        return "Young Adult"
    elif 25 <= series < 34:
        return "Middle Adult"
    elif 35 <= series < 54:
        return "Older Adult"
    elif 55 <= series:
        return "Senior"
widge1['Age_levels']= widge1['Age'].apply(Age_levels)
widge1['Age_levels'].value_counts()
#Getting frequency counts of survival and age class
bivar_freq = pd.crosstab(widge1['Age_levels'],
                         widge1['Survived'],
                         margins=False)
print(bivar_freq)

