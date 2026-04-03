from datetime import datetime


class Logger:
    def __init__(self, name: str = "AI-CORP"):
        self.name = name

    def _log(self, level: str, message: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] [{self.name}] [{level}] {message}")

    def info(self, message: str):
        self._log("INFO", message)

    def warning(self, message: str):
        self._log("WARNING", message)

    def error(self, message: str):
        self._log("ERROR", message)
