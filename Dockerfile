FROM python:3.8

RUN pip install -r C:\Users\drrat\Desktop\Sunny\GitPython\requirements.txt
COPY Name.py python_repo:us-east-1/Name

CMD ["python", "Name.py"]