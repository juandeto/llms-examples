from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, draft):
        messages = [
            {"role": "system", "content": [
                {
                    "type": "text",
                    "text": "You are an expert editor who refines and enhances articles for clarity, coherence and academic quality. It's important to NOT MODIFICATE the language of the original article."
                }
            ]},
            {"role": "user", "content": [
                {
                    "type": "text",
                    "text": (
                        "Please refine and enhance the following article to improve its language, coherence and overall quality:\n\n"
                        f"{draft}\n\n Refined Article:"
                    )
                }
            ]}
        ]
        
        refined_article = self.call(messages,temperature=0.3, max_tokens=1024)
        return refined_article