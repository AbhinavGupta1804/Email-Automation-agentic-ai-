from src.tools.tools import send_email_tool


def send_email_node(state):
    """
    Sends the email using Gmail SMTP
    """
    email_data = state.get("final_email", {})

    if not email_data.get("to") or not email_data.get("body"):
        print("❌ Email not sent: recipient or body missing")
        state["email_status"] = "Failed"
        return state

    state = send_email_tool(state)
    return state
