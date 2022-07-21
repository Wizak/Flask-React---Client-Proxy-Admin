# FROM python:latest

# RUN mkdir -p /client-app
# WORKDIR /client-app

# ENV FLASK_APP=run.py
# ENV FLASK_ENV=development

# COPY requirements.txt /client-app

# RUN pip install -r requirements.txt

# EXPOSE 5001

# ENTRYPOINT [ "flask" ]
# CMD ["run", "--host=0.0.0.0", "--port=5001"]


FROM python:latest

RUN mkdir -p /client-app
WORKDIR /client-app

ENV FLASK_APP=run.py
ENV FLASK_ENV=development

COPY requirements.txt /client-app

RUN pip install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5001"]