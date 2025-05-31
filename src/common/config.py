import os

MCP_SERVER = os.environ.get('MCP_SERVER', 'http://localhost:7600')
mcp_sse_url = f'{MCP_SERVER}/sse'

PORT = os.environ.get('PORT', '5700')

# LiteLLM variables
LITELLM_ENDPOINT = os.environ.get('LITELLM_ENDPOINT', 'http://localhost:4000')
LITELLM_APIKEY = os.environ.get('LITELLM_APIKEY', 'sk-1234')