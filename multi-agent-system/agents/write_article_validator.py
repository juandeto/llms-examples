from .agent_base import AgentBase
from loguru import logger

class WriteArticleValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="WriteArticleValidatorAgent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, topic, article):
        system_message = "You are an expert AI assistant that validates research articles."
        user_content = (
            "Given the topic and the article, asses whether the article is comprenhensively, covers the topic, follows a logical structure and maintains acadeic standards. \n"
            "Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality and 1 indicates poor quality.\n"
            f"Topic: {topic}.\n\n"
            f"Article:\n{article}\n\n"
            f"Validation Score:"
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        
        validation = self.call(messages, max_tokens=1000)
        return validation