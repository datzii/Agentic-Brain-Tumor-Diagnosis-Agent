from services.agent_service import create_agent, make_agent_query
from services.tool_service import init_mcp_server
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

try:
    init_mcp_server()
except Exception as err:
    print(f'Error connecting to MCP Server - {err}')

while True:
    print('------------------------------------ USER ------------------------------------\n>> ', end='')
    prompt = input()
    print('---------------------------------- AI AGENT ----------------------------------')
    response = make_agent_query('1234', prompt, '', 'qwen2.5')
    print('<<', response)
    if 'BYE' in prompt:
        break