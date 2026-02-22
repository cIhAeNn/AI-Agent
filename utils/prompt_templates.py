from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_prompt_template(parser):
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a research assistant that will help generate a research paper.
                Answer the user query and use necessary tools.
                Wrap the output in this format and provide no other text\n{format_instructions}
                """
            ),
            MessagesPlaceholder("chat_history"),
            ("human", "{query}"),
            MessagesPlaceholder("agent_scratchpad")
        ]
    ).partial(format_instructions=parser.get_format_instructions())