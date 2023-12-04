import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    todo ="\n" + st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my to-do app")
st.text("This app is used to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo....",
              on_change=add_todo, key='new_todo')
