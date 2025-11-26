import re

def router_node(state):
    """
    Extracts recipient email and message context from the user's prompt.
    
    """
    prompt = state.get("prompt")
    # extract email using regex
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', prompt)
    recipient = email_match.group(0) if email_match else None

    # remove email part to get context
    context = re.sub(r'[\w\.-]+@[\w\.-]+', '', prompt)
    context = context.replace("send", "").replace("email", "").replace("to", "").strip()

    return {"recipient": recipient, "context": context}
