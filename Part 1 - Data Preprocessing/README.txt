The dataset contains 4 columns and 10 rows:
Country, Age, Salary, Purchased

First three columns[Independent Variables] are the details of a customer and the fourth[Dependent Variable] column tells customer purchased the product or not.


We will use information from Independent Variables to predict Dependent Variable.
1). Read dataset using pandas
2). Create Matrix/Features from Independent variables
3). Create Dependent Variable vector from Independent variable


Taking care of missing data
===========================
Handle the missing data. There are 2 missing data [age, salary]
	1). Remove the lines/rows that have missing data [Not Recommended] 
	2). Replace missing data with mean of the columns


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


Splitting the dataset into Training set and Test set
=====================================================
In any ML model we should split our dataset into 2 separate sets [Training and Tests sets]
In ML, the model learns from the data to make predictions by understanding some correlations present in your dataset.
And if your ML algorithm is running too much on the dataset then its performace will be bad in dataset with slightly different correlations.

We will build our ML model on a training dataset and will test it on a new set which will be slightly different.

The performance of the ML model on Test set should not be different from performance on Training set. This would mean that the ML model understood the correlations well(didn't just mugup[Overfitting]) so that it can adapt to new sets or new situations.


Feature Scaling
================
A case of getting all your data on the same scale. The main advantage of scaling is to avoid attributes in greater numeric ranges dominating those in smaller numeric ranges.

The Age, Salary column contains numerical values and the variables are not on the same scale.
Age    => 27-50
Salary => 48000-83000
Becuase both the variables don't have same scale this will cause issues in ML model.

Lots of ML models are based on Euclidean Distance (Image: EuclideanDistance).
Age    => x-coordinate
Salary => y-coordinate

Since Salary has a much higher range the Euclidean Distance will be dominated by the salary.

Country,Age,Salary,Purchased
Spain,27,48000,Yes
France,48,79000,Yes

The Euclidean Distance b/w above observations :
Distance b/w Salary = 79000-48000 = 31000 = Sqr(31000) = 961000000
Distance b/w Age = 48-27 = 21 = Sqr(21) = 441

In ML model it will make Age to be non-existent bcz Euclidean Distance will be dominated by Salary.

Methods of Feature Scaling => Image : FeatureScalingMethods


