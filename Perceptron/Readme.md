# PERCEPTRON ALGORITHM

## 1. Basics 

Inputs : Training Dataset (D), Hyperparameter (k)
Outputs : Hypothesis, linear classifier ($\theta$, $\theta_0$)

**NOTE :** Initialize $\theta$ to 0 vector of size **d** (size of the input space) and not size of the data !

***Dummy Code***
```
theta = zeros(d,1); theta_0 = 0

for t = 1 to T :

  for i = 1 to n (where n is the number of examples in the training set)
  
    if y[i] x (transpose(theta) x x[i] + theta_0) <= 0 (where y[i] is the correct output and transpose(theta) x x[i] + theta_0 is the prediction)
    
        theta = theta + y[i]x[i]
        theta_0 = theta_0 + y[i]
return theta, theta_0
```
On each step, if the current hypothesis defined by $\theta$, $\theta_0$ classifies example x[i] correctly, no change is made, since the if condition will always be false
If it classifies x[i] incorrectly, it moves $\theta$ and $\theta_0$ closer to classifying x[i],y[i] correctly.

Once it does not enter the if statement, the classifier is fixed and is the good one.

## 2. Validate and check performance of algorithm 

If we use E_n($\theta$, $\theta_0$), it is going to be **too low** as an estimate of actual performance on new data since it is the training set error --> **NOT GOOD ESTIMATE**

What we need to do is save out some validation data from the training data and run the algorithm on this set to see if it works well by getting E_v

## 3. Linear Separability Through Origin

This is a property of a **Dataset** D. D is linearly separable if there is some theta such that :

        y[i](transpose(theta) x x[i]) > 0, for all i    (1)
        y[i](transpose(theta) x x[i] + theta_0) > 0, for all i (2)

(1) works for linear separability of linear classifiers through the origin where we only need $\theta$

(2) works for linear separability of general linear classifiers where we have $\theta$ and $\theta_0$ 

In this case, all predictions on training data is correct --> E_n = 0

## 4. Margin
### A. Margin of a labeled data point 

Margin of a labeled data point (x,y) with respect to a hyperplane/separator is given by :

**1) Separator through the origin : $\theta$**

$$
M = y.\frac{\theta^T x}{||\theta||}
$$

Where M is the margin, y is the target label and $\frac{\theta^T x}{||\theta||}$ is the signed distance

**2) General Separator : $\theta$, $\theta_0$**

$$
M = y.\frac{\theta^T x + \theta_0}{||\theta||}
$$

In both cases, M > 0 only if x is classified as y.

### B. Margin of a Dataset

Margin of a dataset D with respect to a hyperplane is given by :

**1) Separator through origin : $\theta$**

$$
M = \min_i y_i.\frac{\theta^T x_i}{||\theta||}
$$

**2) General Separator : $\theta$, $\theta_0$**

$$
M = \min_i y_i.\frac{\theta^T x_i + \theta_0}{||\theta||}
$$

In both cases, M > 0 only if all points in the dataset D are classified correctly


## 5. Perceptron Convergence Theroem 

Let $\gamma$ > 0 

**IF** 

  a) There exist some $\theta^*$ such that, for all i :
  
$$
y_i.\frac{\theta^{\ast T} x_i}{||\theta^{\ast} ||} 
$$

In other words, the margin of D with respect to $\theta^{\ast}$ is $M \geq \gamma$

  b) $||x_i|| \leq R$ where R is a constant

  **THEN** the perceptron will make at most $(\frac{R}{\gamma})^2$ mistakes. By mistakes, we mean make an update, so enter the if loop of the code above.

  **NOTE :** $\theta$ and $-\theta$ represent the same hyperplane but not the same classifier !

  **NOTE :** To transform **ANY** dataset that is only linearly separable **WITH** an offset to a dataset that is linearly separable **WITHOUT** an offset, add an extra dimension to all 
  datapoints using the same non-zero number for each point

## 6. Averaged Perceptron

Regular perceptron can be sensitive to the most recent examples that it sees. Averaged perceptron has more stable output : average value of $\theta$ , $\theta_0$ across all iterations.
