# Simple Email Client

A simple email client developed in Python using the Tkinter library for the graphical user interface. The application supports basic email management functions, including login, sending emails, viewing the inbox, and automatically replying to read messages.

## Project Scope

The application is designed with ease of use and a clean interface in mind. The project includes:

- **Gmail Account Login:** Secure connection handling with SMTP and IMAP servers.  
- **Sending Emails:** Ability to send messages to any recipient directly from the application interface.  
- **Inbox Browsing:** Displaying emails in an organized list with keyword filtering options.  
- **Reading Emails:** Detailed view of each message, including sender, subject, and content.  
- **Automatic Replies:** After reading an email, the application automatically sends a reply confirming the message has been read.

## Key Features

- **Secure Connection:** SSL/TLS protocols are used for secure SMTP and IMAP communication.  
- **Graphical User Interface (GUI):** Intuitive design built with Tkinter for easy navigation.  
- **Email Filtering:** Search functionality to filter emails based on keywords in the subject or body.  
- **Automation:** Automatic reply generation after reading emails, ensuring quick acknowledgment of received messages.  
- **Error Handling:** Basic error management for login failures, sending issues, and connection problems with mail servers.

## Application Structure

- **User Interface (GUI):** Login fields, email composition form, inbox list, and separate windows for viewing email details.  
- **Application Logic:** Handles SMTP/IMAP connections, manages login sessions, and automates replies.  
- **Security:** Secure transmission of login credentials with no local storage of sensitive data.

## Example Workflow

1. The user logs into their Gmail account by providing an email address and password.  
2. After logging in, the latest emails are displayed in an inbox list.  
3. Clicking the **Read** button opens a new window with the full message content.  
4. Upon reading the message, an automatic reply is generated and sent to the sender, confirming receipt.

## Technologies Used

- **Python 3.x**  
- **Tkinter** – Graphical User Interface  
- **smtplib** – Handling email sending (SMTP)  
- **imaplib** – Retrieving emails (IMAP)  
- **email** – Parsing and creating email messages  

