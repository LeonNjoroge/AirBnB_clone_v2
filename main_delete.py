#!/usr/bin/python3

"""
Tests delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

file_stg = FileStorage()

# All States
all_states = file_stg.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Mkaes a new State
new_state = State()
new_state.name = "California"

file_stg.new(new_state)
file_stg.save()
print("New State: {}".format(new_state))

# All States
all_states = file_stg.all(State)
print("All States: {}".format(len(all_states.keys())))

for state_key in all_states.keys():
    print(all_states[state_key])

# Makes another State
another_state = State()
another_state.name = "Nevada"
file_stg.new(another_state)
file_stg.save()
print("Another State: {}".format(another_state))

# All States
all_states = file_stg.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Deletes the new State
file_stg.delete(new_state)

# All States
all_states = file_stg.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
