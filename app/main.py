from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io
from utils import language
import base64
import uvicorn

app = FastAPI(title="OCR service")

@app.get("/")
async def root():
    """
    Root endpoint for the OCR service.

    This function serves as a health check for the application.
    When a GET request is made to the root endpoint ("/"), 
    it returns a simple message indicating that the OCR service is running.

    Returns:
        dict: A dictionary with a message confirming that the service is running.
    """
    return {"message": "OCR Service is running!"}

@app.post("/ocr")
async def perform_ocr(
    file: UploadFile,
    language: language = Form(...)
):
    """
    Perform OCR on an uploaded image.

    This function handles the OCR process:
    - Accepts an image file and the language to be used for OCR.
    - It reads the uploaded image, performs OCR using Tesseract, 
      and returns the extracted text in the specified language.
    - If any error occurs during image processing or OCR, 
      it raises an appropriate HTTP exception with a message.

    Args:
        file (UploadFile): The image file to perform OCR on.
        language (language): The language to use for OCR.

    Returns:
        JSONResponse: A JSON response with the extracted text and OCR language.
    """
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
    except Exception:
        raise HTTPException(status_code=400, detail="Could not process the uploaded file.")
    
    try:
        extracted_text = pytesseract.image_to_string(image, lang=language.value)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during OCR: {e}")
    
    return JSONResponse(
        content={"language": language.name, "extracted_text": extracted_text}
    )

@app.post("/ocr_base64")
async def perform_ocr_base46(
    base64_string: str = Form(...), 
    language: language = Form(...)
):
    """
    Perform OCR on a base64 encoded image.

    This function handles the OCR process:
    - Accepts a base64 encoded image string and the language to be used for OCR.
    - Decodes the base64 string into image data and converts it to a PIL image.
    - It performs OCR using Tesseract and returns the extracted text in the specified language.
    - If any error occurs during decoding, image processing, or OCR, it raises an 
      appropriate HTTP exception with a message.

    Args:
        base64_string (str): The base64-encoded string representing the image.
        language (language): The language to use for OCR.

    Returns:
        JSONResponse: A JSON response with the extracted text and OCR language.
    """
    try:
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        raise HTTPException(status_code=400, detail="Could not process the base64 string.")
    
    try:
        extracted_text = pytesseract.image_to_string(image, lang=language.value)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during OCR: {e}")
    
    return JSONResponse(
        content={"language": language.name, "extracted_text": extracted_text}
    )

@app.post("/file-to-base64")
async def file_to_base64(file: UploadFile):
    """
    Convert an uploaded file to a base64-encoded string.

    This function processes an uploaded file and converts its binary content
    into a base64-encoded string. The resulting string can be used for
    serialization or transmission of the file content in text format.
    If any error occurs during file processing, it raises an appropriate 
    HTTP exception with a message.

    Args:
        file (UploadFile): The file uploaded by the client.

    Returns:
        JSONResponse: A JSON response containing the filename and the 
                      base64-encoded string of the file content.
    """
    try:
        file_data = await file.read()
        base64_string = base64.b64encode(file_data).decode('utf-8')
    except Exception:
        raise HTTPException(status_code=400, detail="Could not process the uploaded file.")

    return JSONResponse(
        content={"filename": file.filename, "base64_string": base64_string}
    )

@app.get("/languages/")
async def get_supported_languages():
    """
    Get the list of supported languages for OCR.

    This function returns the available languages that can be used for OCR.
    It extracts the available languages from the 'language' Enum or configuration
    and returns them in a dictionary format.

    Returns:
        dict: A dictionary with the supported languages and their respective codes.
    """
    return {"supported_languages": {lang.name: lang.value for lang in language}}

uvicorn.run(app, host="0.0.0.0", port=7000)