from dataclasses import dataclass 
from typing import Dict

@dataclass 
class Headers: 
    headers: Dict[str, str]

    def has(self, key: str) -> bool:
        return key in self.headers.keys()

    def get(self, key: str) -> str | None: 
        if self.has(key):
            return self.headers[key]

        return None 

    def add(self, key, value) -> None: 
        self.headers[key] = value
