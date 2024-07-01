FROM python:3.12-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

# f95b0595339b72b21aef558a019f2422ebf1364a64ed71fac5e8ff4f191feafb