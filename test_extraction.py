import os
from PIL import Image
import pytesseract
from parser import extract_lab_tests
import re

directory = "lbmaske"
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(f"Processing: {filename}")
        image_path = os.path.join(directory, filename)
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print("OCR TEXT START")
        print(text)
        print("OCR TEXT END")
        lab_data = extract_lab_tests(text)
        print("EXTRACTED LAB DATA:")
        print(lab_data)
        print("="*40)

# Matches: Test Name (with spaces/parentheses) Value (number/word) [Unit] Reference Range (number/word or range)
pattern = re.compile(
    r'^([A-Za-z0-9()\\-/ ]+?)\\s+([\\d.,]+|[A-Za-z]+)\\s*([a-zA-Z%/.,]*)\\s+([\\d.,]+\\s*-\\s*[\\d.,]+|[A-Za-z0-9/., -]+)$'
)

IGNORE_KEYWORDS = [
    "LABORATORY", "HOSPITAL", "Test Report", "END OF REPORT", "Scan to Validate",
    "Patient", "Doctor", "Sample", "Mob", "Address", "Page", "Result Unit", "Biological Ref. Range"
]

for line in lines:
    line = line.strip()
    if not line or any(kw in line for kw in IGNORE_KEYWORDS):
        continue
    # ... rest of your logic ... 