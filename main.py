import csv
from generate_email import generate_email
from send_email import send_email

CSV_PATH = 'contacts.csv'
SUBJECT = "Quick Question: Junior roles at your company"

with open(CSV_PATH, newline='', encoding='utf‑8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for contact in reader:
        email_body = generate_email(contact)
        send_email(contact['recruitment_email'], SUBJECT, email_body, attachment_path='Neil_CV.pdf')
        print("Sent to", contact['company_name'])
