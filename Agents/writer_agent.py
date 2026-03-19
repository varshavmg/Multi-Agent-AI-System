from config.llm_config import get_llm

llm = get_llm()

def writer_agent(context, topic):

    prompt = f"""
    Using the following context write a detailed report.

    Topic: {topic}

    Context:
    {context}

    Write structured report.
    """

    response = llm.invoke(prompt)

    return response