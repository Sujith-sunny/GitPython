FROM python:3.8

# RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

# COPY Name.py python_repo:us-east-1/name
COPY Name.py python_repo:us-east-1/latest

CMD ["python", "Name.py"]