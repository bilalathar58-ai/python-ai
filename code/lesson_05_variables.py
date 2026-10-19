
"""Lesson 1.5: AI Model Profile Card and token cost estimate."""

MODEL = "gemini-4-argon"
temperature: float = 0.2
max_tokens: int = 300
stream: bool = False
system_prompt: str = "You are a helpful Python tutor."

price_per_1k_tokens: float = 0.5  # PKR per 1,000 tokens

print("--- AI Model Profile Card ---")
print(f"Model: {MODEL} ({type(MODEL)})")
print(f"Temperature: {temperature} ({type(temperature)})")
print(f"Max tokens: {max_tokens} ({type(max_tokens)})")
print(f"Streaming: {stream} ({type(stream)})")
print(f"System prompt: {system_prompt} ({type(system_prompt)})")

tokens_used = int(input("Tokens used: "))
cost = tokens_used / 1000 * price_per_1k_tokens

print(f"Estimated cost: {round(cost, 2)} PKR")
