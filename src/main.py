
from services.agents import create_agent, make_agent_query


if __name__ == "__main__":

    create_agent()

    while True:
        print('------------------------ USER ------------------------\n>> ', end='')
        prompt = input()
        print('---------------------- AI AGENT ----------------------')
        response = make_agent_query(prompt)
        print('<<', response)
        if 'BYE' in prompt:
            break