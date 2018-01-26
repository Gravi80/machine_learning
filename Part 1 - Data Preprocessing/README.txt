The dataset contains 4 columns and 10 rows:
Country, Age, Salary, Purchased

First three columns[Independent Variables] are the details of a customer and the fourth[Dependent Variable] column tells customer purchased the product or not.


We will use information from Independent Variables to predict Dependent Variable.

1). Read dataset using pandas
2). Create Matrix/Features from Independent variables
3). Create Dependent Variable vector from Independent variable
4). Handle the missing data. There are 2 missing data [age, salary]
	4.1). Remove the lines/rows that have missing data [Not Recommended] 
	4.2). Replace missing data with mean of the columns


Categorical Data
================
Country[contains 3 categories] and Purchased[contains 2 categories] are categorical variables.

Since ML models are based on mathematical equations so keeping text in the Categorical columns need to be encode the categorical variables into Numbers. 
	Dummy Variables
	===============
	Taking country column as example, Image : dummy_variables.png
	Instead of having 1 country column, we will have number of column equals to the number of categories. Each column will have either 1 or 0
	Image : dummy_variables2.png
	If we are in the France column, it will be 1 if the country is France and 0 if the country is not France.

