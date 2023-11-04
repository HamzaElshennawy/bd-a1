FROM ubuntu:latest


RUN apt-get update 
RUN apt-get install python3-pip -y
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir /home/doc-bd-a1/

COPY load.py /home/doc-bd-a1/load.py
COPY dpre.py /home/doc-bd-a1/dpre.py
COPY eda.py /home/doc-bd-a1/eda.py
COPY vis.py /home/doc-bd-a1/vis.py
COPY model.py /home/doc-bd-a1/model.py

COPY results.csv /home/doc-bd-a1/dataset.csv

CMD ["/home/doc-bd-a1/final.sh"]
