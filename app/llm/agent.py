from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    PromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from langchain.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from llm.tools.presidential_election import get_district_result
from llm.tools.retriever import retriever_tool

class Bar(BaseModel):
    bar_name: str = Field(description="Name of the bar")
    heigth: int = Field(description="Heigth of the bar. This would be the number of votes")

class Graph(BaseModel):
    x_label: str = Field(description="The X-axis name of the graph")
    y_label: str = Field(description="The Y-axis name of the graph")
    bars: List[Bar]


class Answer(BaseModel):
    answer: str = Field(description="Helpful answer")
    graph: Optional[Graph] = Field(description="Helpful bar-graph only if applicable/possible, otherwise leave it as default value", default=None)


parser = JsonOutputParser(pydantic_object=Answer)

tools = [retriever_tool, get_district_result]
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate(prompt=PromptTemplate(template="You are a helpful assistant for election commission of Sri Lanka.")),
    MessagesPlaceholder(variable_name='chat_history', optional=True),
    HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], partial_variables={"format_instructions": parser.get_format_instructions()}, template='\n{format_instructions}\n{input}\n')),
    MessagesPlaceholder(variable_name='agent_scratchpad')
])

agent = create_tool_calling_agent(llm, tools, prompt)

def toString(x):
    return x['output']

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) | toString | parser

