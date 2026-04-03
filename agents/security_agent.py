class SecurityAgent:
    """
    Agentul de securitate al corporației AI.
    Scop:
    - verifică task-urile
    - blochează cereri suspecte
    - protejează sistemul de input-uri periculoase
    """

    def __init__(self):
        print("[SecurityAgent] Activat.")

    def validate_task(self, task_type: str, payload: dict) -> bool:
        """
        Verifică dacă task-ul este sigur.
        Aici putem adăuga reguli de securitate.
        """

        # Regula 1: task_type trebuie să fie string
        if not isinstance(task_type, str):
            print("[SecurityAgent] Respins: task_type invalid.")
            return False

        # Regula 2: payload trebuie să fie dict
        if not isinstance(payload, dict):
            print("[SecurityAgent] Respins: payload invalid.")
            return False

        # Regula 3: blocăm task-uri necunoscute (deocamdată)
        allowed_tasks = ["test"]
        if task_type not in allowed_tasks:
            print(f"[SecurityAgent] Atenție: task necunoscut '{task_type}'.")
            # Îl permitem, dar îl marcăm ca suspect
            return True

        return True

    def scan_payload(self, payload: dict) -> bool:
        """
        Verifică dacă payload-ul conține ceva suspect.
        (mai târziu putem adăuga filtre avansate)
        """
        for key, value in payload.items():
            if isinstance(value, str) and ("DROP TABLE" in value or "DELETE" in value):
                print("[SecurityAgent] Payload periculos detectat.")
                return False

        return True
