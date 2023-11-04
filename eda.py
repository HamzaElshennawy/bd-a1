import pandas as pd

def describe_data(dataset):
  

  print(dataset.describe())

def find_correlations(dataset):
  

  correlation_matrix = dataset.corr()
  print(correlation_matrix)

def find_outliers(dataset):
  

  for column in dataset.columns:
    outliers = dataset[column][(dataset[column] < dataset[column].quantile(0.05)) | (dataset[column] > dataset[column].quantile(0.95))]
    print(f'Outliers for column {column}: {outliers}')

if __name__ == '__main__':
  # Load the dataset
  dataset = pd.read_csv('res_dpre.csv')

  # Describe the data
  describe_data(dataset)

  # Find correlations between the features
  find_correlations(dataset)

  # Find outliers
  find_outliers(dataset)

  # Save the insights as text files
  with open('eda-in-1.txt', 'w') as f:
    f.write(describe_data(dataset))

  with open('eda-in-2.txt', 'w') as f:
    f.write(find_correlations(dataset))

  with open('eda-in-3.txt', 'w') as f:
    f.write(find_outliers(dataset))
