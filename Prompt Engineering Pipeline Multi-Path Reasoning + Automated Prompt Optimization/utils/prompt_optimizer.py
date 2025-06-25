from utils.llm_interface import query_tinyllama

def optimize_prompt(old_prompt: str, outputs: list[str], expected: str) -> str:
    """
    Ask TinyLlama to improve the original prompt based on poor outputs and desired result.
    """
    prompt = f"""
You are a prompt optimizer.

Here is a flawed prompt:
---
{old_prompt}
---

Here are some bad or inconsistent model outputs:
---
{chr(10).join(outputs)}
---

The expected answer is: {expected}

Suggest a better prompt that will guide the model to solve the problem accurately with clear steps. Your improved prompt should be concise, math-specific, and easy to follow.
Write only the improved prompt:
"""

    new_prompt = query_tinyllama(prompt)
    return new_prompt.strip()
