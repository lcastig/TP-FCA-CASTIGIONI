FROM python:3
RUN  pip install python-dateutil 
RUN pip install mysql-connector-python
#RUN pip install wheel
#RUN pip install numpy
RUN pip install pandas

COPY statsDB.py ./statsDB.py

WORKDIR .
ADD . .

CMD ["python","/statsDB.py"]


