Random forest is a version of Ensemble learning.

Ensemble learning
=================
When you take multiple algorithms OR same algo multiple times and put them together to make something more powerful from the original.


Steps
======
1). Pick random K data points from the Training set.

2). Build a decision Tree associated to these K data points.

3). Choose number of Trees you want to build and repeat STEPS 1 & 2

4). For a new data, use all of them(Ntree) to predict value of Y.
	Y = avg. across all the predicted Y values.
	

