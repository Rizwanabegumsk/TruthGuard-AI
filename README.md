TruthGuard AI
Overview
TruthGuard AI is a multi-agent system that improves the reliability of AI responses by verifying and correcting them using multiple reasoning agents.

Problem
AI models can generate confident but incorrect answers (hallucinations), reducing trust.

Solution
This system uses four agents:

Generator: produces an initial answer

Skeptic: checks for errors

Research: finds correct information

Corrector: gives final verified answer with confidence

Workflow
Input → Generator → Skeptic → Research → Corrector → Output

Tech Stack
Python

Groq API (LLaMA 3.1)

dotenv

Setup
git clone https://github.com/Rizwanabegumsk/TruthGuard-AI.git
cd TruthGuard-AI

python -m venv venv
venv\Scripts\activate

pip install groq python-dotenv
Create .env:

GROQ_API_KEY=your_api_key_here
Run:

python main.py
Use Cases
Fact checking

Reducing AI hallucinations

Educational tools

Decision validation systems

Author
Rizwanabegum Sk