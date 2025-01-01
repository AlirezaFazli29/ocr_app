# OCR Web-App Project with Tesseract
This is an OCR (Optical Character Recognition) web application built with FastAPI and Tesseract. The app allows you to upload images and extract text in various languages using Tesseract OCR.

The app can be run in two ways: using Docker or without Docker.

## Table of Contents
1. Clone the App using Git
2. Installation
3. Running the App
4. Supported Languages

## Clone the App using Git
First, ensure that you have Git installed. If not, you can download and install it from the official Git website.
Then, use the following command to clone the repository:
```bash
git clone https://github.com/AlirezaFazli29/ocr_app.git
```

## Installation

### Without Docker:

You need Python 3.7 or above and pip installed.
Install the required packages from requirements.txt: 

```bash
pip install -r requirements.txt
```
For the OCR functionality, you need to install the Tesseract software along with the required language packages. Run the following commands:

```bash
# Install Tesseract OCR package
sudo apt update
sudo apt install tesseract-ocr

# Install language packages (Spanish, Farsi, Arabic, French, German)
sudo apt install tesseract-ocr-spa tesseract-ocr-fas tesseract-ocr-ara tesseract-ocr-fra tesseract-ocr-deu
```
You can verify that Tesseract is installed correctly by running:

```bash
tesseract --list-langs
```
This should show the list of available languages, including the ones you've installed.

### With Docker:

First, make sure Docker is installed on your machine. You can download it from the official Docker website.

Now you can get the image with this line:

```bash
docker pull alirezafazli29/fastapi-ocr
```

After downloading the image, you can run the app inside a Docker container. The app will be accessible on port 7000 by default:

```bash
docker run -p 8080:7000 --name my-ocr alirezafazli29/fastapi-ocr
```

This will start the FastAPI app, and you can access it by navigating to http://localhost:8080 in your browser or using any HTTP client.

Also you can use the docker-compose.yml and run the application as bellow:

```bash
docker compose up -d
```

## Running the App

### Without Docker:
After installation, you can run the app locally with the following command:
```bash
python3 ./app/main.py
```
This will start the FastAPI app on http://localhost:7000 (or another port if specified). The --reload flag will automatically reload the server when changes are made.

### With Docker:

If you're running the app with Docker, the app will be running on http://localhost:8080 (as specified in the ```docker run``` or ```docker compose``` command). You can change the ports by modifying the ```docker run``` command or the ```docker-compose.yml``` file if needed.

## Supported Languages

The application supports the following languages:

- English (`eng`)
- Spanish (`spa`)
- Arabic (`ara`)
- French (`fra`)
- German (`deu`)
- Farsi (Persian) (`fas`)

You can request OCR for any of these languages by providing the appropriate language code when making the `/ocr` request.
If you need more language support, you need to get needed tesseract language package and modify the codes.
