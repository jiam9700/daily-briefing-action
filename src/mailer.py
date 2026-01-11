import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config import Config

# [FIX] Changed parameter from subject_prefix to subject (full control)
def send_email(html_content: str, subject: str):
    """
    Sends the HTML email via SMTP.
    """
    print(f"📧 Sending email with subject: {subject}")

    msg = MIMEMultipart("alternative")
    # [FIX] No longer appending extra text. Use the subject exactly as provided.
    msg["Subject"] = subject
    msg["From"] = Config.SENDER_EMAIL
    msg["To"] = Config.RECEIVER_EMAIL

    part = MIMEText(html_content, "html")
    msg.attach(part)

    try:
        if Config.SMTP_PORT == 465:
            server = smtplib.SMTP_SSL(Config.SMTP_SERVER, Config.SMTP_PORT)
        else:
            server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
            server.starttls()

        server.login(Config.SMTP_USER, Config.SMTP_PASSWORD)
        server.sendmail(Config.SENDER_EMAIL, Config.RECEIVER_EMAIL, msg.as_string())
        server.quit()
        
        print(f"✅ Email sent successfully.")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False