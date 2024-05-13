
from tools.tools import get_profile_url_tavily
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub


def lookup(name:str) -> str:
    load_dotenv()
    """
    Given the name of a person, return the linkedin information about the person
    """
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """Given the full name {name_of_person} of a person, I want you to find the link to their linkedin profile page. Your answer should contain only a URL"""
    
    prompt_template = PromptTemplate(input_variables=["name_of_person"], template=template)
    
    tools_for_agent = [
        Tool(name="Crawl Google 4 linkedin profile page", 
             func=get_profile_url_tavily, 
             description="useful for when uou need to get the linkedin page URL")
        ]
    
    
    react_prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})
    
    linkedin_profile_url = result["output"]
    
    return linkedin_profile_url

if __name__ == '__main__':
    linkdin_url = lookup("papa kobina Kwegyir-Aggrey Waterloo")
    print(linkdin_url)
    