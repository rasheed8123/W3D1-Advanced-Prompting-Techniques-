import subprocess
import json
from prompts import zero_shot, few_shot, cot, self_ask, fallback

# Load queries
with open('queries.json') as f:
    queries = json.load(f)

# Define prompt strategies
prompt_styles = {
    "zero-shot": zero_shot,
    "few-shot": few_shot,
    "cot": cot,
    "self-ask": self_ask
}

results = []

# Run each query with each prompt strategy
for query in queries:
    for style, prompt_fn in prompt_styles.items():
        prompt = prompt_fn(query)

        print(f"\n=== Running [{style.upper()}] for query: {query} ===")

        try:
            # Call Ollama and run prompt using tinyllama
            result = subprocess.run(
                ['ollama', 'run', 'mistral'],
                input=prompt.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=180
            )

            output = result.stdout.decode().strip()
            error = result.stderr.decode().strip()

            if not output and error:
                output = f"[Error]: {error}"

        except Exception as e:
            output = f"[Exception]: {str(e)}"

        results.append({
            'query': query,
            'style': style,
            'prompt': prompt,
            'output': output
        })

# Save results
with open('results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n✅ All queries processed. Results saved to results.json")
