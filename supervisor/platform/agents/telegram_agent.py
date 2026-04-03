import requests


class TelegramAgent:
    """
    Agent responsabil pentru comunicarea cu Supervisorul prin Telegram.
    - trimite mesaje
    - trimite rapoarte
    - trimite alerte
    """

    def __init__(self, bot_token: str, chat_id: str = None):
        self.bot_token = bot_token
        self.chat_id = chat_id  # îl setăm mai târziu
        print("[TelegramAgent] Activat.")

    def set_chat_id(self, chat_id: str):
        """
        Setează chat_id-ul supervisorului (al tău).
        """
        self.chat_id = chat_id
        print(f"[TelegramAgent] Chat ID setat: {chat_id}")

    def send_message(self, text: str) -> bool:
        """
        Trimite un mesaj simplu pe Telegram.
        """

        if not self.chat_id:
            print("[TelegramAgent] Eroare: chat_id nu este setat.")
            return False

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        payload = {
            "chat_id": self.chat_id,
            "text": text
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("[TelegramAgent] Mesaj trimis cu succes.")
                return True
            else:
                print(f"[TelegramAgent] Eroare Telegram: {response.text}")
                return False

        except Exception as e:
            print(f"[TelegramAgent] Eroare la trimiterea mesajului: {e}")
            return False

    def send_alert(self, message: str):
        """
        Trimite o alertă importantă.
        """
        alert_text = f"⚠️ ALERTĂ: {message}"
        return self.send_message(alert_text)

    def send_report(self, title: str, content: str):
        """
        Trimite un raport formatat.
        """
        report_text = f"📊 *{title}*\n\n{content}"
        return self.send_message(report_text)
