from aler import email_alert


def text_to_email(text_file,email,subject):
    with open(text_file) as f:
        lines = f.read()
        #[print(line) for line in f.readlines()]
        email_alert( subject,lines , email)

