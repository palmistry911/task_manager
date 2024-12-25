import json


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        if len(task.strip()) < 2:
            raise ValueError("Задача должна содержать хотя бы 2 символа")
        self.tasks.append({"title": task.strip(), "completed": False})
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("Список задача пуст.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{idx}. {status} {task['title']}")

    def mark_completed(self, index):
        if index < 1 or index > len(self.tasks):
            raise IndexError("Неверный номер задачи.")
        if self.tasks[index - 1]["completed"]:
            raise ValueError("Задача уже отмечена как выполненная ")
        self.tasks[index - 1]["completed"] = True
        self.save_tasks()

    def delete_task(self, index):
        if index < 1 or index > len(self.tasks):
            raise IndexError("Неверный номер задачи")
        del self.tasks[index - 1]
        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []


def main():
    manager = TaskManager()
    print("Добро пожаловать в Планировщик задач. Для начала программы выберете нужную цифру из списка")
    while True:
        print("1.Добавить задачу")
        print("2.Показать задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выход")
        choice = input("Впишите нужную цифру команды: ")

        try:
            if choice == "1":
                task = input("Введите задачу:")
                manager.add_task(task)
                print("Задача добавлена!")
            elif choice == "2":
                print("Ваши задачи:")
                manager.list_tasks()
            elif choice == "3":
                index = int(input("Введите номер задачи для выполнения: "))
                manager.mark_completed(index)
                print("Задача отмечена как выполненная")
            elif choice == "4":
                index = int(input("Введите номер задачи для удаления: "))
                manager.delete_task(index)
                print("Задача удалена!")
            elif choice == "5":
                print("Завершение работы.Все задачи сохранены.")
                break
            else:
                print("Некорректный выбор, попробуйте снова")
        except (ValueError, IndexError) as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
