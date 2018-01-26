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