from langchain_core.prompts import PromptTemplate
from config.llm_config import get_llm

llm = get_llm()

prompt = PromptTemplate(
    input_variables=["task"],
    template="""
    You are an AI planner.

    Break the following task into steps.

    Task: {task}

    Provide numbered steps.
    """
)

chain = prompt | llm

def planner_agent(task):
    result = chain.invoke({"task": task})
    return result