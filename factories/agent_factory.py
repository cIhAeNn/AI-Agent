from agents.react_agent import ReactAgent
from agents.tool_calling_agent import ToolCallingAgent

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str):
        match agent_type:
            case "ToolCallingAgent":
                return ToolCallingAgent()
            case "ReactAgent":
                return ReactAgent()
            case _:
                raise ValueError(f"Unknown Agent Type: {agent_type}")