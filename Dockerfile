FROM python:3.6.2-jessie
WORKDIR /tracklift/backend
COPY . .

RUN pip install -r requirements.txt
CMD python main.py
