import json

dict_states = {}

# Saves context
def save_state(chat_id: str, state):
    saved_state = json.dumps(state)
    dict_states[chat_id]=saved_state
    #print('-- saved states',dict_states)

# Recovers context
def get_state(chat_id: str):
    state = json.loads(dict_states[chat_id])
    #print('loaded ', state)
    return state

# Checks if context exists
def check_state_exists(chat_id: str) -> bool:
    #print('checking')
    return chat_id in dict_states.keys()

# Deletes context
def delete_state(chat_id: str):
    try:
        del dict_states[chat_id]
    
    except Exception as err:
        return ''