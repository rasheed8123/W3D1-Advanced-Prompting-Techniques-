from utils.tree_of_thought import generate_thought_paths
from utils.aggregator import self_consistency
from utils.prompt_optimizer import optimize_prompt
from datetime import datetime
import json

def log_prompt_version(prompt: str, outputs: list[str], final_answer: str, file_path="logs/prompt_versions.json"):
    try:
        with open(file_path, "r") as f:
            versions = json.load(f)
    except FileNotFoundError:
        versions = []

    versions.append({
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "outputs": outputs,
        "final_answer": final_answer
    })

    with open(file_path, "w") as f:
        json.dump(versions, f, indent=2)

def main():
    print("🎯 Multi-Path Reasoning via TinyLlama")
    problem = input("Enter a structured reasoning problem:\n> ").strip()

    print("\n🔁 Generating reasoning paths...\n")

    prompt_template = f"""You are a helpful math tutor. Solve the following equation carefully and show your steps clearly.

Problem: {problem}

Steps:
1."""
    paths = generate_thought_paths(problem, n_paths=5, base_prompt=prompt_template)

    for i, path in enumerate(paths):
        print(f"\n--- Reasoning Path {i+1} ---\n{path}")

    print("\n🧠 Applying Self-Consistency...\n")
    final_answer, votes = self_consistency(paths)

    print(f"✅ Final Answer (by majority): {final_answer}")
    print(f"Votes: {votes}")

    log_prompt_version(prompt_template, paths, final_answer)

    retry = input("\n🔁 Do you want to improve the prompt and retry? (y/n): ").strip().lower()
    if retry == "y":
        improved_prompt = optimize_prompt(prompt_template, paths, expected="x = 5")
        print("\n🛠️ Optimized Prompt:\n", improved_prompt)

        print("\n🔁 Regenerating with improved prompt...\n")
        improved_paths = generate_thought_paths(problem, n_paths=3, base_prompt=improved_prompt)

        for i, path in enumerate(improved_paths):
            print(f"\n--- Improved Path {i+1} ---\n{path}\n")

        final_answer, votes = self_consistency(improved_paths)
        print(f"\n✅ New Final Answer: {final_answer}")

if __name__ == "__main__":
    main()
