from event_client import create_event, get_events, register_attendee, get_attendees

def main():
    while True:
        print("\n===== MENU =====")
        print("1. Criar evento")
        print("2. Listar eventos")
        print("3. Registrar participante")
        print("4. Listar participantes")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            name = input("Nome do evento: ")
            date = input("Data do evento (ANO-MÊS-DIA): ")
            #date = input("Data do evento (YYYY-MM-DD): ")
            print(create_event(name, date))

        elif opcao == "2":
            print("Eventos cadastrados:")
            eventos = get_events()
            if not eventos:
                print("Nenhum evento cadastrado.")
            else:
                for event in eventos:
                    print(f"ID: {event['id']}, Nome: {event['name']}, Data: {event['date']}, Participantes: {event['attendees']}")

        elif opcao == "3":
            name = input("Nome do participante: ")
            event_id = input("ID do evento: ")
            print(register_attendee(name, event_id))

        elif opcao == "4":
            print("Participantes registrados:")
            participantes = get_attendees()
            if not participantes:
                print("Nenhum participante registrado.")
            else:
                for event_id, names in participantes.items():
                    print(f"Evento ID {event_id}: {', '.join(names)}")

        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
