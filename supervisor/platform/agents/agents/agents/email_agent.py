import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailAgent:
    """
    Agent responsabil pentru trimiterea emailurilor.
    - trimite emailuri simple
    - trimite emailuri HTML
    - (mai târziu) generează texte cu AI
    """

    def __init__(self, host: str, port: int, user: str, password: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

        print("[EmailAgent] Activat.")

    def send_email(self, to_email: str, subject: str, message: str, html: bool = False) -> bool:
        """
        Trimite un email simplu sau HTML.
        """

        try:
            msg = MIMEMultipart("alternative")
            msg["From"] = self.user
            msg["To"] = to_email
            msg["Subject"] = subject

            if html:
                msg.attach(MIMEText(message, "html"))
            else:
                msg.attach(MIMEText(message, "plain"))

            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()
                server.login(self.user, self.password)
                server.sendmail(self.user, to_email, msg.as_string())

            print(f"[EmailAgent] Email trimis către {to_email}")
            return True

        except Exception as e:
            print(f"[EmailAgent] Eroare la trimiterea emailului: {e}")
            return False

    def generate_email_text(self, topic: str) -> str:
        """
        Placeholder pentru generarea textelor cu AI.
        (mai târziu îl conectăm la Groq)
        """
        return f"Acesta este un email generat automat despre: {topic}"
