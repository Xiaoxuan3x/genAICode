from azure.ai.openai import OpenAIClient
from azure.core.credentials import AzureKeyCredential

# Initialize the Azure OpenAI client with endpoint and API key
endpoint = "https://<your-openai-service>.openai.azure.com/"
api_key = "<your_api_key>"
client = OpenAIClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

# Define agent functions with specific tasks and models

def general_banking_advice(client, user_input, model="gpt-3.5-turbo"):
    response = client.completions.create(
        model=model,
        prompt=f"Provide general banking advice for the following question: {user_input}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def account_provisioning(client, user_input, model="gpt-3.5-turbo"):
    response = client.completions.create(
        model=model,
        prompt=f"Assist the user with account provisioning and onboarding for the following request: {user_input}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def customer_support(client, user_input, model="gpt-3.5-turbo"):
    response = client.completions.create(
        model=model,
        prompt=f"Provide 24/7 customer support for issues like account unlocking, PIN reset. Here is the user's question: {user_input}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def loan_eligibility_check(client, user_input, model="gpt-4"):
    response = client.completions.create(
        model=model,
        prompt=f"Assist in checking loan eligibility and creditworthiness for the following details: {user_input}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def money_management_assistant(client, user_input, model="gpt-3.5-turbo"):
    response = client.completions.create(
        model=model,
        prompt=f"Provide money management and financial planning advice for the following question: {user_input}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Routing function to direct user queries to the appropriate agent with model selection
def route_query(client, user_input):
    if "open account" in user_input.lower():
        return account_provisioning(client, user_input, model="gpt-3.5-turbo")
    elif "loan" in user_input.lower() or "credit" in user_input.lower():
        return loan_eligibility_check(client, user_input, model="gpt-4")
    elif "advice" in user_input.lower():
        return general_banking_advice(client, user_input, model="gpt-3.5-turbo")
    elif "support" in user_input.lower() or "unlock" in user_input.lower():
        return customer_support(client, user_input, model="gpt-3.5-turbo")
    elif "budget" in user_input.lower() or "manage money" in user_input.lower():
        return money_management_assistant(client, user_input, model="gpt-3.5-turbo")
    else:
        return "I'm sorry, I didn't understand your request. Could you please provide more details?"
