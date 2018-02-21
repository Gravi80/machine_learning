Image : dataset_scatter.png

Scatterplot representing our dataset:
	We have got 2 Independent variable[X1, X2] and are predicting a 3rd dependent variable[y].


After running the decision tree algorithm. The scatter plot will split up into segments.
	Image : scatter_split.png

How and where these splits are conducted is determined by the algorithm which involves looking at the information entropy.


Information entropy : 
=====================
When we perform a split[leaves], is the split increasing amout of information that we have about our points. Is it adding any value in the way we want to group our point.
Algorithm stops when some minimum/No information needs to be added.

Final leaves are called Terminal leaves.

Image : scatter_split.png
We are drawing the decision tree of our split.
1). Split1 at X1 = 20
2). Split2 at X2 = 170 and X1 > 20
3). Split3 at X2 = 200 and X1 < 20
4). Split4 at X1 = 40 and X2 < 170

Image : decision_tree.png

How we are going to predict the value of Y for a new obsetvation(X1=30, X2=50).

It falls in the bucket/region/terminal_leaf between 20<X1<40 and X2<170
Image : observation_point.png

For predicting the value of Y, we take the averages of all terminal leaves for Y.

Ex- Average for Y for each terminal leaf :

Image : leaf_average.png
So, for point (X1=30, X2=50) the algorithm will predicted value of Y = -64.1
Image : decision_tree_leaf_value.png








Entropy, so far, had been a concept in physics. 
Namely, it is the (log of the) number of microstates or microscopic configurations.
i.e if the particles inside a system have many possible positions to move around, then the system has high entropy, and if they have to stay rigid, then the system has low entropy.

For example, water in its three states, solid, liquid, and gas, has different entropies.
Image : EntropyPhysics.png

But In 1948 paper "A Mathematical Theory of Communication", Claude Shannon introduced the revolutionary notion of Information Entropy.

	Entropy and Knowledge
	=====================
	 Let’s say we have 3 buckets with 4 balls each. The balls have the following colors:
	 
	 Bucket 1: 4 red balls
	 Bucket 2: 3 red balls, and 1 green ball
	 Bucket 3: 2 red balls, and 2 green balls

	 Image: buckets.png

How much information we have on the color of a ball drawn at random. In this case, we have the following:	 

1). In the first bucket, we’ll know for sure that the ball coming out is red.
2). In the second bucket, we know with 75% certainty that the ball is red, and with 25% certainty that it’s green.
3). In the third bucket, we know with 50% certainty that the ball is red, and with the same certainty that it’s green.

So it makes sense to say that Bucket 1 gives us the most amount of “knowledge” about what ball we’ll draw (because we know for sure it’s red), that Bucket 2 gives us some knowledge, and that Bucket 3 will give us the least amount of knowledge.


Entropy is in some way, the opposite of knowledge. So we’ll say that Bucket 1 has the least amount 
==================================================
of entropy, Bucket 2 has medium entropy, and Bucket 3 has the greatest amount of entropy.

Bucket 1 is producing less information bcz there is less uncertainity/surprise about the ball drawn.
Claude Shannon calls this measure of uncertaininty as entropy and is represented by H and has a unit BIT.


	Entropy and Probability
	=======================
	In entropy we will give :
	1). A low number for a bucket with 4 red balls, 
	2). A high number for a bucket with 2 red and 2 green balls, and 
	3). A medium number for a bucket with 3 red and 1 green ball

We know from physics that If molecules have many possible rearrangements, then the system has high entropy, and if they have very few rearrangements, then the system has low entropy.

	So a first attempt would be to count the number of rearrangements of these balls. In this case, 
	1). we have 1 possible rearrangement for Bucket 1, 
	2). 4 for Bucket 2, and 
	3). 6 for Bucket 3

	Image : balls_arrangement.png

	This gives us an idea, that if there are many arrangements, then entropy is large, and if there are very few arrangements, then entropy is low. 


