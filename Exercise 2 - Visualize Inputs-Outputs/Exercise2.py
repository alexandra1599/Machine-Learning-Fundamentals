import pandas as pd
import requests

# Download the CSV file from the URL
url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv"
response = requests.get(url)

# Save the file locally
with open("doggy-boot-harness.csv", "wb") as f:
    f.write(response.content)

# Load the data using pandas
dataset = pd.read_csv("doggy-boot-harness.csv")

# Print the first few rows of the dataset
print(dataset.head())

# Look at the harness sizes
print("Harness sizes")
print(dataset["harness_size"])

# Remove the 'sex' and 'age_years' columns
dataset.drop(columns=["sex", "age_years"], inplace=True)

# Print the column names
print("\nAvailable columns after deleting sex and age information:")
print(dataset.columns.values)

# Print the data at the top of the table
print("TOP OF TABLE")
print(dataset.head())

# Print the data at the bottom of the table
print("\nBOTTOM OF TABLE")
print(dataset.tail())

# Print how many rows of data we have
print(f"We have {len(dataset)} rows of data")

# Determine whether each avalanche dog's harness size is < 55
# This creates a True or False value for each row
is_small = dataset.harness_size < 55
print("\nWhether the dog's harness was smaller than size 55:")
print(is_small)

# Apply this mask to filter only smaller dogs
data_from_small_dogs = dataset[is_small]
print("\nData for dogs with harness smaller than size 55:")
print(data_from_small_dogs)

# Print the number of small dogs
print(f"\nNumber of dogs with harness size less than 55: {len(data_from_small_dogs)}")


# Make a copy of the dataset that only contains dogs with a boot size below 40
data_smaller_paws = dataset[dataset.boot_size < 40].copy()

# Print information about the filtered dataset
print(f"We now have {len(data_smaller_paws)} rows in our dataset. The last few rows are:")
print(data_smaller_paws.tail())

# Load and prepare matplotlib to use for plotting graphs
import matplotlib.pyplot as plt

# Show a graph of harness size by boot size for dogs with smaller paws
plt.scatter(data_smaller_paws["harness_size"], data_smaller_paws["boot_size"])

# Add axis labels
plt.xlabel("Harness Size (cm)")
plt.ylabel("Boot Size (cm)")

# Optionally add a title and show the plot
plt.title("Harness Size vs Boot Size for Smaller-Pawed Dogs")
plt.grid(True)
plt.show()

# Convert harness sizes from metric (cm) to imperial (inches)
data_smaller_paws['harness_size_imperial'] = data_smaller_paws.harness_size / 2.54

# Plot harness size in inches vs. boot size
import matplotlib.pyplot as plt

plt.scatter(data_smaller_paws["harness_size_imperial"], data_smaller_paws["boot_size"])

# Add axis labels and title
plt.xlabel("Harness Size (inches)")
plt.ylabel("Boot Size (cm)")
plt.title("Boot Size vs. Harness Size (Imperial Units)")

# Show grid and plot
plt.grid(True)
plt.show()
