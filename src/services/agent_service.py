import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from services.tool_service import get_diagnosis_tool
from services.short_term_memory import delete_state, save_state, get_state, check_state_exists
from common.config import LITELLM_ENDPOINT, LITELLM_APIKEY
from services.tool_service import get_diagnosis_tool

def create_agent(engine: str):    
    
    model_client = OpenAIChatCompletionClient(
        model=engine,
        base_url=LITELLM_ENDPOINT,
        api_key=LITELLM_APIKEY,
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": "unknown",
        },
    )

    global agent

    agent = AssistantAgent(
        name="assistant",
        model_client=model_client,
        tools=get_diagnosis_tool(),
        system_message="You are a ReAct (Reasoning + Act) agent that will receive a request.\n" \
        "You have to decide if the request is just a simple chatting (Type Chatting) or if the request is related to a realize a brain tumor diagnosis. (Type Diagnosis) \n" \
        "If the request is of Type Chatting, you just need to answer the request\n"
        "If the request is of Type Diagnosis, then you become an expert in brain tumor analysis. In that case, your task is to give the diagnosis of the brain MRI Image to the pacient. You have the 'classify_brain_tumor_from_MRI' tool available to use. Don't refer in your answer about the directory of the image.\n" \
        "**IMPORTANT:** You can only answer in english.\n" \
        "**OUTPUT FORMAT**: You have to first provide the reasoning process you have gone through before deciding what to do, and then return your answer, in the following structure:\n" \
        "Reasoning: \n Your reasoning process \n" \
        "Answer: \n Your answer",
        reflect_on_tool_use=True
    )


async def execute_assitant_query(chat_id: str, input: str) -> str:
    global agent

    if check_state_exists(chat_id):
        await agent.load_state(get_state(chat_id))

    response = await agent.on_messages(
        [TextMessage(content=input, source="user")],
        cancellation_token=CancellationToken(),
    )

    state = await agent.save_state()
    save_state(chat_id, state)

    #print(response.inner_messages)
    #print(f"-- result {response.chat_message}")
    #print(f"-- result {response.chat_message.content}")
    return response.chat_message.content

file_path = '/mnt/c/Users/Usuario/Desktop/MASTER/TFM/cleaned/Testing/images/Te-no_0012.jpg'
input = "Can you tell me if I have brain cancer? I am not feeling well and I want to be sure if anything is wrong with me. The MRI image of my brain is located in " + file_path


def make_agent_query(chat_id: str, input: str, image_path: str, engine: str) -> str:
    create_agent(engine)
    query = create_query(input, image_path)
    #print(query)
    result = asyncio.run(execute_assitant_query(chat_id, query))  # Run the async function
    return result


def create_query(input: str, image_path: str) -> str:
    if image_path != '':
        return input + '\nThe MRI image in located in ' + image_path
    
    return input
