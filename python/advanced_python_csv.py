import csv
from advanced_python_regex import email_addresses

def emails_writer(dataframe):
    emails_list = email_addresses(dataframe)
    with open('emails.csv', 'wb') as f:
        writer = csv.writer(f)
        for email in emails_list:
            writer.writerow([email])
