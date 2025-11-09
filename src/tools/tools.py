from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from src.ui.config import Config

def send_email_tool(state):
    """
    Sends an email using SendGrid based on the data in the state.
    Expects: state["recipient"], state["subject"], state["final_email"]
    """
    config = Config()
    email_data = state.get("final_email")
    if not email_data["to"]:
        print("❌ No recipient email found in state.")
        return state

    try:
        sg = SendGridAPIClient(config.get_sendgrid_api_key())
        message = Mail(
            from_email=config.get_sender_email(),
            to_emails=email_data.get("to"),
            subject=email_data.get("subject"),
            html_content = email_data.get("body")
        )

        response = sg.send(message)
        print(f"✅ Email sent successfully! Status: {response.status_code}")
        state["email_status"] = "Sent"

    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        state["email_status"] = "Failed"

    return state
