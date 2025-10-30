
# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent

# Load environment variables from .env file
load_dotenv(".env")

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor"

knowledge = "You know everything about Texas"
# TODO: 2 - Define the Texas Knowledge Augmented Prompt Agent
texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

knowledge = "You know everything about Europe"
# TODO: 3 - Define the Europe Knowledge Augmented Prompt Agent
europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge )

persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
# TODO: 4 - Define the Math Knowledge Augmented Prompt Agent
math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge )


agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x) # TODO: 5 - Call the Texas Agent to respond to prompts
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x) # TODO: 6 - Define a function to call the Europe Agent
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        # TODO: 7 - Define a function to call the Math Agent
        "func": lambda x: math_agent.respond(x)
    }
]
routing_agent = RoutingAgent(openai_api_key, agents)
#routing_agent.agents = agents

# TODO: 8 - Print the RoutingAgent responses to the following prompts:
texas_prompt =  "Tell me about the history of Rome, Texas"

print(f"\nTexas Prompt:\n{texas_prompt}\n")
resp = routing_agent.route_user(texas_prompt)
print(f"\nResponse:\n{resp}\n")

europe_prompt =  "Tell me about the history of Rome, Italy"
print(f"\nEurope Prompt:\n{europe_prompt}\n")
resp = routing_agent.route_user(europe_prompt)
print(f"\nResponse:\n{resp}\n")
#print(resp)

math_prompt =  "One story takes 2 days, and there are 20 stories"
print(f"\nMath Prompt:\n{math_prompt}\n")
resp = routing_agent.route_user(math_prompt)
print(f"\nResponse:\n{resp}\n")

#print(resp)

