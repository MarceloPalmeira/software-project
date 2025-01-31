from event_client import create_event, get_events, register_attendee, get_attendees, edit_event, register_speaker_or_performer, edit_speaker_or_performer, get_speakers_or_performers

def main():

    while True:
        print("\n===== MENU =====")
        print("1. Event Creation and Management") #Ok
        print("2. Attendee Registration")   #Ok
        print ("3. Speaker and Performer Profiles Management")#Ok
        print("4. Vendor Management")
        print("5. Feedback and Survey Tools") 
        print("6. Budget and Financial Management")
        print ("7. Quit") #Ok

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


        elif opcao == "3":
            print("\n===== SUBMENU =====")
            print("\nHello Speaker/Performer! Please introduce yourself:")
            print("1. Create Profile")
            print("2. Edit Profile")
            print("3. List Profiles")
            print("4. Return")

            opt_2 = input("Choose an option: ")

            if opt_2 == "1":
                print("Create Profile")
                speaker_name = input("Nome do palestrante/artista: ")
                event_id = input("ID do evento: ")
                description = input("Breve descrição do palestrante/artista: ")
                print(register_speaker_or_performer(speaker_name, event_id, description))

            elif opt_2 == "2":
                print("Edit Profile")
                event_id = input("ID do evento: ")
                old_name = input("Nome atual do palestrante/artista: ")
                new_name = input("Novo nome do palestrante/artista (pressione Enter para manter o mesmo): ")
                new_description = input("Nova descrição do palestrante/artista (pressione Enter para manter a mesma): ")

                new_name = new_name if new_name else None
                new_description = new_description if new_description else None

                print(edit_speaker_or_performer(event_id, old_name, new_name, new_description))

            elif opt_2 == "3":
                print("\nPalestrantes e Artistas registrados:")
                speakers = get_speakers_or_performers()
                if not speakers:
                    print("Nenhum palestrante/artista registrado.")
                else:
                    for event_id, speaker_list in speakers.items():
                        print(f"\nEvento ID {event_id}:")
                        for speaker in speaker_list:
                            print(f" - {speaker['name']}: {speaker['description']}")

            elif opt_2 == "4":
                print("Return")
            else:
                print("Invalid option!") 

                        ############################################################################################
                        ####################PAREI AQUI##############################################################
                        ############################################################################################

        elif opcao == "4":
            #Gerenciamento de equipamentos/produtos/serviços com fornecedores;
            print("")
        elif opcao == "5":
            print("")
        elif opcao == "6":
            print("")
        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
