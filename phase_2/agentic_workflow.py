# agentic_workflow.py

# TODO: 1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module

import os
import re
from time import sleep
from dotenv import load_dotenv
from workflow_agents.base_agents import (ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent)

load_dotenv(".env")
# TODO: 2 - Load the OpenAI key into a variable called openai_api_key
openai_api_key = os.getenv("OPENAI_API_KEY")

# load the product spec
# TODO: 3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec

product_spec = """Product Specification Document
Email Router
1. Introduction
1.1 Business Overview
Our organization handles a high volume of incoming email communications that require timely, accurate responses across multiple departments. Currently, manual email triage and routing creates bottlenecks, delays customer responses, and consumes valuable staff time that could be directed toward higher-value activities.
Team members spend significant portions of their workday sorting through emails, determining appropriate handlers, and forwarding messages—a process that introduces inconsistency in response quality and timing. Subject matter experts often receive misdirected inquiries, while routine questions that could be automated consume unnecessary attention.
The introduction of the Email Router system addresses these operational challenges by implementing AI-powered email analysis and routing. This solution will integrate with our existing email infrastructure to automatically categorize incoming messages, generate responses for routine inquiries, and intelligently route complex communications to the appropriate subject matter experts.
By implementing this system, we aim to reduce response times, ensure consistent communication quality, and free our team members to focus on specialized tasks requiring human expertise rather than email management.
1.2 Problem Statement
Our organization is struggling with inefficient email management processes that negatively impact operational performance and customer satisfaction. The current manual approach to email triage and routing presents several critical challenges:
Significant time delays occur between receipt and response as emails pass through multiple hands before reaching the appropriate subject matter expert.
Staff members across departments spend excessive time sorting, categorizing, and forwarding emails, diverting resources from high-value work requiring specialized expertise.
Inconsistent handling of similar inquiries results in variable response quality and contradictory information being provided to customers and partners.
Important emails may be overlooked in high-volume periods, leading to missed opportunities or unaddressed critical issues.
The organization lacks visibility into email traffic patterns that could inform staffing decisions and process improvements.
Routine, repetitive inquiries that could be automated consume disproportionate staff attention and resources.
Without an automated solution to streamline email classification and routing, these inefficiencies will continue to create operational bottlenecks, increase response times, and potentially damage our reputation for customer service excellence.
1.3 Current Process
The existing email management process in our organization follows a largely manual workflow that involves multiple touchpoints and handoffs:
Incoming emails arrive at general departmental inboxes (e.g., info@company.com, support@company.com) or to specific team members.
Administrative staff or designated team members manually open, read, and make initial assessments of each email to determine its priority and appropriate handler.
For routine inquiries, staff members search for relevant information across various knowledge bases, documentation, or by consulting colleagues before drafting responses.
More complex or specialized inquiries require forwarding to subject matter experts (SMEs), often involving multiple transfers before reaching the appropriate person.
SMEs must review each email, including the chain of previous communications, to understand the context before responding.
Responses are drafted individually, with limited standardization or templates, leading to inconsistent messaging and varying quality.
Follow-up tracking is managed through ad-hoc methods such as flagging emails, creating calendar reminders, or maintaining separate spreadsheets.
Performance metrics and response time data are collected manually, if at all, providing little insight into operational efficiency or areas for improvement.
During peak periods or staff absences, backlogs develop quickly with no automated prioritization system to ensure critical communications receive prompt attention.
Cross-departmental inquiries often bounce between teams with unclear ownership, further delaying resolution and creating customer frustration.
This labor-intensive process creates significant inefficiencies, delays customer communication, and represents a substantial opportunity cost as skilled staff members devote time to email management rather than applying their expertise to core business functions.
1.4 Scope
The Email Router project encompasses the development, deployment, and integration of an AI-powered email management system that will:
Interface with our existing email infrastructure to capture and process all incoming external communications.
Analyze email content using natural language processing to determine intent, urgency, and required expertise.
Automatically generate responses for routine, standard inquiries based on approved organizational knowledge.
Route complex inquiries to appropriate subject matter experts based on content analysis and defined business rules.
Provide a management dashboard for monitoring system performance, workflow bottlenecks, and response metrics.
Include tools for continuous improvement through feedback loops and model training.

The project scope specifically excludes:
Modifications to existing backend email servers
Processing of internal employee-to-employee communications
Integration with CRM systems (planned for future phase)
Mobile application development (web interface only in initial release)

1.5 Objectives

Primary Objectives
Reduce Response Time: Decrease average email response time by 60% within three months of full implementation.
Increase Efficiency: Automate responses to at least 40% of incoming emails that contain routine inquiries.
Improve Routing Accuracy: Achieve 90% accuracy in routing emails to appropriate subject matter experts by the end of the pilot phase.
Enhance Consistency: Standardize responses to common inquiries to ensure consistent messaging and information delivery.
Liberate Staff Resources: Reduce time spent by SMEs and administrative staff on email triage by 70%, allowing reallocation to higher-value activities.
Secondary Objectives
Generate Insights: Develop analytics capabilities to identify communication trends, common customer pain points, and potential service improvements.
Increase Scalability: Create a solution that can accommodate 200% growth in email volume without proportional increases in staffing.
Improve Customer Satisfaction: Achieve a 30% improvement in customer satisfaction metrics related to communication responsiveness.
Support Knowledge Management: Identify gaps in current knowledge base through analysis of inquiries that cannot be automatically answered.
Enhance Compliance: Ensure all communications adhere to organizational standards and regulatory requirements through consistent handling.


2. Product Overview
2.1 Product Features
Email Ingestion System
Seamless integration with email services via SMTP, IMAP, and RESTful APIs.
Real-time email retrieval and preprocessing to extract relevant metadata and content.
Message Classification Module
Utilization of LLM-based classifiers to analyze email content and determine intent and category.
Assignment of confidence scores to decide between automated responses and manual handling.
Knowledge Base Integration
Implementation of a vector database for efficient storage and retrieval of organizational knowledge.
Continuous learning mechanism to update the knowledge base with new information from resolved inquiries.
Response Generation Engine
Deployment of a RAG system to generate contextually accurate and human-like responses.
Incorporation of an approval workflow for reviewing and editing automated responses before dispatch.
Routing Logic
Development of a rules-based engine to assign emails to appropriate SMEs based on content analysis.
Context-aware forwarding that includes relevant metadata and previous correspondence history.
User Interface
Creation of a comprehensive dashboard for monitoring system performance, including metrics on response times and accuracy.
Provision of a configuration panel for managing the knowledge base, routing rules, and system settings.
Implementation of manual override options to allow human intervention when necessary.
2.2 User Classes and Characteristics
Customer Support Representatives: Will benefit from reduced workload on routine inquiries, allowing focus on complex issues.
Subject Matter Experts (SMEs): Will receive only relevant, complex inquiries, improving efficiency and job satisfaction.
IT Administrators: Responsible for system configuration, maintenance, and monitoring performance metrics.
2.3 Operating Environment
The Email Router will operate within the organization's existing IT infrastructure, integrating with standard email services and databases. It will be deployed on secure servers, adhering to the organization's data protection and privacy policies.
2.4 Constraints
Data Privacy: Compliance with data protection regulations is mandatory, ensuring that sensitive information is handled appropriately.
Integration: The system must seamlessly integrate with existing email platforms without requiring significant changes to current workflows.
Scalability: The architecture should support scaling to accommodate increasing email volumes as the organization grows.
3. Functional Requirements
Email Ingestion
The system shall connect to designated email services to retrieve incoming messages in real-time.
The system shall preprocess emails to extract metadata such as sender, recipient, subject, and timestamp.
Message Classification
The system shall analyze email content to determine intent and category using LLM-based models.
The system shall assign a confidence score to each classification to guide subsequent actions.
Knowledge Base Retrieval
The system shall search the knowledge base for relevant information corresponding to the classified intent.
The system shall update the knowledge base with new information from resolved inquiries.
Response Generation
The system shall generate draft responses for routine inquiries using the RAG system.
The system shall provide an interface for human review and approval of generated responses.
Email Routing
The system shall forward complex or high-confidence emails to the appropriate SME based on predefined rules.
The system shall include relevant context and metadata when routing emails to SMEs.
User Interface
The system shall provide a dashboard displaying performance metrics such as response times and accuracy.
The system shall offer configuration options for managing the knowledge base, routing rules, and system settings.
The system shall allow manual intervention to override automated processes when necessary.
4. Non-Functional Requirements
Performance: The system shall process and classify incoming emails within 5 seconds of receipt.
Reliability: The system shall maintain 99.9% uptime, ensuring continuous email processing capabilities.
Scalability: The system shall handle a minimum of 10,000 emails per hour without degradation in performance.
Security: 
Data Encryption: All emails, including stored and transmitted data, shall be encrypted using AES-256 encryption. TLS 1.2 or higher shall be used for secure communication between the Email Router and external email services.
Access Control: Role-Based Access Control (RBAC) shall be implemented to restrict system access based on user roles. Multi-Factor Authentication (MFA) shall be required for administrative access.
Data Privacy and Compliance: The system shall comply with GDPR, CCPA, and other relevant data protection regulations.
Personally Identifiable Information (PII) shall be anonymized or masked before processing when required.
"""

