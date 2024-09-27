class TasksModel:
    def __init__(self):
        self.tasks = [{'name': 'поспать', 'status': 'в ожидании'}]

    def get_tasks(self):
        return self.tasks

    def add_tasks(self, name):
        task = {'name': name, 'status': 'в ожидании'}
        self.tasks.append((task))

    def complete_task(self, task_number):
        self.tasks[task_number]['status'] = 'Выполнено'

class View:
    @staticmethod
    def show_all_tasks(tasks):
        for number, task in enumerate(tasks, 1):
            print(f"{number}. {task['name']} : {task['status']}")

    @staticmethod
    def show_add_task():
        return input('Введите название задачи')

    @staticmethod
    def show_complete_task():
        return int(input('Введите номер задачи'))


class Controller:
    """класс для бизнес логики."""

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_tasks(self):
        """Добавлени задачи"""
        tasks = self.model.get_tasks()
        self.view.show_all_tasks(tasks)
        task_name = self.view.show_add_task()
        self.model.add_tasks(task_name)
        self.view.show_all_tasks(tasks)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_all_tasks(tasks)

    def complete_task(self):
        task_number = self.view.show_complete_task()
        task_number -= 1
        self.model.complete_task(task_number)


model = TasksModel()
view = View()
controller = Controller(view, model)

while True:
    print('1 - добавить задачу')
    print('2 - выполнить задачу')
    print('3 - посмотреть список задач')
    print('4 - выйти')
    choice = input('Что ты хочешь сделать?')

    if choice == '1':
        controller.add_tasks()
    elif choice == '2':
        controller.complete_task()
    elif choice == '3':
        print('вот ваши задачи')
        controller.show_tasks()
    elif choice == '4':
        print('До свидания!')
        break