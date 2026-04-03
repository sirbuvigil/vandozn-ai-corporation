import requests


class ProspectAgent:
    """
    Agent responsabil pentru prospectare:
    - caută potențiali clienți
    - analizează date
    - generează lead-uri
    - pregătește mesaje personalizate
    """

    def __init__(self):
        print("[ProspectAgent] Activat.")

    def find_leads(self, keyword: str) -> list:
        """
        Caută potențiali clienți pe baza unui cuvânt cheie.
        (Deocamdată returnează date mock, dar îl putem conecta la API-uri reale)
        """

        print(f"[ProspectAgent] Caut lead-uri pentru: {keyword}")

        # Exemplu de date mock (temporar)
        leads = [
            {"name": "Firma Alpha", "email": "contact@alpha.com"},
            {"name": "Firma Beta", "email": "office@beta.com"},
            {"name": "Firma Gamma", "email": "hello@gamma.com"},
        ]

        return leads

    def analyze_lead(self, lead: dict) -> dict:
        """
        Analizează un lead și îi dă un scor.
        (Mai târziu putem folosi AI pentru scoring real)
        """

        score = 80  # scor mock
        print(f"[ProspectAgent] Lead analizat: {lead['name']} | scor: {score}")

        return {
            "lead": lead,
            "score": score
        }

    def generate_message(self, lead: dict) -> str:
        """
        Creează un mesaj personalizat pentru lead.
        (Mai târziu îl conectăm la Groq pentru generare AI)
        """

        name = lead.get("name", "client")
        return f"Salut {name},\n\nAm observat că firma ta ar putea beneficia de soluțiile noastre AI."
