# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Step 2: Explore the Dataset

# Display the first few rows of the dataset
print(iris.head())

# Generate summary statistics
print(iris.describe())

# Check for missing values
print(iris.isnull().sum())

# Step 3: Visualize the Dataset

# Plot histograms for each feature
iris.hist(figsize=(10, 8))
plt.suptitle('Histograms of Iris Features')
plt.show()

# Create a pairplot to visualize relationships between features
sns.pairplot(iris, hue='species')
plt.suptitle('Pairplot of Iris Features')
plt.show()

# Plot a bar chart for the class distribution
sns.countplot(x='species', data=iris)
plt.title('Class Distribution of Iris Dataset')
plt.show()
