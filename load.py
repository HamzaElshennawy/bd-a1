import pandas as pd

def load_dataset(file_path):
  """Loads a dataset file into a Pandas DataFrame.

  Args:
    file_path: The path to the dataset file.

  Returns:
    A Pandas DataFrame containing the dataset.
  """

  return pd.read_csv(file_path)

if __name__ == '__main__':
  file_path = input('Enter the path to the dataset file: ')
  dataset = load_dataset(file_path)

  print(dataset.head())
