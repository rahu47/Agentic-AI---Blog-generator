from src.states.blogstate import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blogstate import Blog
class BlogNode:

    def __init__(self,llm):
        self.llm=llm


    def title_creation(self,state:BlogState):

        if 'topic' in state and state['topic']:
            prompt="""

                    you are a expert blog content writer .User Markdown formatting. Generate a blog title for the {topic}.This title should be creative and SEO freindly"""


            system_message=prompt.format(topic=state['topic'])
            response=self.llm.invoke(system_message)
            return {'blog':{'title':response.content}}
        
    
    def content_generation(self,state:BlogState):
        system_prompt="""

                    you are a expert blog writer .User Markdown formatting. Generate a detailed blog contentwith detailed breakdown for the {topic}.This title should be creative and SEO freindly"""
        
        system_message=system_prompt.format(topic=state['topic'])
        response=self.llm.invoke(system_message)     
        return {'blog':{'title':state['blog']['title'],'content':response.content}}
    

    def translation(self,state:BlogState):
        translation_prompt="""
        Translate the following content into {current_language}.
        - Maintain the original tone , style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}

         """
        
        blog_content=state['blog']['content']
        messages=[
            HumanMessage(translation_prompt.format(current_language=state['current_language'],blog_content=blog_content))
        ]

        translation_content=self.llm.with_structured_output(Blog).invoke(messages)

    def route(self,state: BlogState):
            return {'current_language': state['current_language']}
        
    def route_decision(self,state: BlogState):

            if state['current_language']== 'hindi':
                return 'hindi'
            
            elif state['current_language']=='french':
                return 'french'
            
            else:
                return state['current_language']



        

