from enum import Enum

class ArgumentOptionEnum(str, Enum):
    PRO: str = 'Pro'
    CONTRA: str = 'Contra'
    FRAGE: str = 'Frage'
    RISIKO: str = 'Risiko'