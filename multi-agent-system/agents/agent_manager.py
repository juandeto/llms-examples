from .agent_base import AgentBase
from .write_article_tool import WriteArticleTool
from .write_article_validator import WriteArticleValidatorAgent
from .sanitize_data_tool import SanitizeDataTool
from .sanitize_data_validator import SanitizeDataValidatorAgent
from .summarize_tool import SummarizeTool
from .summarize_validator import SummarizeValidatorAgent
from .refiner_agent import RefinerAgent
from .validator_agent import ValidatorAgent
from loguru import logger

class AgentManager:
    def __init__(self, max_retries = 2, verbose = True):
        self.agents = {
            "summarize": SummarizeTool(max_retries=max_retries, verbose=verbose),
            "summarize_validator_agent": SummarizeValidatorAgent(max_retries=max_retries, verbose=verbose),
            "write_article": WriteArticleTool(max_retries=max_retries, verbose=verbose),
            "write_article_validator_agent": WriteArticleValidatorAgent(max_retries=max_retries, verbose=verbose),
            "sanitize_data": SanitizeDataTool(max_retries=max_retries, verbose=verbose),
            "sanitize_data_validator_agent": SanitizeDataValidatorAgent(max_retries=max_retries, verbose=verbose),
            "refiner": RefinerAgent(max_retries=max_retries, verbose=verbose),
            "validator": ValidatorAgent(max_retries=max_retries, verbose=verbose)
        }
    
    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)

        if not agent:
            raise ValueError(f"Agent {agent_name} not found")
        
        return agent
    
     