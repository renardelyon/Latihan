#!/usr/bin/env python3
import emails
import os
from datetime import date
import reports

desc_path = os.path.expanduser('~')+'/supplier-data/descriptions/'
desc_text=[desc  for desc in os.listdir(desc_path)]

text_data = []
for text_file in desc_text:
  with open(os.path.join(desc_path,text_file), 'r') as f:
    text_data.append([line.strip() for line in f.readlines()])
report=[]
def processdata(data):
  for isi in data:
    report.append("name: {}<br/>weight: {}\n".format(isi[0], isi[1]))
  return report
if __name__ == "__main__":
  summary = processdata(text_data)
  title="Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
  attachment="/tmp/processed.pdf"
  paragraph = "<br/><br/>".join(summary)
  reports.generate(attachment, title, paragraph)
#send email
  subject = "Upload Completed - Online Fruit Store"
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate(sender, receiver, subject, body, attachment)
  emails.send(message)
