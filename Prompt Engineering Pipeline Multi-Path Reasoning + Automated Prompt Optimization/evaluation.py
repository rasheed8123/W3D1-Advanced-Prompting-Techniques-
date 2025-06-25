# evaluation.py
import json
from collections import Counter

def evaluate_results(results_path):
    with open(results_path, 'r') as f:
        lines = f.readlines()

    total = 0
    correct = 0
    hallucinated = 0
    all_votes = []

    for line in lines:
        record = json.loads(line)
        total += 1
        if record.get("correct"):
            correct += 1

        # Heuristic for hallucination: if votes are wildly inconsistent
        if len(set(record["votes"].values())) == len(record["votes"]):
            hallucinated += 1

        all_votes.append(record["votes"])

    accuracy = correct / total * 100
    hallucination_rate = hallucinated / total * 100

    print(f"Total Tasks Evaluated: {total}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Hallucination Rate: {hallucination_rate:.2f}%")

if __name__ == "__main__":
    evaluate_results("logs/results.jsonl")