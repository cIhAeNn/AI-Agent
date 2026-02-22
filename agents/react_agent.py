from langchain_anthropic import ChatAnthropic
from pydantic import PydanticOutputParser
from models.research_response import ResearchResponse
from tools import search_tool, wiki_tool, save_tool
from agents.agent import Agent

class ReactAgent(Agent):
    def __init__(self, llm_model="claude-3-5-sonnet-20241022"):
        self.llm = ChatAnthropic(model=llm_model)
        self.tools = [search_tool, wiki_tool, save_tool]
        self.parser = PydanticOutputParser(pydantic_object=ResearchResponse)
        # Define the behavior specific to ReactAgent

    async def run(self, query: str):
        # Custom logic for ReactAgent
        return {"message": "React agent is still under construction"}