FROM alpine:3.15
RUN apk add python3 py-pip && \
python3 -m ensurepip && \
pip install --upgrade pip && \
pip install flask pytz

ENV FLASK_APP app.py
ENV PLATFORM 'Amazon ECS'

WORKDIR /app
COPY . /app/

CMD ["python3", "app.py"]
