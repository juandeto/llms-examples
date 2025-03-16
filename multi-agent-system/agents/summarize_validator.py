from .agent_base import AgentBase
from loguru import logger

class SummarizeValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="SummarizeValidatorAgent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, original_text, summary):
        system_message = "You are an expert AI assistant that validates the summaries of medical data."
        user_content = (
            "Given the original summary, asses wether the summary accurately capture the key points and is of high quality. It's important to NOT MODIFICATE the language of the original text. \n"
            "Provide a brief analysis and rate the summary on a scale of 1 to 5, where 5 indicates excellent quality and 1 indicates poor quality.\n"
            f"Original Text: {original_text}.\n\n"
            f"Summary:\n{summary}\n\n"
            f"Validation Score:"
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        
        validation = self.call(messages, max_tokens=1000)
        return validation