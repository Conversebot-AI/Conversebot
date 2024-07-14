FROM python:3.10.8

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "Conversebot-backend/manage.py", "runserver"]