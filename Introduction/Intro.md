# INTRODUCTION TO MACHINE LEARNING

Main Focus of ML : 
- making decisions/predictions based on data
- fit models as a means to the end of making good decisions/predictions

Humans still have to **frame** the problem :
- Acquire and organize data --> **not always easy**
- Design the space of possible solutions
- Select the Learning Algorithm (LA) and parameters
- Apply it to the data
- Validate

***Why does previoulsy seen data help us predict the future?***
Assumptions : all training data are IID (independent and identically distributed) and queries are drawn from the same distribution as training data

We want the ML model to **learn implicit patterns** in the data to predict new data labels.
For this we need to solve two problems :

***1) Estimation :***
We usualy hav noisy data reflecting some underlying quantity of interest. When making estimates we need to take into account :
- How to deal with the fact that the same treatment may give different results on different trials ?
- How to predict how well an estimate may compare to future results ?

***2) Generalization :***
Predict results of a situation/experiment never encountered before in the dataset.

## Problem Characterization 

**1) Problem Class :**
What is the nature of the training data ? What quieries wil be made at testing ?

**2) Assumptions :**
What do we knnow about the source of the data, form of solutions?

**3) Evaluation Criteria :**
What is the goal of the prediction/estimation ? How to evaluate them ? How to measure overall performance of the system ?

**4) Model Type :** 
Will an intermediate model be made ? What aspects of the data will be modeled ? How will the model be used to make predictions ?

**5) Model Class :**
What is the model ? What are the parameters ? Criterion to pick the best model ?

**6) Algorithm :**
Computational process to fit model to data and/or make predictions ?

## Machine Learning (ML)

ML is a subset of Artificial Intelligence (AI) concerned with using specialized algorithms to uncover meaningful information and find hidden patterns from perceived data to corroborate the rational decision making process.
The model is the core component of ML and can be built in many ways. Rather than being edited by people so they work well, ML models are **shaped by data**.


