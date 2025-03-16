import openai
from abc import ABC, abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class AgentBase(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call(self, messages, temperature=0.7, max_tokens=150):
        retries = 0

        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] Sending message to MOdel API...")
                    for msg in messages:
                        logger.debug(f"{msg['role']}: {msg['content']}")
                
                response = self.client.chat.completions.create(
                    model = "gpt-3.5-turbo",
                    messages = messages,
                    temperature = temperature,
                    max_tokens = max_tokens
                )

                reply = response.choices[0].message.content
                if self.verbose:
                    logger.info(f"[{self.name}] Received reply from Model API: {reply}")
                
                return reply 
            except Exception as e:
                retries += 1
                if self.verbose:
                    logger.error(f"[{self.name}] Error calling Model API: {e}")
                    logger.error(f"[{self.name}] Retry {retries}/{self.max_retries}")

        raise Exception(f"Failed to call Model API after {self.max_retries} retries")