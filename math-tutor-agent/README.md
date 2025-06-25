# 🧠 Math Tutor Agent

An intelligent math tutor built using a local LLM (Mistral via Ollama) that answers math queries with step-by-step reasoning in various prompting styles.

---

## 📦 Project Structure

math-tutor-agent/
├── tutor_agent.py # Main script to run the tutor agent
├── prompts.py # Prompt templates for different reasoning styles
├── evaluate.py # Script to evaluate performance across prompts
├── queries.json # Dataset of math questions to test
├── responses.json # Model-generated outputs
└── README.md # This file

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/math-tutor-agent.git
cd math-tutor-agent
2. Install Python Requirements (if any)
No external dependencies other than Python and Ollama CLI.

bash
Copy
Edit
# Optional if using virtualenv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install & Start Ollama
Install Ollama: https://ollama.com/download

Then pull the Mistral model:

bash
Copy
Edit
ollama pull mistral
⚠️ Make sure ollama is available in your system PATH.

🚀 Running the Agent
bash
Copy
Edit
python tutor_agent.py
This will:

Read math problems from queries.json

Generate responses from the Mistral model

Save results to responses.json

✅ Evaluation
To evaluate performance across prompts (accuracy, reasoning, hallucinations, consistency):

bash
Copy
Edit
python evaluate.py
Sample Output:
yaml
Copy
Edit
📊 Evaluation Summary:
Accuracy:         4 / 20
Reasoning:        5 / 20
No Hallucinations: 12 / 20
Consistency:      9 / 20
✨ Prompting Strategies Supported
Zero-shot: Basic query without examples.

Few-shot: Includes example problems + solution steps.

Chain-of-Thought (CoT): Encourages step-by-step reasoning.

Self-ask: Breaks problem down into sub-questions.

Prompt logic is defined in prompts.py.

