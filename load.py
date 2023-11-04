import pandas as pd

def load_dataset(file_path):
  

  return pd.read_csv(file_path)

if __name__ == '__main__':
  file_path = input('Enter the path to the dataset file: ')
  dataset = load_dataset(file_path)

  print(dataset.head())
