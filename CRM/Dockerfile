FROM python:3.10.4-slim-buster

WORKDIR /opt/oss_system

COPY . .
#COPY ../requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "CRM.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
