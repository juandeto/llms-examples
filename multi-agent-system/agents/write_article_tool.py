from .agent_base import AgentBase
from loguru import logger

class WriteArticleTool(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="WriteArticleAgent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, topic, outline = None):
        system_message = "You are an expert academic writer"
        user_content = f"Write an article on the following topic: \n Topic: {topic}."
        if outline:
            user_content += f"\n\nOutline: \n{outline}"

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]

        article = self.call(messages, max_tokens=1000)
        return article