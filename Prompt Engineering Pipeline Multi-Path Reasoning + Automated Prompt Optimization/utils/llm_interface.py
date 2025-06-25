import subprocess

def query_tinyllama(prompt: str) -> str:
    command = ["ollama", "run", "tinyllama"]
    result = subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8",  # ✅ Force utf-8 decoding
        errors="replace"   # ✅ Replace invalid characters with �
    )
    return result.stdout.strip()
