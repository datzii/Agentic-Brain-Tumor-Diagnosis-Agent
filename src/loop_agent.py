from services.agents import create_agent, make_agent_query


while True:
    print('------------------------ USER ------------------------\n>> ', end='')
    prompt = input()
    print('---------------------- AI AGENT ----------------------')
    response = make_agent_query('1234', prompt, '', 'qwen2.5')
    print('<<', response)
    if 'BYE' in prompt:
        break