from firebase_admin import credentials, firestore, initialize_app
import uuid

# Initialize Firebase only once
cred = credentials.Certificate("secrets/serviceAccountKey.json")  # path to your key
initialize_app(cred)
db = firestore.client()

# Store teacher info in Firestore
def store_teacher_info(name, subject, email, phone):
    teacher = {
        "name": name,
        "subject": subject,
        "email": email,
        "phone": phone
    }

    doc_id = str(uuid.uuid4())
    db.collection("teachers").document(doc_id).set(teacher)
    print(f"✅ Teacher {name} added successfully to Firestore.")

# Input from user
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

    # Display all teachers from Firestore
    print("\n📚 All Teachers (from Firebase):")
    teachers_ref = db.collection("teachers").stream()
    for idx, doc in enumerate(teachers_ref, start=1):
        teacher = doc.to_dict()
        print(f"{idx}. {teacher['name']} | {teacher['subject']} | {teacher['email']} | {teacher['phone']}")

# Run
input_teacher_info()
