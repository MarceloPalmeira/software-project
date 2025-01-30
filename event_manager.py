from event_client import create_event, get_events, register_attendee, get_attendees, edit_event

def main():

    while True:
        print("\n===== MENU =====")
        print("1. Event Creation and Management") #Ok
        print("2. Attendee Registration")   #Ok
        print ("3. Schedule and Agenda Management")
        print("4 Speaker and Performer Profiles Management")
        print("5. Vendor Management")
        print("6. Feedback and Survey Tools") 
        print("7. Budget and Financial Management")
        print ("8. Quit") #Ok

        opcao = input("Escolha uma opção: ")

    ############################################################################################
    ############################################################################################
    ############################################################################################

        if opcao == "1":
            print("\n===== SUBMENU =====")
            print("1. Criar evento")
            print("2. Editar evento")
            print("3. Listar eventos")
            print("4. Listar participantes registrados")
            print("5. Voltar")

            opt_1 = input("Escolha uma opção: ")

            if opt_1 == "1":
                # Criação de evento
                name = input("Nome do evento: ")
                date = input("Data do evento (ANO-MÊS-DIA): ")
                print(create_event(name, date))

            elif opt_1 == "2":
                # Edição de evento
                event_id = input("ID do evento: ")
                name = input("Novo nome do evento: ")
                date = input("Nova data do evento (ANO-MÊS-DIA): ")
                print(edit_event(event_id, name, date))

            elif opt_1 == "3":
                print("\nEventos cadastrados:")
                eventos = get_events()
                if not eventos:
                    print("Nenhum evento cadastrado.")
                else:
                    for event in eventos:
                        print(f"ID: {event['id']}, Nome: {event['name']}, "
                            f"Data: {event['date']}, Participantes: {event['attendees']}")

            elif opt_1 ==  "4": 
                print("\nParticipantes registrados:")
                participantes = get_attendees()
                if not participantes:
                    print("Nenhum participante registrado.")
                else:
                    for event_id, names in participantes.items():
                        print(f"Evento ID {event_id}: {', '.join(names)}")

            elif opt_1 == "5":
                print("Voltando ao menu principal...")
            else:
                print("Opção inválida!")

        elif opcao == "2":
                # Registrar participante (em um evento específico)
                name = input("Nome do participante: ")
                event_id = input("ID do evento: ")
                print(register_attendee(name, event_id))

                        ############################################################################################
                        ####################PAREI AQUI##############################################################
                        ############################################################################################


        elif opcao == "3":
            print ("")

        elif opcao == "4":
            print("\nParticipantes registrados:")
            participantes = get_attendees()
            if not participantes:
                print("Nenhum participante registrado.")
            else:
                for event_id, names in participantes.items():
                    print(f"Evento ID {event_id}: {', '.join(names)}")

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
