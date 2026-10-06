import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

historical_traces = """
Trace 1:
Task failed, retried successfully.

Trace 2:
User rejected action.

Trace 3:
Task completed normally.

Trace 4:
Checkpoint recovered after interruption.

Trace 5:
Tool execution succeeded.

Trace 6:
Invalid task blocked by hook.

Trace 7:
Task approved and executed.

Trace 8:
Task saved to storage.

Trace 9:
State restored from checkpoint.

Trace 10:
Langfuse trace logged.
"""

prompt = f"""
You are an evaluator.

Review these agent traces.

Rate the agent's Error Recovery
from 1 to 5.

Explain reasoning.

{historical_traces}
"""

response = model.generate_content(prompt)

print(response.text)