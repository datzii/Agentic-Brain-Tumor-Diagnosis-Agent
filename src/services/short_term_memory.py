import json

dict_states = {}


def save_state(chat_id: str, state):
    saved_state = json.dumps(state)
    dict_states[chat_id]=saved_state
    #print('-- saved states',dict_states)

def get_state(chat_id: str):
    state = json.loads(dict_states[chat_id])
    #print('loaded ', state)
    return state

def check_state_exists(chat_id: str) -> bool:
    #print('checking')
    return chat_id in dict_states.keys()

def delete_state(chat_id: str):
    try:
        del dict_states[chat_id]
    
    except Exception as err:
        return ''