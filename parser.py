import re
from utils import is_out_of_range

IGNORE_KEYWORDS = [
    "LABORATORY", "HOSPITAL", "Test Report", "END OF REPORT", "Scan to Validate",
    "Patient", "Doctor", "Sample", "Mob", "Address", "Page", "Result Unit", "Biological Ref. Range",
    "Investigation", "Result", "Units", "Biological Reference Interval", "Reference", "Method"
]
CATEGORICAL_VALUES = {"POSITIVE", "NEGATIVE", "DETECTED", "NOT DETECTED", "NIL", "TRACE"}

main_pattern = re.compile(
    r'^([A-Za-z0-9()\-/ .]+?)\s+([\d.,]+|[A-Za-z]+)\s*([a-zA-Z%/.,]*)\s+([\d.,]+\s*-\s*[\d.,]+[ a-zA-Z%/.,]*)$'
)

def extract_lab_tests(text):
    lines = text.splitlines()
    data = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or any(kw in line for kw in IGNORE_KEYWORDS):
            continue

        # Try main regex
        match = main_pattern.match(line)
        if match:
            test_name = match.group(1).strip()
            test_value = match.group(2).strip()
            test_unit = match.group(3).strip()
            reference = match.group(4).strip()
            if not (test_value.replace('.', '', 1).isdigit() or test_value.upper() in CATEGORICAL_VALUES):
                continue
            if len(test_name) < 3:
                continue
            out_of_range = is_out_of_range(test_value, reference)
            data.append({
                "test_name": test_name,
                "test_value": test_value,
                "bio_reference_range": reference,
                "test_unit": test_unit,
                "lab_test_out_of_range": out_of_range
            })
            continue

        # Fallback: split by 2+ spaces or tabs (for tabular data)
        columns = re.split(r"\s{2,}|\t", line)
        columns = [c.strip() for c in columns if c.strip()]
        if 2 <= len(columns) <= 4:
            test_name = columns[0]
            test_value = columns[1]
            test_unit = columns[2] if len(columns) > 2 else ""
            reference = columns[3] if len(columns) > 3 else ""
            if not (test_value.replace('.', '', 1).isdigit() or test_value.upper() in CATEGORICAL_VALUES):
                continue
            if len(test_name) < 3:
                continue
            out_of_range = is_out_of_range(test_value, reference)
            data.append({
                "test_name": test_name,
                "test_value": test_value,
                "bio_reference_range": reference,
                "test_unit": test_unit,
                "lab_test_out_of_range": out_of_range
            })
    return data
