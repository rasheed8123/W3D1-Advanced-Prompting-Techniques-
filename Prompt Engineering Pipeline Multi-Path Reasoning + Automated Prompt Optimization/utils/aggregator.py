import re
from collections import Counter

def extract_final_answer(response: str) -> str:
    # Try to extract 'x = <value>' pattern first
    matches = re.findall(r"x\s*=\s*-?\d+\.?\d*", response)
    if matches:
        return matches[-1].strip()
    
    # Fallback: extract any number
    matches = re.findall(r"[-+]?\d+\.?\d*", response)
    if matches:
        return matches[-1]
    
    # Fallback: last line
    return response.strip().split("\n")[-1]

def self_consistency(paths):
    answers = [extract_final_answer(p) for p in paths]
    count = Counter(answers)
    most_common, freq = count.most_common(1)[0]
    return most_common, count
