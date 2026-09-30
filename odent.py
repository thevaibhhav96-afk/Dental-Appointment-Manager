CLINIC_NAME = "O'dent Aesthetic and Family Dental Clinic"


services_list = [
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

time_slots = ["10:00 AM", "11:00 AM", "12:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]


booked_patients = []


def view_overview():
    print(f"\n {CLINIC_NAME} ")
    print("Tagline: Your Trusted Dental Care Partner")
    print("About: We provide dental care for patients of all ages.\n")
    print("Doctor: Dr. Reet Sharma (Reg: 696969-A) | Lead Dentist")
    print("Highlights: Aesthetic Specialist, Patient-Centered, Certified")
    print("\nContact Info:")
    print("SCO 89, 1st Floor, Sec 82, JLPL Ind. Area, Mohali, Punjab")
    print("Phone: +91 9807645 | Email: odentaestheticdentistry89@gmail.com")
    print("Timings: Mon-Sat 10:00 AM to 7:00 PM (Sunday Closed)")


def list_services():
    print("\nAvailable Dental Treatments:")
    for num, name in enumerate(services_list, 1):
        print(f" {num}. {name}")


def create_booking():
    print("\n[ Book New Slot ]")
    p_name = input("Enter patient name: ").strip()
    p_age = input("Age: ").strip()
    p_phone = input("Phone: ").strip()

    if not p_name or not p_phone:
        print(">> Missing details. Booking skipped.")
        return

    list_services()
    try:
        s_idx = int(input("Select service (1-9): ")) - 1
        if s_idx not in range(len(services_list)):
            print(">> Invalid service chosen.")
            return
        selected_service = services_list[s_idx]
    except ValueError:
        print(">> Numeric input only.")
        return

    appt_date = input("Date (DD/MM/YYYY): ").strip()

    print("\nSlots:")
    for i, t in enumerate(time_slots, 1):
        print(f" {i}) {t}")

    try:
        t_idx = int(input("Pick a slot number: ")) - 1
        if t_idx not in range(len(time_slots)):
            print(">> Out of bounds slot.")
            return
        chosen_slot = time_slots[t_idx]
    except ValueError:
        print(">> Invalid slot input.")
        return

    entry = {
        "name": p_name,
        "age": p_age,
        "phone": p_phone,
        "service": selected_service,
        "date": appt_date,
        "time": chosen_slot
    }
    booked_patients.append(entry)
    print(f"\n>> Confirmed! {p_name} booked for {selected_service} on {appt_date} at {chosen_slot}.")


def show_all_bookings():
    if not booked_patients:
        print("\n>> Appointment book is currently empty.")
        return

    print(f"\n Current Bookings ({len(booked_patients)}) ")
    for i, item in enumerate(booked_patients, 1):
        print(f"{i}. {item['name']} | {item['service']} | {item['date']} @ {item['time']} | Ph: {item['phone']}")


def search_record():
    term = input("\nEnter patient name to find: ").lower().strip()
    hits = [x for x in booked_patients if term in x['name'].lower()]
    
    if not hits:
        print(">> No matching records.")
        return

    print(f">> Found {len(hits)} record(s):")
    for row in hits:
        print(f" - {row['name']} ({row['age']} yrs) -> {row['service']} on {row['date']} ({row['time']})")


def cancel_record():
    if not booked_patients:
        print("\n>> Nothing to cancel.")
        return
    
    show_all_bookings()
    try:
        target = int(input("\nEnter index to cancel: "))
        if 1 <= target <= len(booked_patients):
            dropped = booked_patients.pop(target - 1)
            print(f">> Cancelled booking for {dropped['name']}.")
        else:
            print(">> Invalid appointment index.")
    except ValueError:
        print(">> Please type a number.")



MENU_ACTIONS = {
    "1": ("Clinic Overview & Contact", view_overview),
    "2": ("List Services", list_services),
    "3": ("Book Appointment", create_booking),
    "4": ("View All Appointments", show_all_bookings),
    "5": ("Search by Name", search_record),
    "6": ("Cancel Appointment", cancel_record),
}

def main():
    while True:
        print("\n")
        print(" DENTAL CLINIC MENU")
        
        for key, val in MENU_ACTIONS.items():
            print(f"{key}. {val[0]}")
        print("7. Exit")

        choice = input("\nAction: ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        elif choice in MENU_ACTIONS:
            MENU_ACTIONS[choice][1]()
        else:
            print(">> Unknown choice, try again.")


if __name__ == "__main__":
    main()
