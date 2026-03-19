from Agents.planner_agent import planner_agent
from Agents.writer_agent import writer_agent
from Agents.critic_agent import critic_agent


def run_system(topic: str):
    """
    Orchestrator function that controls full agent workflow
    """
    plan = planner_agent(topic)
    draft = writer_agent(plan, topic)
    final = critic_agent(draft)

    return {
        "topic": topic,
        "plan": plan.content if hasattr(plan, "content") else str(plan),
        "report": final.content if hasattr(final, "content") else str(final)
    }