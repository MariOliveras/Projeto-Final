import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """Carrega as tarefas do arquivo JSON se ele existir."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def _save_tasks(self):
        """Salva a lista atual de tarefas no arquivo JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def add_task(self, title, description):
        """Adiciona uma nova tarefa."""
        new_task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks.append(new_task)
        self._save_tasks()
        print(f"\n✅ Tarefa '{title}' adicionada com sucesso!")

    def list_tasks(self):
        """Lista todas as tarefas cadastradas."""
        if not self.tasks:
            print("\n📭 Nenhuma tarefa encontrada.")
            return

        print("\n📋 === LISTA DE TAREFAS ===")
        for task in self.tasks:
            status = "🟢 Concluída" if task["completed"] else "🔴 Pendente"
            print(f"ID: {task['id']} | [{status}] {task['title']}")
            print(f"   Descrição: {task['description']}\n--------------------------")

    def complete_task(self, task_id):
        """Marca uma tarefa específica como concluída."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save_tasks()
                print(f"\n🚀 Tarefa ID {task_id} marcada como concluída!")
                return
        print("\n❌ Tarefa não encontrada com o ID informado.")

    def delete_task(self, task_id):
        """Exclui uma tarefa da lista."""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                # Reorganiza os IDs para não quebrar a sequência
                for index, t in enumerate(self.tasks):
                    t["id"] = index + 1
                self._save_tasks()
                print(f"\n🗑️ Tarefa ID {task_id} removida com sucesso!")
                return
        print("\n❌ Tarefa não encontrada com o ID informado.")
