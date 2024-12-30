FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-spa \
    tesseract-ocr-fas \
    tesseract-ocr-ara \
    tesseract-ocr-fra \
    tesseract-ocr-deu \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY /app /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
RUN rm -fr requirements.txt

EXPOSE 7000

CMD [ "python3", "main.py" ]