import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_email_tool(state: dict) -> dict:
    """
    Sends email using Gmail SMTP with App Password.
    Expects state['final_email'] = {
        'to': str,
        'subject': str,
        'body': str
    }
    """

    email_data = state.get("final_email", {})

    sender_email = os.getenv("GMAIL_USER")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    if not sender_email or not app_password:
        print("❌ Gmail SMTP credentials missing")
        state["email_status"] = "Failed"
        return state

    try:
        # Create email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email_data["to"]
        msg["Subject"] = email_data.get("subject", "No Subject")

        msg.attach(MIMEText(email_data["body"], "plain"))

        # Gmail SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)

        print("✅ Email sent via Gmail SMTP")
        state["email_status"] = "Sent"

    except Exception as e:
        print(f"❌ SMTP Email Error: {e}")
        state["email_status"] = "Failed"

    return state
