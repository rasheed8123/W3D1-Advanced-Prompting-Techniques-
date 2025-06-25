import json

# Load results
with open("results.json") as f:
    data = json.load(f)

# Criteria tags
def evaluate_response(item):
    output = item["output"].lower()

    if "[error]" in output or "[exception]" in output or not output.strip():
        return "❌ Error/Timeout", 0, 0, 0, 0

    hallucination = "yes" if any(bad in output for bad in [
        "x = -10.5", "123.8", "imaginary", "matlab", "dof", "wrong steps"
    ]) else "no"

    accuracy = 1 if item["query"].startswith("Solve: 2x - 7 = 15") and "x = 11" in output else 0
    reasoning = 1 if "step" in output or "first" in output else 0
    consistency = 1 if "x =" in output or math_like(output) else 0

    return hallucination, accuracy, reasoning, 1 if hallucination == "no" else 0, consistency

def math_like(text):
    return any(k in text for k in ["x =", "=", "step", "solve", "km/h"])

# Evaluate
scores = {"total": 0, "accuracy": 0, "reasoning": 0, "non_hallucinated": 0, "consistency": 0}

for item in data:
    hallucination, a, r, nh, c = evaluate_response(item)
    item["hallucination"] = hallucination
    item["accuracy_score"] = a
    item["reasoning_score"] = r
    item["hallucination_score"] = nh
    item["consistency_score"] = c

    scores["total"] += 1
    scores["accuracy"] += a
    scores["reasoning"] += r
    scores["non_hallucinated"] += nh
    scores["consistency"] += c

# Save updated results
with open("results_evaluated.json", "w") as f:
    json.dump(data, f, indent=2)

# Print summary
print("\n📊 Evaluation Summary:")
print(f"Accuracy: {scores['accuracy']} / {scores['total']}")
print(f"Reasoning: {scores['reasoning']} / {scores['total']}")
print(f"No Hallucinations: {scores['non_hallucinated']} / {scores['total']}")
print(f"Consistency: {scores['consistency']} / {scores['total']}")
