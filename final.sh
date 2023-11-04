#!/bin/bash

# Run the data preprocessing script
python /home/doc-bd-a1/dpre.py

# Run the exploratory data analysis script
python /home/doc-bd-a1/eda.py

# Run the visualization script
python /home/doc-bd-a1/vis.py

# Run the modeling script
python /home/doc-bd-a1/model.py

# Copy the output files to the host machine
cp /home/doc-bd-a1/res_dpre.csv /bd-a1/service-result/
cp /home/doc-bd-a1/eda-in-1.txt /bd-a1/service-result/
cp /home/doc-bd-a1/eda-in-2.txt /bd-a1/service-result/
cp /home/doc-bd-a1/vis.png /bd-a1/service-result/
cp /home/doc-bd-a1/k.txt /bd-a1/service-result/

# Close the container
exit 0