import threading
import time
from typing import Callable


class TaskManager:
    """
    Se ocupă de task-uri programate (recurente).
    De exemplu:
    - verifică campanii
    - pornește agenți
    - trimite rapoarte
    """

    def __init__(self, supervisor: "Supervisor") -> None:
        self.supervisor = supervisor
        self._running = False

    def start_scheduled_tasks(self) -> None:
        """
        Pornește un thread separat care rulează task-uri la intervale.
        Deocamdată avem doar un task de test.
        """
        if self._running:
            return

        self._running = True
        thread = threading.Thread(target=self._loop, daemon=True)
        thread.start()
        print("[TaskManager] Task-urile programate au fost pornite.")

    def _loop(self) -> None:
        """
        Rulează la nesfârșit, la intervale fixe.
        Deocamdată: la fiecare 60 de secunde trimite un task de test.
        """
        while self._running:
            # Exemplu: la fiecare 60 secunde, trimitem un task de test
            self._run_safe(self._test_task)
            time.sleep(60)

    def _run_safe(self, func: Callable[[], None]) -> None:
        """
        Rulează un task și prinde eventualele erori,
        ca să nu se oprească tot sistemul.
        """
        try:
            func()
        except Exception as e:
            print(f"[TaskManager] Eroare în task: {e}")

    def _test_task(self) -> None:
        """
        Task de test – doar ca să vedem că sistemul funcționează.
        Mai târziu îl înlocuim cu task-uri reale (emailuri, campanii, etc.).
        """
        print("[TaskManager] Rulez task-ul de test.")
        self.supervisor.handle_task("test", {"source": "TaskManager"})