filename = "./Product-Spec-Email-Router.txt"

def read_product_spec():
    try:
        with open(filename, 'r') as file:
            product_spec = file.read()
            #print(product_spec)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#print("Reading Product spec")
#read_product_spec()

# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'

action_planning_agent = ActionPlanningAgent(openai_api_key, knowledge_action_planning)

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product.\n "
    # TODO: 5 - Complete this knowledge string by appending the product_spec loaded in TODO 3
    f"{product_spec}"
)
# TODO: 6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'

#print(f"Product manager knowlwdge \n {knowledge_product_manager}")

product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_product_manager, knowledge_product_manager)

# Product Manager - Evaluation Agent
# TODO: 7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
# The evaluation_criteria should specify the expected structure for user stories (e.g., "As a [type of user], I want [an action or feature] so that [benefit/value].").
persona_product_eval = "You are an evaluation agent that checks the answers of other worker agents."
product_eval_criteria = (
    "User sroties should have the following structure:"
    "As a [type of user], I want [an action or feature] so that [benefit/value]."
)
product_eval_agent = EvaluationAgent(openai_api_key, persona_product_eval, product_eval_criteria, product_manager_knowledge_agent, 10)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_program_manager, knowledge_program_manager)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."

# TODO: 8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.

persona_program_manager_eval = (
    "The answer should be product features that follow the following structure: "
    "Feature Name: A clear, concise title that identifies the capability\n"
    "Description: A brief explanation of what the feature does and its purpose\n"
    "Key Functionality: The specific capabilities or actions the feature provides\n"
     "User Benefit: How this feature creates value for the user"
)
program_manager_evaluation_agent = EvaluationAgent(openai_api_key, persona_program_manager_eval, persona_program_manager_eval, program_manager_knowledge_agent, 10)

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)

