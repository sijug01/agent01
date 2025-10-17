# TODO: 1 - Import the AugmentedPromptAgent class
import os
from dotenv import load_dotenv
from openai import OpenAI
from workflow_agents.base_agents import AugmentedPromptAgent

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = "voc-1005963941159874436462368c0af5b6c4317.26188318"

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters

aug_agent = AugmentedPromptAgent(openai_api_key, persona)

# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'

augmented_agent_response = aug_agent.respond(prompt)



# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# The agent used the knowledge from the Web that the capital of the country, France is Paris.
# - How the system prompt specifying the persona affected the agent's response.
# The persona made the agent to aswer the question as a professor answering students' questions. 

print(f"\nPrompt: {prompt}\n")
print("Response:\n")
# Print the agent's response
print(augmented_agent_response)