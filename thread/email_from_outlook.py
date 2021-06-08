# pip install html2text
# pip install beautifulsoup4
# pip install email_reply_parser

import email.parser
import imaplib
import time
import html2text
from email_reply_parser import EmailReplyParser
import re

user = 'rjsnh1522@outlook.com'
mailbox_password = "logan#9798#(&(*"


def get_email_body(body):
    if body.is_multipart():
        print("Its a multipart")
        for payload in body.get_payload():
            for part in body.walk():
                if (part.get_content_type() == 'text/plain') and (part.get('Content-Disposition') is None):
                    output = part.get_payload(decode=True)
                    return output
    else:
        text = f"{body.get_payload(decode=True)}"
        html = text.replace("b'", "")
        h = html2text.HTML2Text()
        h.ignore_links = True
        output = (h.handle(f'''{html}''').replace("\\r\\n", ""))
        output = output.replace("'", "")
        # output in one line
        # output = output.replace('\n'," ")
        output = output.replace('*', "")
        print(output)
        return output


def clear_inbox(conn, dest_folder):
    output = []
    result = conn.uid('COPY', emailid, dest_folder)
    output.append(result)
    if result[0] == 'OK':
        print("Clear Inbox")
        # result = mov, data = conn.uid('STORE', emailid, '+FLAGS', '(UNSEEN)')
        # print(result)
        # print("Mov", mov)
        # print("dataaa", data)
        conn.expunge()


conn = imaplib.IMAP4_SSL("outlook.office365.com")
conn.login(user, mailbox_password)
conn.select("Inbox")

try:

    resp, items = conn.uid("search", None, '(UNSEEN)')
    items = items[0].split()
    print("items", items)

    for emailid in items:
        t = time.time()
        f = open(f"{t}.txt", "a+")
        resp, data = conn.uid("fetch", emailid, "(RFC822)")
        if resp == 'OK':
            email_body = data[0][1].decode('utf-8')

            email_message = email.message_from_string(email_body)
            subject = email_message["Subject"]
            if subject.lower().startswith('re: anlyz case management'.lower()):
                output = get_email_body(email_message)
                case_id = [int(s) for s in subject.split() if s.isdigit()]
                print("**" * 10)
                email_parser = EmailReplyParser.read(output.decode("utf-8"))
                regex = "(?:(?:on|On|ON) (?:Wed|Tue|Mon|Thu|Fri|Sat|Sun), (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]+, [0-9]{4} at [0-9]+:[0-9]+ (?:AM|PM))"
                kk = re.split(regex, email_parser.reply)
                import ipdb;ipdb.set_trace()
                print(kk[0])
                f.write(kk[0])
                print("**" * 10)
                clear_inbox(conn, "Processed")
            else:
                clear_inbox(conn, "backup")
        f.close()
except IndexError:
    print("No new email")

conn.close()
conn.logout()
