import streamlit as st
import functions

todos = functions.fetch_todo()

def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_todo(todos)
    st.session_state['new_todo'] = ''

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
