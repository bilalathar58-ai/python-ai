
"""Create three ready-to-use AI prompts for a local business owner."""

# Ask for business details so the prompts fit the client's real needs.
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")
monthly_budget = int(input("Monthly budget (PKR): "))

print("\n=========================================")
print(f"       AI Prompt Kit for {business_name}")
print("=========================================")

# A specific audience and tone help the AI produce a more useful post.
marketing_prompt = (
    f"Write a short Instagram post for {business_name}, "
    f"a {business_type} in {city}. "
    f"Target {customers}. Use a friendly tone and include 1 call to action."
)

# Giving the AI a role and a clear situation guides its reply.
customer_service_prompt = (
    f"You are the manager of {business_name}. "
    "Write a polite reply to a customer whose order arrived late. "
    "Apologise sincerely and offer a small discount. "
    "Do not invent order details."
)

# The budget limit helps the AI suggest realistic, affordable options.
growth_prompt = (
    f"Suggest 3 low-cost AI ideas for a {business_type} in {city} "
    f"to attract {customers}. The monthly budget is "
    f"{monthly_budget} PKR. Give practical ideas and estimated costs; "
    "clearly label estimates and do not invent verified prices."
)

print("\n[1] Marketing")
print("-----------------------------------------")
print(marketing_prompt)

print("\n[2] Customer Service")
print("-----------------------------------------")
print(customer_service_prompt)

print("\n[3] Growth")
print("-----------------------------------------")
print(growth_prompt)

print("\n=========================================")
print("Tip: Review AI answers for made-up facts, prices, or tools.")
