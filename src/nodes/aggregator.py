def aggregator_node(state):
    """
    Prepares structured email components (subject, body, recipient)
    to be used by the email sender node.
    """
    recipient = state.get("recipient")
    subject = state.get("subject")
    body = state.get("body")

    # Store them in separate keys for clarity
    state["final_email"] = {
        "to": recipient,
        "subject": subject,
        "body": body
    }
    return state
