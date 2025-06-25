from utils.llm_interface import query_tinyllama


def generate_thought_paths(problem: str, n_paths: int = 3, base_prompt: str = None):
    if base_prompt is None:
        base_prompt = f"""
You are a helpful math tutor. Solve the following equation carefully and show your steps clearly.

Problem: {problem}

Steps:
1."""
    paths = []
    for _ in range(n_paths):
        prompt = base_prompt.replace("{problem}", problem)
        response = query_tinyllama(prompt)
        paths.append(response)
    return paths
