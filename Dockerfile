FROM git@github.com:Sujith-sunny/gitpython.git:master
FROM python:3.8

RUN pip install -r requirements.txt

COPY Name.py python_repo:us-east-1/Name

CMD ["python", "Name.py"]