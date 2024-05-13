import os
from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.Linkedin import scrape_linkedin_profile as sc
from agents.linkedin_loopup_agents import lookup as linkedin_lookup_agent
from output_parses import summary_parser, Summary


def ice_break_with(name:str) -> Tuple[Summary, str]:
    """
    Given the name of a person, I want you to find the link to their linkedin profile page. Your answer should contain only a URL
    """
    linkedin_username = linkedin_lookup_agent(name)
    linkedin_data = sc(linkedin_username, True)
    
    summary_template = """
    given the Linkedin information {information} about a person I want you to Create:
    1. A short summary 
    2. Two interesting facts about the person
    3. A one sentence Funny Potential Ice breakers when meeting the person for the first time
    4. 2 Topics of Interest of that person
    \n{format_instructions}
    """
        
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template, 
        partial_variables={"format_instructions": summary_parser.get_format_instructions()
    })
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    
    chain = summary_prompt_template | llm | summary_parser

    res:Summary = chain.invoke(input={"information": linkedin_data})
    return res, linkedin_data.get("profile_pic_url")




if __name__ == '__main__':
    load_dotenv()
    print('Ice breaker Enter')
    
    ice_break_with("papa kobina Kwegyir-Aggrey Waterloo")
