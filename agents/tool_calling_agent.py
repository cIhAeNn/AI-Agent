from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_anthropic import ChatAnthropic
from pydantic import PydanticOutputParser
from models.research_response import ResearchResponse
from utils.prompt_templates import create_prompt_template
from tools import search_tool, wiki_tool, save_tool
from agents.agent import Agent
import os

class ToolCallingAgent(Agent):
    def __init__(self, llm_model=os.getenv("LLM_MODEL")):
        self.llm = ChatAnthropic(model=llm_model)
        self.tools = [search_tool, wiki_tool, save_tool]
        self.parser = PydanticOutputParser(pydantic_object=ResearchResponse)
        self.prompt = create_prompt_template(self.parser)
        self.agent = create_tool_calling_agent(
            llm=self.llm,
            prompt=self.prompt,
            tools=self.tools,
        )
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    async def run(self, query:str):

        raw_response = await self.agent_executer.ainvoke({"query":query})

        try:
            output = raw_response.get("output")
            if output and isinstance(output, list):
                return self.parser.parse(raw_response.get("output")[0]["text"])
            else:
                return {"error": "Invalid response format"}
        except Exception as e:
            return {"error": f"Error while parsing response: {str(e)}"}
