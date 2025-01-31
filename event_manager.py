from event_client import create_event, get_events, register_attendee, get_attendees, edit_event, register_speaker_or_performer, get_speakers_or_performers, register_vendor, get_vendors, get_budget, get_feedback, submit_feedback, update_budget

def main():
    while True:
        print("\n===== MENU =====")
        print("1. Event Creation and Management")
        print("2. Attendee Registration")
        print("3. Speaker and Performer Management")
        print("4. Vendor Management")
        print("5. Feedback and Survey Tools")
        print("6. Budget and Financial Management")
        print("7. Quit")

        option = input("Choose an option: ")

        if option == "1":
            print("\n===== EVENT MANAGEMENT =====")
            print("1. Create Event")
            print("2. Edit Event")
            print("3. List Events")
            print("4. List Registered Attendees")
            print("5. Back")

            sub_option = input("Choose an option: ")

            if sub_option == "1":
                name = input("Event Name: ")
                date = input("Event Date (YYYY-MM-DD): ")
                print(create_event(name, date))

            elif sub_option == "2":
                event_id = input("Event ID: ")
                name = input("New Event Name: ")
                date = input("New Event Date (YYYY-MM-DD): ")
                print(edit_event(event_id, name, date))

            elif sub_option == "3":
                print("\nRegistered Events:")
                events = get_events()
                if not events:
                    print("No events registered.")
                else:
                    for event in events["events"]:
                        print(f"ID: {event['id']}, Name: {event['name']}, Date: {event['date']}, Attendees: {event['attendees']}")

            elif sub_option == "4":
                print("\nRegistered Attendees:")
                attendees = get_attendees()
                if not attendees:
                    print("No attendees registered.")
                else:
                    for event_id, names in attendees.items():
                        print(f"Event ID {event_id}: {', '.join(names)}")

        elif option == "2":
            name = input("Attendee Name: ")
            event_id = input("Event ID: ")
            print(register_attendee(name, event_id))

        elif option == "3":
            print("\n===== SPEAKER/PERFORMER MANAGEMENT =====")
            print("1. Register Speaker/Performer")
            print("2. List Speakers/Performers")
            print("3. Back")

            sub_option = input("Choose an option: ")

            if sub_option == "1":
                speaker_name = input("Speaker/Performer Name: ")
                event_id = input("Event ID: ")
                description = input("Short Description: ")
                print(register_speaker_or_performer(speaker_name, event_id, description))

            elif sub_option == "2":
                print("\nRegistered Speakers/Performers:")
                speakers = get_speakers_or_performers()
                if not speakers:
                    print("No speakers/performers registered.")
                else:
                    for event_id, speaker_list in speakers.items():
                        print(f"\nEvent ID {event_id}:")
                        for speaker in speaker_list:
                            print(f" - {speaker['name']}: {speaker['description']}")

        elif option == "4":
            print("\n===== VENDOR MANAGEMENT =====")
            print("1. Register Vendor")
            print("2. List Vendors")
            print("3. Back")

            sub_option = input("Choose an option: ")

            if sub_option == "1":
                name = input("Vendor Name: ")
                products = input("Products/Services Offered (comma-separated): ")
                print(register_vendor(name, products))

            elif sub_option == "2":
                print("\nRegistered Vendors:")
                vendors = get_vendors()
                if not vendors:
                    print("No vendors registered.")
                else:
                    for name, products in vendors.items():
                        print(f" - {name}: {', '.join(products)}")

        elif option == "5":
            print("\n===== FEEDBACK MANAGEMENT =====")
            print("1. Submit Feedback")
            print("2. List Feedback")
            print("3. Back")

            sub_option = input("Choose an option: ")

            if sub_option == "1":
                event_id = input("Event ID: ")
                feedback = input("Enter your feedback: ")
                print(submit_feedback(event_id, feedback))

            elif sub_option == "2":
                event_id = input("Event ID: ")
                feedbacks = get_feedback(event_id)
                if not feedbacks:
                    print("No feedback found.")
                else:
                    print("\nFeedback:")
                    for fb in feedbacks:
                        print(f" - {fb}")

        elif option == "6":
            print("\n===== BUDGET MANAGEMENT =====")
            print("1. Update Budget")
            print("2. View Budget")
            print("3. Back")

            sub_option = input("Choose an option: ")

            if sub_option == "1":
                event_id = input("Event ID: ")
                amount = input("Enter the new budget: ")
                print(update_budget(event_id, amount))

            elif sub_option == "2":
                event_id = input("Event ID: ")
                budget = get_budget(event_id)
                print(f"Event Budget: {budget}")

        elif option == "7":
            print("Exiting...")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
