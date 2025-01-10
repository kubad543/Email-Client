import tkinter as tk
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def fetch_all_emails(email_address, password, keyword=None):
    # Połącz się z serwerem IMAP (Gmail)
    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    # Zaloguj się do skrzynki pocztowej
    mail.login(email_address, password)

    # Wybierz folder, z którego chcemy pobrać wiadomości (np. "INBOX")
    mail.select('inbox')

    # Kryterium wyszukiwania - wszystkie wiadomości lub wiadomości zawierające słowo kluczowe
    if keyword:
        result, data = mail.search(None, '(TEXT "{}")'.format(keyword))
    else:
        result, data = mail.search(None, 'ALL')

    # Przeiteruj przez wszystkie wiadomości
    messages = []
    for num in data[0].split():
        # Pobierz wiadomość
        result, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Dekoduj nagłówki nadawcy, tematu i treści wiadomości
        sender = email.header.decode_header(msg["From"])[0][0]
        if isinstance(sender, bytes):
            sender = sender.decode()
        subject = email.header.decode_header(msg["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode()

        # Dodaj informacje o nadawcy, temacie i treści do listy
        messages.append({'sender': sender, 'subject': subject, 'num': num})

    # Wyloguj się z serwera
    mail.logout()

    # Wyświetl wiadomości w oknie tekstowym
    message_text_display.delete('1.0', tk.END)  # Wyczyść okno tekstowe
    for message in messages:
        num = message['num']
        sender = message['sender']
        subject = message['subject']
        message_text_display.insert(tk.END,
                                    f'Od: {sender}\nTemat: {subject}\n')
        # Dodaj przycisk "Odczytaj" obok każdej wiadomości
        read_button = tk.Button(message_text_display, text="Odczytaj", command=lambda num=num: display_email_content(email_address, password, num))
        message_text_display.window_create(tk.END, window=read_button)
        message_text_display.insert(tk.END, '\n\n')


def display_email_content(email_address, password, num):
    # Połącz się z serwerem IMAP (Gmail)
    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    # Zaloguj się do skrzynki pocztowej
    mail.login(email_address, password)

    # Wybierz folder, z którego chcemy pobrać wiadomość (np. "INBOX")
    mail.select('inbox')

    # Pobierz treść wiadomości
    result, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    content = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                content += part.get_payload(decode=True).decode()
    else:
        content = msg.get_payload(decode=True).decode()

    # Wyświetl treść wiadomości w nowym oknie
    content_window = tk.Toplevel()
    content_window.title("Treść wiadomości")

    content_text = tk.Text(content_window, height=20, width=80)
    content_text.pack()
    content_text.insert(tk.END, content)

    # Wyślij autoresponse
    send_autoresponse(email_address, password, msg)

    # Wyloguj się z serwera
    mail.logout()


def send_autoresponse(email_address, password, msg):
    # Połącz się z serwerem SMTP (Gmail)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, password)

    sender = msg['From']
    subject = msg['Subject']

    # Odpowiedz
    reply_msg = MIMEMultipart()
    reply_msg['From'] = email_address
    reply_msg['To'] = sender
    reply_msg['Subject'] = f"Odp: {subject}"

    body = f"Dziękuję za maila!\n\nOdczytano: Tak"
    reply_msg.attach(MIMEText(body, 'plain'))

    # Wyślij odpowiedź
    server.send_message(reply_msg)

    # Wyloguj się z serwera
    server.quit()


def send_email(email_address, password):
    # Pobierz dane z pól wprowadzania
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # Utwórz wiadomość e-mail
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Połącz się z serwerem SMTP (Gmail)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, password)

    # Wyślij wiadomość
    server.send_message(msg)

    # Wyloguj się z serwera
    server.quit()


def create_mail_interface(email_address, password):
    # Tworzenie okna głównego
    root = tk.Tk()
    root.title("Prosty klient poczty")

    # Pole do wprowadzenia adresata
    recipient_label = tk.Label(root, text="Adresat:")
    recipient_label.pack()
    global recipient_entry
    recipient_entry = tk.Entry(root)
    recipient_entry.pack()

    # Pole do wprowadzenia tematu
    subject_label = tk.Label(root, text="Temat:")
    subject_label.pack()
    global subject_entry
    subject_entry = tk.Entry(root)
    subject_entry.pack()

    # Pole do wprowadzenia treści wiadomości
    message_label = tk.Label(root, text="Treść:")
    message_label.pack()
    global message_text
    message_text = tk.Text(root, height=10, width=50)
    message_text.pack()

    # Przycisk do wysyłania wiadomości
    send_button = tk.Button(root, text="Wyślij wiadomość", command=lambda: send_email(email_address, password))
    send_button.pack()

    # Pole do wprowadzenia słowa kluczowego
    keyword_label = tk.Label(root, text="Słowo kluczowe:")
    keyword_label.pack()
    global keyword_entry
    keyword_entry = tk.Entry(root)
    keyword_entry.pack()

    # Przycisk do szukania wiadomości na podstawie słowa kluczowego
    search_button = tk.Button(root, text="sprawdz maile",
                              command=lambda: fetch_all_emails(email_address, password, keyword_entry.get()))
    search_button.pack()

    # Okno tekstowe do wyświetlania wiadomości
    global message_text_display
    message_text_display = tk.Text(root, height=20, width=80)
    message_text_display.pack()

    # Uruchomienie pętli głównej
    root.mainloop()


def login():
    # Pobierz dane z pól wprowadzania
    email_address = email_entry.get()
    password = password_entry.get()

    # Połącz się z serwerem IMAP (Gmail)
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_address, password)
        print("Zalogowano pomyślnie.")
        login_window.destroy()  # Zamknij okno logowania
        create_mail_interface(email_address, password)  # Przejdź do interfejsu z mailami
    except imaplib.IMAP4.error as e:
        print("Błąd logowania:", e)


# Tworzenie okna logowania
login_window = tk.Tk()
login_window.title("Logowanie")

# Pole do wprowadzenia adresu e-mail
email_label = tk.Label(login_window, text="Adres e-mail:")
email_label.pack()
email_entry = tk.Entry(login_window)
email_entry.pack()

# Pole do wprowadzenia hasła
password_label = tk.Label(login_window, text="Hasło:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Przycisk do logowania
login_button = tk.Button(login_window, text="Zaloguj", command=login)
login_button.pack()

# Uruchomienie pętli głównej
login_window.mainloop()