development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_dev_engineer, knowledge_dev_engineer)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
persona_dev_engineer_eval = (
    "The answer should be tasks following this exact structure: "
    "Task ID: A unique identifier for tracking purposes\n"
    "Task Title: Brief description of the specific development work\n"
    "Related User Story: Reference to the parent user story\n"
    "Description: Detailed explanation of the technical work required\n"
    "Acceptance Criteria: Specific requirements that must be met for completion\n"
    "Estimated Effort: Time or complexity estimation\n"
    "Dependencies: Any tasks that must be completed first"
)

# Routing Agent
# TODO: 10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.

agents = [
    {
        "name": "Product Manager",
        "description": "Responsible for defining product personas and user stories only. Does not define features or tasks. Does not group stories.",
        "func": lambda x: product_manager_knowledge_agent.respond(x) # TODO: 5 - Call the Product Manager to respond to prompts
    },
    {
        "name": "Program Manager",
        "description": "Responsible for defining the features for a product. Does not define strories or tasks.",
        "func": lambda x: program_manager_knowledge_agent.respond(x) # TODO: 6 - Call the Product Manager to respond to prompts
    },
    {
        "name": "Development Engineer",
        "description": "Responsible for defining the development tasks for a product. Does not define stories or features. Does not group stories",
        "func": lambda x: development_engineer_knowledge_agent.respond(x)
    }
]

routing_agent = RoutingAgent(openai_api_key, agents)


# Job function persona support functions
# TODO: 11 - Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.



# Run the workflow


print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
workflow_prompt = f"What would the development tasks for this product be? : {product_spec}"
# ****
#print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).

completed_steps = []

steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt )

for step in steps:
    print(step)

cur_prompt = []
for index, step in enumerate(steps):
    #print(index, step)


    if len(step) > 0:
        step_clean = re.sub(r"^[^a-zA-Z]+", " ", step)
        if step[0].isdigit():
            if len(cur_prompt) > 0:
                cur_step = "".join(cur_prompt)
                print(f"\n***Executing step:***\n\n {cur_step}")
                tasks = routing_agent.route_user(cur_step)
                print(f"\n***Tasks:***\n\n {tasks}")
                cur_prompt = []
                cur_prompt.append(step_clean)
            else:
                cur_prompt.append(step_clean)        
        else:
            cur_prompt.append(step_clean)

    #print(f"Executing step {indx}:\n{step}")
    #sleep(1)
    step_clean = re.sub(r"^[^a-zA-Z]+", "", step)
    #print(f"{task_new}\n")
    #step_compl = routing_agent.route_user(step_clean)
    #print(f"Result: \n{task}")
    #completed_steps = completed_steps.append(step_compl)

#for index, entity in enumerate(completed_steps):
# #    print(f"Step {index} tasks: \n {entity}\n")