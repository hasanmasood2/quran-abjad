FROM python:3.9.6
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update && apt-get install -y curl
WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app
ENV FLASK_APP quran_app
COPY . .
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "quran_app:app", "-b", "0.0.0.0:8000"]
