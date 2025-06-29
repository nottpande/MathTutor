from a2a.types import AgentCard, AgentSkill, AgentCapabilities

simplify_skill = AgentSkill(
    id="simplify_explanation",
    name="Simplify Explanation",
    description="Simplifies a math explanation for better understanding.",
    tags=["math", "teaching", "simplification"],
    examples=[
        "Simplify: 'To solve x+2=5, we subtract 2 from both sides.'",
        "Simplify: 'Differentiate x^2 to get 2x.'"
    ],
)

agent_card = AgentCard(
    name="Teaching Agent",
    description="Simplifies explanations generated by a reasoning agent.",
    url="http://localhost:9001",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=False),
    skills=[simplify_skill],
)
