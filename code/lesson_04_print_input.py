

"""Create an AI prompt using details entered by a business owner."""

# Real business details help the AI provide useful recommendations.
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

# A specific problem helps the AI suggest relevant business solutions.
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(f"\nWelcome, {name}!")
print("\n--- Your AI Prompt ---")
print(prompt)
