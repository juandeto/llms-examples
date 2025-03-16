from .agent_base import AgentBase
from loguru import logger

class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="SanitizeDataValidatorAgent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, original_data, sanitized_data):
        system_message = "You are an expert AI assistant that validates the sanitization of medical data by checking the removal of PHI. It's important to NOT MODIFICATE the language of the original data."
        user_content = (
            "Given the original data and sanitized data, verify that all the PHI has been removed \n"
            "Provide a brief analysis and rate the sanitized process on a scale of 1 to 5, where 5 indicates excellent quality and 1 indicates poor quality.\n"
            f"Original Data: {original_data}.\n\n"
            f"Sanitized Data:\n{sanitized_data}\n\n"
            f"Validation Score:"
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        
        validation = self.call(messages, max_tokens=1000)
        return validation