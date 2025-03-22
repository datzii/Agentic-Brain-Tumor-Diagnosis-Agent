import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from services.tools import classify_brain_tumor_from_MRI
from services.short_term_memory import delete_state, save_state, get_state, check_state_exists

def create_agent():
    model_client = OpenAIChatCompletionClient(
        model="qwen2.5:7b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
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
        tools=[classify_brain_tumor_from_MRI],
        system_message="You are a doctor agent expert in brain tumor diagnosis. You are able to maintain a normal conversation but also to perform a first brain diagnosis. Your task is to use the tool provided to diagnose the brain status of the patient. Use your tool to make a diagnosis given a filepath. \nIMPORTANT:\n You can only answer in english.",
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


def make_agent_query(chat_id: str, input: str, image_path: str) -> str:
    create_agent()
    query = create_query(input, image_path)
    print(query)
    result = asyncio.run(execute_assitant_query(chat_id, query))  # Run the async function
    return result


def create_query(input: str, image_path: str) -> str:
    if image_path != '':
        return input + '\nThe MRI image in located in ' + image_path
    
    return input
