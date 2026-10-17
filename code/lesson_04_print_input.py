
"""Lesson 1.4: Build an AI prompt from business input."""

# Set sample business details automatically.
name = "Malik Bilal"
business = "imported electronics gadgets business"
problem = "delays in imported stock and repeated customer questions"

# Build the AI prompt using an f-string.
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(f"\nWelcome, {name}!")
print("\n--- Your AI Prompt ---")
print(prompt)
