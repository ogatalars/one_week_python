todos = []
while True:
    for i in range(len(todos)):
        print(f"* {i + 1} {todos[i]}")
    print("**********************")
    print("Enter a comand. Type h for help: ")
    command = input("> ")
    if command == 'q':
        break
    elif command.isnumeric():
        idx= int(command) - 1
        if idx >= len(todos):
            print('Invalido index')
        else:    
            todos.pop(idx)
    else:
        todos.append(command)
print('Ok Goodbye')    