FROM python:3.10.5-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=flaskr
ENV FLASK_ENV=development

COPY flaskr ./flaskr

CMD ["flask", "run", "--host=0.0.0.0"]