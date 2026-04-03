class MarketingAgent:
    """
    Agent responsabil pentru marketing:
    - generează texte promoționale
    - creează reclame
    - creează postări pentru social media
    - pregătește campanii
    """

    def __init__(self):
        print("[MarketingAgent] Activat.")

    def generate_ad_copy(self, product: str) -> str:
        """
        Creează un text promoțional simplu.
        (Mai târziu îl conectăm la Groq pentru generare AI reală)
        """
        return (
            f"Descoperă {product}! Soluția perfectă pentru a-ți transforma afacerea "
            "și a obține rezultate mai bune în cel mai scurt timp."
        )

    def create_social_post(self, topic: str) -> str:
        """
        Creează o postare scurtă pentru social media.
        """
        return (
            f"🔥 Noutăți despre {topic}! 🔥\n"
            "Află cum poți folosi tehnologia pentru a-ți crește afacerea."
        )

    def build_campaign(self, name: str, goal: str) -> dict:
        """
        Creează o campanie de marketing.
        """
        print(f"[MarketingAgent] Construiesc campania '{name}' cu obiectivul: {goal}")

        return {
            "campaign_name": name,
            "goal": goal,
            "status": "draft",
            "steps": [
                "Analiză public țintă",
                "Creare mesaje",
                "Creare vizualuri",
                "Programare postări",
                "Lansare campanie"
            ]
        }
