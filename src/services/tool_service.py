import asyncer
from autogen_ext.tools.mcp import mcp_server_tools, SseMcpToolAdapter, SseServerParams
from autogen_ext.tools.mcp import _session
from mcp import ClientSession
from mcp.client.sse import sse_client
import mcp.types as types
from typing_extensions import Self
import common.config as config

# List of MCP tools
activated_tools_mcp = []


class AgntticSseMcpToolAdapter(SseMcpToolAdapter):

  @classmethod
  async def from_server_params_list_tools(
    cls, server_params: SseServerParams
  ) -> list[Self]:
      """
      Create an instances of AgntticSseMcpToolAdapter from server parameters.

      Args:
          server_params (ServerParams): Parameters for the MCP server connection.

      Returns:
          list[AgntticSseMcpToolAdapter]: An instances of AgntticSseMcpToolAdapter.
      """
      response = []

      async with sse_client(**server_params.model_dump()) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
          await session.initialize()

          tools_response = await session.list_tools()
          
          for t in tools_response.tools:
            tool_adapter = cls(server_params=server_params, tool=t)
            response.append(tool_adapter)

      return response

  def __str__(cls):
    return cls._tool.__str__()

# Starts the MCP server connection
def init_mcp_server():
  print('innnit mcp')
  asyncer.runnify(_init_mcp_server)()


async def _init_mcp_server():
  """call MCP server and get tools"""
  print('- innnit mcp server')

  # Create server params for the remote MCP service
  server_params = SseServerParams(
      url=config.mcp_sse_url,
      # headers={"Authorization": "Bearer your-api-key", "Content-Type": "application/json"},
      headers={"Content-Type": "application/json"},
      timeout=30,  # Connection timeout in seconds
  )
 
  adapter = await AgntticSseMcpToolAdapter.from_server_params_list_tools(server_params=server_params)
  print(f'{" -> ".join(map(str, adapter))}')

  global activated_tools_mcp
  activated_tools_mcp = adapter


# Gets the diagnosis tool
def get_diagnosis_tool():
    for tool in activated_tools_mcp:
        if tool.name == 'classify_brain_tumor_from_MRI':
            return [tool]
    return []


