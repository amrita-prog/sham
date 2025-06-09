teachers = []

#sham
def store_teacher_info(name, subject, email, phone):
    teacher = {
        "name": name,
        "subject": subject,
        "email": email,
        "phone": phone
    }
    teachers.append(teacher)
    print(f"Teacher {name} added successfully.")

# teacher info
def input_teacher_info():
    while True:
        print("\nEnter Teacher Details:")
        name = input("Name: ")
        subject = input("Subject: ")
        email = input("Email: ")
        phone = int(input("Phone: "))

        store_teacher_info(name, subject, email, phone)

        more = input("Do you want to add another teacher? (yes/no): ").strip().lower()
        if more != 'yes':
            break
#teacher info
    print("\nAll Teachers:")
    for idx, teacher in enumerate(teachers, start=1):
        print(f"{idx}. {teacher}")

# Run the input function
input_teacher_info()
