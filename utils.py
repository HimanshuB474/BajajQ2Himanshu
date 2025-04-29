import re

def is_out_of_range(test_value, reference_range):
    try:
        value = float(re.findall(r"[\d.]+", test_value)[0])
        ref_values = [float(x) for x in re.findall(r"[\d.]+", reference_range)]
        if len(ref_values) == 2:
            return not (ref_values[0] <= value <= ref_values[1])
        return False
    except:
        return False
