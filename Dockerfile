FROM python:3.8

RUN pip install -r requirements.txt

COPY Name.py python_repo:us-east-1/name

CMD ["python", "Name.py"]