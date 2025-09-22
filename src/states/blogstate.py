from typing import TypedDict
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str=Field(description='The Title of theblog post')
    content:str=Field(description='The main content of blog post')

class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str