FROM python:latest

RUN mkdir -p proxy-app
WORKDIR /proxy-app

ENV FLASK_APP=run.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

COPY requirements.txt /proxy-app

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=8080"]
