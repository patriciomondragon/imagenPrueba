FROM python:3

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install flask_wtf

EXPOSE 3000

CMD ["python", "./app.py"]
