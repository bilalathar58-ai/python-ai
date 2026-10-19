
"""Lesson 1.6: Clean a messy user message before sending it to AI."""

name = input("Your name: ")
raw = input("Your question: ")

# Clean extra spaces and make the text easier to read.
clean_name = name.strip().title()
clean_question = raw.strip()

# Capitalize the first character without lowercasing the rest.
if clean_question:
    clean_question = clean_question[0].upper() + clean_question[1:]

# Estimate tokens and limit the question to 150 characters.
estimated_tokens = round(len(clean_question) / 4)
short_question = clean_question[:150]

# Check for Python without worrying about capitalization.
mentions_python = "python" in clean_question.lower()

prompt = f"""You are a helpful Python tutor.
Answer in 3 lines.
Student: {clean_name}
Question: {short_question}"""

print("=" * 40)
print(f"Cleaned name: {clean_name}")
print(f"Cleaned question: {clean_question}")
print(
    f"Characters: {len(clean_question)}, "
    f"about {estimated_tokens} tokens"
)
print(f"Mentions Python: {mentions_python}")
print("=" * 40)
print(prompt)
