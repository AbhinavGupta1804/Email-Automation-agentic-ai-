from src.tools.tools import send_email_tool
def aggregator_node(state):
    """
    Prepares structured email components (subject, body, recipient)
    to be used by the email sender node.
    """
    recipient = state.get("recipient", "")
    subject = state.get("subject", "No Subject")
    body = state.get("body", "No content")

    # Store them in separate keys for clarity
    state["final_email"] = {
        "to": recipient,
        "subject": subject,
        "body": body
    }
    state = send_email_tool(state)
    return state
