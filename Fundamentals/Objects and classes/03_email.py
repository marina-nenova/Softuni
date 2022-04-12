class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}"


command = input()
emails = []
while command != "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

sent_emails = list(map(int, input().split(", ")))

for index in sent_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())
