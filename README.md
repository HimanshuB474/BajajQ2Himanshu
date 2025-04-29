# Lab Extractor

This project extracts lab test names, values, and reference ranges from lab report images using OCR and exposes a FastAPI service for structured extraction.

## Features
- Extracts lab test data from images (PNG/JPG)
- Calculates if test values are out of reference range
- Exposes a POST API `/get-lab-tests` for image upload and extraction
- Includes a batch script for testing extraction on a directory of images

## Setup
1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install Tesseract OCR engine on your system and ensure it's in your PATH.

## Running the FastAPI Service
```bash
uvicorn main:app --reload
```
- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to use the Swagger UI and test the `/get-lab-tests` endpoint.

## Batch Testing on a Directory
To test extraction on all images in the `lbmaske` directory:
```bash
python test_extraction.py
```

## File Structure
- `main.py` - FastAPI app
- `parser.py` - Extraction logic
- `utils.py` - Out-of-range logic
- `test_extraction.py` - Batch test script
- `lbmaske/` - Directory containing your dataset images

## Notes
- Only standard OCR and regex logic are used (no LLMs).
- For PDF support, see the instructions in the code comments.

## Requirements
- Python 3.7+
- Tesseract OCR (system dependency) 