import pandas as pd
import statsmodels.formula.api as smf
import joblib

# Make sure to manually download the dataset or use it from a local path
# Download link: https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv
data = pd.read_csv("doggy-boot-harness.csv")

# Preview data
print(data.head())

# Train a linear regression model
model = smf.ols(formula="boot_size ~ harness_size", data=data).fit()

print("Model trained!")

# Save model to file
model_filename = "./avalanche_dog_boot_model.pkl"
joblib.dump(model, model_filename)
print("Model saved!")

# Load model from file (as an example)
model_loaded = joblib.load(model_filename)

# Function to load the model and predict boot size
def load_model_and_predict(harness_size):
    '''
    This function loads a pretrained model. It uses the model
    with the customer's dog's harness size to predict the size of
    boots that will fit that dog.
    '''
    loaded_model = joblib.load(model_filename)
    print("We've loaded a model with the following parameters:")
    print(loaded_model.params)

    inputs = {"harness_size": [harness_size]}
    predicted_boot_size = loaded_model.predict(inputs)[0]
    return predicted_boot_size

# Test the prediction function
predicted_boot_size = load_model_and_predict(45)
print("Predicted dog boot size:", predicted_boot_size)

# Function to check if selected boot size is appropriate
def check_size_of_boots(selected_harness_size, selected_boot_size):
    '''
    Calculates whether the customer has chosen a pair of doggy boots that 
    are a sensible size. It compares the selected size to a prediction.
    '''
    estimated_boot_size = load_model_and_predict(selected_harness_size)
    estimated_boot_size = int(round(estimated_boot_size))

    if selected_boot_size == estimated_boot_size:
        return "Great choice! We think these boots will fit your avalanche dog well."

    if selected_boot_size < estimated_boot_size:
        return "The boots you have selected might be TOO SMALL for a dog as "\
               f"big as yours. We recommend a doggy boots size of {estimated_boot_size}."

    if selected_boot_size > estimated_boot_size:
        return "The boots you have selected might be TOO BIG for a dog as "\
               f"small as yours. We recommend a doggy boots size of {estimated_boot_size}."

# Test the sizing advisory function
advice = check_size_of_boots(selected_harness_size=55, selected_boot_size=39)
print(advice)

# Show final model parameters
print("We have loaded a model with the following parameters:")
print(model_loaded.params)
