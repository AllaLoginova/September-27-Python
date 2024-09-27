# паттерн MVC
tasks = [{'name': 'поспать', 'status': 'в ожидании'}]

def add_task(name):
    task = {'name': name, 'status': 'в ожидании'}
    tasks.append(task)

def complete_tasks(task_num):
    """выполнение задачи"""
    if len(tasks) >= task_num:
        task = tasks[task_num]
        task['status'] = 'Выполнена'

def show_tasks():
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task['name']} : {task['status']}")

while True:
    print('1 - добавить задачу')
    print('2 - выполнить задачу')
    print('3 - посмотреть список задач')
    print('4 - выйти')
    choice = input('Что ты хочешь сделать?')

    if choice == '1':
        show_tasks()
        name = input('Название задачи')
        add_task(name)
        show_tasks()
    elif choice == '2':
        show_tasks()
        task_num = int(input('введи номер задачи'))
        task_num -= 1
        complete_tasks(task_num)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print('До свидания!')
        break

