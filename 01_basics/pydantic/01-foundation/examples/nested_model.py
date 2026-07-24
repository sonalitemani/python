from pydantic import BaseModel
from typing import List

class Lesson(BaseModel):
    id:int,
    topic:str,
    
class Module(BaseModel):
    id:int,
    topic:str,
    lessons:List[Lesson]

class Course(BaseModel):
    id:int,
    name:str,
    modules:List[Module]

class Comment(BaseModel):
    id:int,
    user:str,
    content:str,
    replies:List[Comment]

    Comment.model_rebuild()