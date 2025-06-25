# prompts.py

def zero_shot(query):
    # Make zero-shot more instructive to reduce vague outputs
    return (
        f"{query}\n"
        "Explain your answer clearly with all steps if it's a problem, or examples if it's a concept."
    )


def few_shot(query):
    # Add a more diverse and aligned example to guide the model
    return (
        "Example 1:\n"
        "Solve the equation: 3x + 4 = 19\n"
        "Answer:\n"
        "Step 1: Subtract 4 from both sides → 3x = 15\n"
        "Step 2: Divide both sides by 3 → x = 5\n\n"
        "Example 2:\n"
        "Solve the equation: 4x - 2 = 10\n"
        "Answer:\n"
        "Step 1: Add 2 to both sides → 4x = 12\n"
        "Step 2: Divide by 4 → x = 3\n\n"
        f"Now solve the equation: {query}\n"
        "Answer:"
    )


def cot(query):
    # Force chain-of-thought reasoning with a step-by-step mindset
    return (
        f"Solve the following problem step by step: {query}\n"
        "Step 1: Identify what we want to find.\n"
        "Step 2: What operations are being applied to the variable?\n"
        "Step 3: Reverse those operations one at a time.\n"
        "Now solve and explain your reasoning clearly."
    )


def self_ask(query):
    # Use nested self-questioning better suited for math tutoring
    return (
        f"Let's break down the problem: {query}\n"
        "What is the unknown we need to find?\n"
        "What operations are applied to the unknown?\n"
        "In what order should we reverse those operations?\n"
        "Answer step by step, asking and answering each sub-question."
    )


def fallback():
    return (
        "I couldn't understand your request. Would you like help solving a math problem, understanding a concept, or doing a step-by-step explanation?"
    )
