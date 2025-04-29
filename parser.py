import re
from utils import is_out_of_range

IGNORE_KEYWORDS = [
    "LABORATORY", "HOSPITAL", "Test Report", "END OF REPORT", "Scan to Validate",
    "Patient", "Doctor", "Sample", "Mob", "Address", "Page", "Result Unit", "Biological Ref. Range"
]

def extract_lab_tests(text):
    lines = text.splitlines()
    data = []

    # Regex to match lines like: Test Name  Value  [Unit]  Reference Range
    pattern = re.compile(
        r'^([A-Za-z0-9()\-/ ]+?)\s+([\d.,]+|[A-Za-z]+)\s*([a-zA-Z%/.,]*)\s+([\d.,]+\s*-\s*[\d.,]+|[A-Za-z0-9/., -]+)$'
    )

    for line in lines:
        line = line.strip()
        if not line or any(kw in line for kw in IGNORE_KEYWORDS):
            continue

        match = pattern.match(line)
        if match:
            test_name = match.group(1).strip()
            test_value = match.group(2).strip()
            test_unit = match.group(3).strip()
            reference = match.group(4).strip()
            out_of_range = is_out_of_range(test_value, reference)
            data.append({
                "test_name": test_name,
                "test_value": test_value,
                "bio_reference_range": reference,
                "test_unit": test_unit,
                "lab_test_out_of_range": out_of_range
            })

    return data
