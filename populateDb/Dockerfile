FROM python:3.7-alpine 
RUN  pip install python-dateutil 
RUN pip install mysql-connector-python

COPY populateDB.py ./populateDB.py
COPY results.csv ./results.csv

WORKDIR .
ADD . .

CMD ["python","/populateDB.py", "results.csv"]


