from dataclasses import dataclass


@dataclass
class School:
    def __init__(self):
        pass

    def __repr__(self):
        return f"{getattr(self, '대학명')}"
