FROM python:3

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt 2>/dev/null

ADD . /app

EXPOSE 5000

CMD ["flask", "--app", "application.py", "run", "--host=0.0.0.0"]
