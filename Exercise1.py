import pandas as pd
import statsmodels.formula.api as smf

# If you need to download the data programmatically, use requests or urllib:
import requests

# Download the graphing helper file
graphing_url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py"
graphing_response = requests.get(graphing_url)
with open("graphing.py", "w") as file:
    file.write(graphing_response.text)

# Download the dataset
csv_url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv"
csv_response = requests.get(csv_url)
with open("doggy-boot-harness.csv", "wb") as file:
    file.write(csv_response.content)

# If you're missing a library, you should install it outside your script (e.g., in terminal):
# pip install statsmodels

# Or check for it in code and prompt the user
try:
    import statsmodels
except ImportError:
    print("Please install 'statsmodels' by running: pip install statsmodels")

# Define the data dictionary
data = {
    'boot_size': [39, 38, 37, 39, 38, 35, 37, 36, 35, 40, 
                  40, 36, 38, 39, 42, 42, 36, 36, 35, 41, 
                  42, 38, 37, 35, 40, 36, 35, 39, 41, 37, 
                  35, 41, 39, 41, 42, 42, 36, 37, 37, 39,
                  42, 35, 36, 41, 41, 41, 39, 39, 35, 39],
    
    'harness_size': [58, 58, 52, 58, 57, 52, 55, 53, 49, 54,
                     59, 56, 53, 58, 57, 58, 56, 51, 50, 59,
                     59, 59, 55, 50, 55, 52, 53, 54, 61, 56,
                     55, 60, 57, 56, 61, 58, 53, 57, 57, 55,
                     60, 51, 52, 56, 55, 57, 58, 57, 51, 59]
}

# Convert to pandas DataFrame
dataset = pd.DataFrame(data)

# Print the dataset
print(dataset)

# As you see, we now have the sizes of boots and harnesses for 50 avalanche dogs.

# want to use harness size to estimate boot size. INPUT : harness_size, OUTPUT : boot size

## SELECT THE MODEL 
#let's start with a very simple model called OLS (Ordinary Least Square). This is just a straight line (sometimes called a trendline) to minimize the sum of squared differences between observed values and predicted values.
# Define formula for linear regression: boot_size as a function of harness_size
formula = "boot_size ~ harness_size"

# Create the model object (not yet trained)
model = smf.ols(formula=formula, data=dataset)

# Check if the model has parameters before training
if not hasattr(model, 'params'):
    print("Model selected but it does not have parameters set. We need to train it!")

# Fit the model (i.e., train it)
trained_model = model.fit()

# Show the model parameters
# Print information about our model now it has been fit
print("The following model parameters have been found:\n" +
      f"Line slope: {trained_model.params['harness_size']}\n" +
      f"Line Intercept: {trained_model.params['Intercept']}")

# Print model summary
print("\nModel summary:")
print(trained_model.summary())

import matplotlib.pyplot as plt

# Scatter plot of the data points
plt.scatter(dataset["harness_size"], dataset["boot_size"], label='Data points')

# Plot the fitted regression line
slope = trained_model.params['harness_size']
intercept = trained_model.params['Intercept']
plt.plot(dataset["harness_size"], slope * dataset["harness_size"] + intercept, 'r', label='Fitted line')

# Add labels and legend
plt.xlabel("Harness Size (cm)")
plt.ylabel("Boot Size (cm)")
plt.title("Dog Boot Size vs. Harness Size")
plt.legend()
plt.grid(True)
plt.show()


# Define the harness size we want to predict for
harness_size = pd.DataFrame({ 'harness_size' : [52.5] })

# Use the trained model to make a prediction
approximate_boot_size = trained_model.predict(harness_size)

# Print the result
print("Estimated approximate boot size:")
print(approximate_boot_size.iloc[0])
