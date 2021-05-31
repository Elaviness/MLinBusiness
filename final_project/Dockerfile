FROM python:3.9

RUN mkdir -p /user/app
WORKDIR /user/app

COPY . /user/app

EXPOSE 8180

RUN pip install -r req.txt
ENTRYPOINT ["python", "app.py"]
