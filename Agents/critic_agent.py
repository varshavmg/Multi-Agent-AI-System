from config.llm_config import get_llm

llm = get_llm()

def critic_agent(report):

    prompt = f"""
    You are an expert reviewer.

    Review the following report.

    Improve clarity, structure and grammar.

    Report:
    {report}
    """

    result = llm.invoke(prompt)

    return result