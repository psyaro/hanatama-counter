FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update -y
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir app
COPY ./ /app
WORKDIR /app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "-t", "300"]
# "--config", "/var/www/gunicorn.py" 