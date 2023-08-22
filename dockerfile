FROM git@github.com:Sujith-sunny/GitPython.git:master

RUN pip install -r requirements.txt

COPY Name.py python_repo:us-east-1/Name

CMD ["python", "Name.py"]