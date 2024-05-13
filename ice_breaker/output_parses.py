from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    Summary: str = Field(description="A summary of the person's linkedin profile")
    facts: List[str] = Field(description="Interesting facts about the person")
    ice_breaker: str = Field(description="A one sentence Funny Potential Ice breakers when meeting the person for the first time")
    topics_of_interest: List[str] = Field(description="2 Topics of Interest of that person")

    
    
    def to_dict(self) -> Dict[str, Any]:
        return {"Summary": self.Summary, "facts": self.facts, "ice_breaker": self.ice_breaker, "topics_of_interest": self.topics_of_interest}
    
    

summary_parser = PydanticOutputParser(pydantic_object=Summary)# Path: ice_breaker/ice_breaker.py