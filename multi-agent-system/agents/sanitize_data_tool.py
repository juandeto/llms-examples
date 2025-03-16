from .agent_base import AgentBase
from loguru import logger

class SanitizeDataTool(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="SanitizeDataTool", max_retries=max_retries, verbose=verbose)
    
    def execute(self, medical_data):
        messages = [
            {"role": "system", "content": "You are an AI assistant that sanitizes medical data by removing Protected Health Information (PHI)."},
            {"role": "user", "content": (
                "Remove all PHI from the following medical text:\n\n",
                f"{medical_data}\n\n Sanitized Data:",
            )}
        ]
        sanitized_data = self.call(messages, max_tokens=300)
        return sanitized_data