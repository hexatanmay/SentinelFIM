from pathlib import Path


class RiskEngine:
    """
    Calculates risk scores for file system events.
    """

    EVENT_SCORES = {
        "created": 20,
        "modified": 30,
        "moved": 40,
        "deleted": 60,
    }

    HIGH_RISK_EXTENSIONS = {
        ".exe",
        ".dll",
        ".bat",
        ".cmd",
        ".ps1",
        ".vbs",
        ".js",
        ".jar",
        ".msi",
    }

    SENSITIVE_EXTENSIONS = {
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".csv",
        ".db",
        ".sqlite",
        ".json",
    }

    HIGH_RISK_PATHS = {
        "windows",
        "system32",
        "startup",
        "programdata",
    }

    @classmethod
    def calculate_risk(cls, event_type: str, file_path: str):
        """
        Returns:
            (risk_score, severity)
        """

        score = cls.EVENT_SCORES.get(event_type.lower(), 5)

        extension = Path(file_path).suffix.lower()

        # Executable / script files
        if extension in cls.HIGH_RISK_EXTENSIONS:
            score += 40

        # Sensitive business/user files
        if extension in cls.SENSITIVE_EXTENSIONS:
            score += 15

        # High-risk locations
        path_lower = str(file_path).lower()

        for keyword in cls.HIGH_RISK_PATHS:
            if keyword in path_lower:
                score += 30
                break

        # Cap at 100
        score = min(score, 100)

        severity = cls.get_severity(score)

        return score, severity

    @staticmethod
    def get_severity(score: int):
        if score < 25:
            return "LOW"
        elif score < 50:
            return "MEDIUM"
        elif score < 75:
            return "HIGH"
        else:
            return "CRITICAL"
