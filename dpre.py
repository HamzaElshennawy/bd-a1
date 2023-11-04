import pandas as pd

def clean_data(dataset):
  

  dataset.dropna(inplace=True)
  dataset.drop_duplicates(inplace=True)

  return dataset

def transform_data(dataset):
 

  for column in dataset.columns:
    if dataset[column].dtype == 'object':
      dataset[column] = pd.get_dummies(dataset[column])

  return dataset

def reduce_data(dataset):
  

  features = ['feature1', 'feature2', 'feature3']
  dataset = dataset[features]

  return dataset

def discretize_data(dataset):
  
  for column in dataset.columns:
    if dataset[column].dtype != 'object':
      dataset[column] = pd.qcut(dataset[column], 4)

  return dataset

if __name__ == '__main__':
  # Load the dataset
  dataset = pd.read_csv('results.csv')

  # Clean the data
  dataset = clean_data(dataset)

  # Transform the data
  dataset = transform_data(dataset)

  # Reduce the data
  dataset = reduce_data(dataset)

  # Discretize the data
  dataset = discretize_data(dataset)

  # Save the resulting data frame as a new CSV file
  dataset.to_csv('res_dpre.csv', index=False)
