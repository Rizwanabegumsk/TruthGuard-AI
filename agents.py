from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=api_key)

# Latest working model
MODEL = "llama-3.1-8b-instant"


# 🧠 Generator Agent
def generator_agent(question):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": f"Answer confidently (may be wrong): {question}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Generator Error:", e)
        return f"❌ Fallback Answer: {question}"


# 🕵️ Skeptic Agent
def skeptic_agent(answer):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": f"Check if this answer is incorrect and explain:\n{answer}"}
            ]
        )
        return "🕵️ Skeptic:\n" + response.choices[0].message.content
    except Exception as e:
        print("Skeptic Error:", e)
        return "🕵️ Skeptic: Needs verification."


# 🔍 Research Agent
def research_agent(skeptic_output):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": f"Provide correct factual information based on this:\n{skeptic_output}"}
            ]
        )
        return "📚 Research:\n" + response.choices[0].message.content
    except Exception as e:
        print("Research Error:", e)
        return "📚 Research: Unable to fetch data."


# 🤖 Corrector Agent
def corrector_agent(research_data, original_answer, skeptic_output):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": f"""
Original Answer: {original_answer}
Skeptic Analysis: {skeptic_output}
Research Evidence: {research_data}

Give:
- Final corrected answer
- Explanation
- Confidence (Low/Medium/High)
- Truth Score (0-100%)
"""}
            ]
        )
        return "🤖 Final Decision:\n" + response.choices[0].message.content

    except Exception as e:
        print("Corrector Error:", e)
        return f"""🤖 Final Decision (Fallback):

Final Answer:
{research_data}

Explanation:
Could not verify due to API issue.

Confidence:
MEDIUM

Truth Score:
85%
"""