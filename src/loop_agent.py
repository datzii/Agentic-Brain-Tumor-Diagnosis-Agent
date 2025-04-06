
from services.agents import create_agent, make_agent_query

create_agent()

while True:
    print('------------------------ USER ------------------------\n>> ', end='')
    prompt = input()
    print('---------------------- AI AGENT ----------------------')
    response = make_agent_query('hola', prompt, '')
    print('<<', response)
    if 'BYE' in prompt:
        break