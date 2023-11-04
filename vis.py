import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
  # Load the dataset
  dataset = pd.read_csv('res_dpre.csv')

  # TODO: Create a visualization of the data

  # Save the visualization as a PNG file
  plt.savefig('vis.png')
