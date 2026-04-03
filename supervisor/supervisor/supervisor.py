import os
from dotenv import load_dotenv

from .task_manager import TaskManager


class Supervisor:
    """
    Creierul corporației tale AI.
    - primește task-uri
    - decide ce agent trebuie să lucreze
    - (mai târziu) vorbește cu agenții și cu AI-ul Groq
    """

    def __init__(self) -> None:
        # Încarcă variabilele din .env (GROQ_API_KEY, etc.)
        load_dotenv()

        self.groq_api_key = os.getenv("GROQ_API_KEY", "")
        if not self.groq_api_key:
            print("[Supervisor] ATENȚIE: GROQ_API_KEY nu este setat în .env")

        # Inițializăm Task Manager-ul (programatorul de task-uri)
        self.task_manager = TaskManager(supervisor=self)

        print("[Supervisor] Inițializat cu succes.")

    def start(self) -> None:
        """
        Punctul de start al corporației AI.
        De aici pornim task-urile recurente și logica principală.
        """
        print("[Supervisor] Pornire corporație AI...")
        self.task_manager.start_scheduled_tasks()
        print("[Supervisor] Corporația AI rulează. Gata de primit task-uri.")

    def handle_task(self, task_type: str, payload: dict | None = None) -> None:
        """
        Punct unic prin care trec toate task-urile.
        Aici decidem ce agent ar trebui să lucreze.
        Deocamdată doar afișăm, apoi legăm agenții reali.
        """
        if payload is None:
            payload = {}

        print(f"[Supervisor] Task primit: {task_type} | payload: {payload}")

        # Aici vom conecta agenții reali (email, prospectare, marketing, etc.)
        if task_type == "test":
            print("[Supervisor] Rulez un task de test.")
        else:
            print(f"[Supervisor] Nu cunosc încă tipul de task: {task_type}")
