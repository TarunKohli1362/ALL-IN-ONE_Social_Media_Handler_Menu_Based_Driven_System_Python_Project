import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openpyxl


def send_email():
    print("\n--- Send Email ---")
    sender_email = input("Enter sender email: ")
    app_password = input("Enter app password: ")
    receiver_email = input("Enter receiver email: ")
    subject = input("Enter subject: ")
    message = input("Enter message: ")

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print("Failed to send email:", e)


def send_sms():
    print("\n--- Send SMS (Mock) ---")
    number = input("Enter phone number: ")
    message = input("Enter message: ")
    print(f"Sending SMS to {number}: {message}")
    print("Message sent (mock).")


def post_on_linkedin():
    print("\n--- Post on LinkedIn ---")
    print("Via Zapier: Triggered when you add a row to a connected Google Sheet.")
    content = input("Enter LinkedIn post content: ")

    try:
        path = "linkedin_posts.xlsx"
        try:
            wb = openpyxl.load_workbook(path)
        except FileNotFoundError:
            wb = openpyxl.Workbook()
            wb.active.append(["Post Content"])

        sheet = wb.active
        sheet.append([content])
        wb.save(path)
        print("Post content added to Google Sheet (locally).")

    except Exception as e:
        print("Error writing to sheet:", e)


def tweet_on_twitter():
    print("\n--- Tweet on Twitter (Mock) ---")
    tweet = input("Enter tweet: ")
    print(f"Posting tweet: {tweet}")
    print("Tweet posted (mock).")


def send_whatsapp_message():
    print("\n--- Send WhatsApp Message (Mock) ---")
    number = input("Enter WhatsApp number: ")
    message = input("Enter message: ")
    print(f"Sending WhatsApp message to {number}: {message}")
    print("Message sent (mock).")


def post_on_instagram():
    print("\n--- Post on Instagram ---")
    print("Instagram posting is typically automated via Instabot, Zapier, or Graph API.")
    print("Use a Zapier + Google Sheet based trigger for this task.")


def menu():
    while True:
        print("\n--- Python Automation Toolkit ---")
        print("1. Post on Instagram")
        print("2. Send Email")
        print("3. Send SMS (Mock)")
        print("4. Post on LinkedIn (via Google Sheets + Zapier)")
        print("5. Tweet on Twitter (Mock)")
        print("6. Send WhatsApp Message (Mock)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            post_on_instagram()
        elif choice == '2':
            send_email()
        elif choice == '3':
            send_sms()
        elif choice == '4':
            post_on_linkedin()
        elif choice == '5':
            tweet_on_twitter()
        elif choice == '6':
            send_whatsapp_message()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    menu()
