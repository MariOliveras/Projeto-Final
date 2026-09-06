from task_manager import TaskManager

def show_menu():
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Excluir Tarefa")
    print("5. Sair")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("\nEscolha uma opção (1-5): ").strip()

        if choice == "1":
            title = input("Digite o título da tarefa: ").strip()
            description = input("Digite a descrição da tarefa: ").strip()
            if title:
                manager.add_task(title, description)
            else:
                print("\n❌ O título da tarefa não pode ser vazio.")

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Digite o ID da tarefa a concluir: "))
                manager.complete_task(task_id)
            except ValueError:
                print("\n❌ Por favor, insira um número válido para o ID.")

        elif choice == "4":
            try:
                task_id = int(input("Digite o ID da tarefa a excluir: "))
                manager.delete_task(task_id)
            except ValueError:
                print("\n❌ Por favor, insira um número válido para o ID.")

        elif choice == "5":
            print("\n👋 Saindo do sistema. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()
