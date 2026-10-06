from dotenv import load_dotenv
from langfuse import Langfuse
import os

load_dotenv()

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)

trace = langfuse.trace(
    name="agent-test"
)

trace.event(
    name="startup",
    input={"message": "Agent started"}
)

langfuse.flush()

print("Trace sent")