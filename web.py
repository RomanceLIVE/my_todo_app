import streamlit as st
import final_functions as functions
#import the backend

todos = functions.get_todos()
# we put this above to use before we define function below

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

# st.session_state is a dictionary format object like "{'new_todo':"Clean"}"

st.title("My Todo App")
st.subheader("Your tasks to finish.")
st.write("An app to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index) #pop removes the item
        functions.write_todos(todos)
        del st.session_state[todo] #deletes item from the session bellow on web
        st.experimental_rerun() #reruns the code


# each generated checkbox will have same key if for exp key="task",
# it will duplicate with new task,
# reason why we will put key=todo to make unique keys for each task

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo") #on_change is a callback function
                                    # key identifies a widget

# st.session_state
# we delete this when we finish to develop the app
# we use this to check values when we develop the app,
# like todos having true values when checked on the box to make a conditional statement


