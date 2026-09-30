CLINIC = "O'dent Aesthetic and Family Dental Clinic"


services = [
    "Teeth Cleaning & Scaling",
    "Teeth Whitening",
    "Root Canal Treatment",
    "Dental Implants",
    "Braces & Aligners",
    "Smile Makeover",
    "Tooth Extraction",
    "Pediatric Dentistry",
    "Veneers & Crowns"
]


slots = [
    "10:00 AM", "11:00 AM", "12:00 PM",
    "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"
]


bookings = []

def show_info():
    print("\n" + "="*35)
    print(CLINIC)
    print("="*35)
    print("Tagline: Your Trusted Dental Care Partner")
    print("Doctor: Dr. Reet Sharma (Reg: 696969-A)")
    print("Position: Lead Dentist (Aesthetic Specialist)")
    print("\nAddress:")
    print("SCO 89, 1st Floor, Sector 82, JLPL Industrial Area, Mohali, Punjab")
    print("Phone: +91 9807645 | Email: odentaestheticdentistry89@gmail.com")
    print("Timings: Mon - Sat (10am to 7pm) | Sunday Closed")


def print_services():
    print("\n--- Available Treatments ---")
    for i in range(len(services)):
        print(str(i + 1) + ". " + services[i])


def add_appointment():
    print("\n--- Book Appointment ---")
    name = input("Patient Name: ").strip()
    if len(name) == 0:
        print("Name is required.")
        return

    age = input("Age: ").strip()
    contact = input("Contact Number: ").strip()

    print_services()

    chosen_service = ""
    while True:
        raw_choice = input("Select service (1-9): ").strip()
        if raw_choice.isdigit():
            idx = int(raw_choice) - 1
            if 0 <= idx < len(services):
                chosen_service = services[idx]
                break
        print("Invalid selection, please try again.")

    pref_date = input("Enter appointment date (DD/MM/YYYY): ").strip()

    print("\nAvailable Time Slots:")
    for num, slot in enumerate(slots, 1):
        print(f"[{num}] {slot}")


    selected_time = ""
    slot_input = input("Choose slot number: ").strip()
    if slot_input.isdigit() and 1 <= int(slot_input) <= len(slots):
        selected_time = slots[int(slot_input) - 1]
    else:
        print("Invalid slot number entered. Cancelling...")
        return


    patient_data = {
        "name": name,
        "age": age,
        "phone": contact,
        "service": chosen_service,
        "date": pref_date,
        "time": selected_time
    }
    bookings.append(patient_data)


    print("\nBooking successful!")
    print(f"Booked: {name} for {chosen_service} on {pref_date} ({selected_time})")



def view_all():
    if not bookings:
        print("\nNo appointments booked yet.")
        return

    print(f"\nAll Appointments (Total: {len(bookings)})")
    print("-" * 35)
    for i, b in enumerate(bookings, 1):
        print(f"{i}) {b['name']} (Age: {b['age']})")
        print(f"   Treatment: {b['service']}")
        print(f"   When: {b['date']} at {b['time']}")
        print(f"   Contact: {b['phone']}")



def search_patient():
    if len(bookings) == 0:
        print("\nNo records available to search.")
        return

    query = input("\nEnter name to search: ").strip().lower()
    matches = []
    for b in bookings:
        if query in b['name'].lower():
            matches.append(b)

    if not matches:
        print("No matching patient record found.")
    else:
        print(f"Found {len(matches)} match(es):")
        for m in matches:
            print(f"- {m['name']} | {m['service']} | {m['date']} ({m['time']}) | Phone: {m['phone']}")



def cancel_booking():
    if len(bookings) == 0:
        print("\nNothing to cancel.")
        return

    view_all()
    ans = input("\nEnter appointment number to remove: ").strip()
    if ans.isdigit():
        idx = int(ans) - 1
        if 0 <= idx < len(bookings):
            removed = bookings.pop(idx)
            print(f"Cancelled booking for {removed['name']}.")
            return

    print("Invalid index. Nothing removed.")


def main():
    while True:
        print("\n==== DENTAL CLINIC MENU ====")
        print("1. Clinic & Contact Info")
        print("2. Treatment List")
        print("3. Book Appointment")
        print("4. View All Bookings")
        print("5. Search Patient")
        print("6. Cancel Appointment")
        print("7. Exit")

        opt = input("Enter choice (1-7): ").strip()

        if opt == "1":
            show_info()
        elif opt == "2":
            print_services()
        elif opt == "3":
            add_appointment()
        elif opt == "4":
            view_all()
        elif opt == "5":
            search_patient()
        elif opt == "6":
            cancel_booking()
        elif opt == "7":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 7.")



if __name__ == "__main__":
    main()
