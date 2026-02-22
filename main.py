from dotenv import load_dotenv
import asyncio
from factories.agent_factory import AgentFactory

load_dotenv()

async def main():
    while True:
        query = input("Please Choose agent (ToolCallingAgent/ReactAgent): ")
        if query.casefold() == "q".casefold():
            break

        try:
            agent = AgentFactory.create_agent(query)
            query_text = input("What is your research question? ")
            result = await agent.run(query_text)
            print("Result:", result)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
