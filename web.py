import streamlit as st
import func20app

todos = func20app.read_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    func20app.write_todos(todos)


st.title("My Todo App")
st.subheader("This is a my todo app.")
st.write("This app helps to increase your productivity.")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func20app.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')