Filepath = 'todos.txt'

def read_todos(filepath=Filepath):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_go_here,filepath=Filepath):
    with open(filepath,'w') as file:
        file.writelines(todos_go_here)