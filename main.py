from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
from parser import extract_lab_tests

app = FastAPI()

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        text = pytesseract.image_to_string(image)
        print("OCR TEXT START")
        print(text)
        print("OCR TEXT END")
        lab_data = extract_lab_tests(text)

        return JSONResponse({
            "is_success": True,
            "data": lab_data
        })

    except Exception as e:
        return JSONResponse({
            "is_success": False,
            "error": str(e),
            "data": []
        })
