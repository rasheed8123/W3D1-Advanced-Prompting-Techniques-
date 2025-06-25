# 🧠 Prompt Engineering Pipeline: Multi-Path Reasoning + Optimization

## 💡 Overview
A local LLM-based system to solve structured reasoning problems using:
- Tree-of-Thought (ToT) prompting
- Self-Consistency voting
- Automated Prompt Optimization (OPRO)

## 🧱 Structure

project/
├── main.py
├── utils/
│ ├── tree_of_thought.py
│ ├── optimizer.py
│ └── tinyllama_runner.py
├── logs/
│ └── results.jsonl
├── evaluation.py
├── report.md
└── README.md

yaml


---

## 🚀 How It Works

1. **ToT Prompting**: Generates multiple reasoning paths
2. **Voting**: Applies self-consistency to select a majority answer
3. **Optimization**: Refines prompt based on failures using LLM feedback

---

## 🛠️ Usage

```bash
python main.py
You'll be prompted to enter a math/logic/code problem (e.g. Solve: 2(x + 3) = 16)

To evaluate performance:

bash

python evaluation.py
📊 Evaluation Metrics
Accuracy (% correct)

Hallucination Rate

Reasoning Quality (manual review)

🔧 Dependencies
Python 3.10+

Ollama + TinyLlama installed locally

👥 Authors
[Your Name]

Built as part of Misogi AI Week – Day 3

🧪 Example
Input:

makefile

Solve: 2(x + 3) = 16
Output:

yaml

✅ Final Answer: 5
Votes: {'5': 3, '6': 1, '9': 1}
📘 License
MIT

yaml


---

Would you like me to:
- Add code that *writes each task result to `logs/results.jsonl`*?
- Help generate 5 example tasks with expected answers for 
