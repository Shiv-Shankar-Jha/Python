import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Todo App")
st.subheader("Monetize your tasks.")
st.write("This will help you organize and prioritize your tasks effectively.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add a new todo:", placeholder="Enter todo here...",
              on_change=add_todo, key='new_todo')
