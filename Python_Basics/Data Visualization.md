# Prepare and Visualize Data using Scikit-Learn

Now is the time to start asking questions about your data. As you work with data and apply ML solutions,
it's very important to understand how to ask the right question to properly unlock the potentials of your dataset.
One key step is asking the right question that will will determine what type of ML algorithms you will leverage. 
And the quality of the answer you get back will be heavily dependent on the nature of your data.

It is not very common to be gifted a dataset that is completely ready to use to create a ML model out of the box. You usually need to play around
with the dataset, extract good features and arrange it in a way that will facilitate the ML decoding. 

Even if your model can answer your question about the data, one of the most important thing to do is plotting the results. If you cannot convey
your point using plots, then it is meaningless. Part of the data scientist's role is to demonstrate the quality and nature of the data they 
are working with. To do this, they often create interesting visualizations, or plots, graphs, and charts, showing different aspects of data.
In this way, they are able to visually show relationships and gaps that are otherwise hard to uncover. Visualizations can also help determine 
the machine learning technique most appropriate for the data. A scatterplot that seems to follow a line, for example, indicates that the data 
is a good candidate for a linear regression exercise.

One of the most used visualization libraries is [Matplotlib](https://matplotlib.org/). plot(), scatter() and bar() are the most famous functions 
in this library to plot the data. But there are many more and the one you want to use depends on your data type and what you want to show.

You can also use [panda frames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html) API which uses Matplotlib in the background.
the function is pandas.DataFrame.plot and takes as inputs : 
- dataSeries or DataFrame : The object for which the method is called.
- xlabel or position, default None. Only used if data is a DataFrame.
- ylabel, position or list of label, positions, default None. Allows plotting of one column versus another. Only used if data is a DataFrame.
- kindstr: The kind of plot to produce:

      - ‘line’ : line plot (default)
      - ‘bar’ : vertical bar plot
      - ‘barh’ : horizontal bar plot
      - ‘hist’ : histogram
      - ‘box’ : boxplot
      - ‘kde’ : Kernel Density Estimation plot
      - ‘density’ : same as ‘kde’
      - ‘area’ : area plot
      - ‘pie’ : pie plot
      - ‘scatter’ : scatter plot (DataFrame only)
      - ‘hexbin’ : hexbin plot (DataFrame only)

So you see there are many kinds of plots you can have. But not all of them are suitable for your data !! 

# Build your ML model : REGRESSION : 

While visualization allows you to make sense of data, the real power of Machine Learning comes from training models.
Models are trained on historic data to automatically capture data dependencies, and they allow you to predict outcomes for new data,
which the model has not seem before.

We have multiple types of regression models. Two of them are : Linear regression and Polynomial regression.
**Linear Regression** establishes establishes a linear relationship between x and y (Ex: y = bx+m), where the goal is to optimize the slope (b)
to minimize the cost.
The goal of a linear regression exercise is to be able to plot a line to:
- Show variable relationships.
- Make accurate predictions on where a new datapoint would fall in relationship to that line.
It is typical of **Least-Squares Regression** to draw this type of line. The term 'least-squares' means that all the datapoints
surrounding the regression line are squared and then added up. Ideally, that final sum is as small as possible, because we want a low
number of errors, or least-squares.
We do so since we want to model a line that has the least cumulative distance from all of our data points.
We also square the terms before adding them since we are concerned with its magnitude rather than its direction.

This line, called the line of best fit can be expressed by y = bx+m. X is the 'explanatory variable'. Y is the 'dependent variable'.
The slope of the line is b and m is the y-intercept, which refers to the value of Y when X = 0.

[!Linear Regression](images/LR.png)

**Polynomial Regression** is a type of linear regression where y is now modeled as a $n^{th}$ degree polynomial of x. 
Example :
$y = m + b_1x + b_2x^2 + ... + b_nx^n$, where the goal is to optimize the coefficients b_1, .. b_n to reduce loss. 
