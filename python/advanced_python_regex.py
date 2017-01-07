import pandas as pd
import re
from collections import defaultdict

data = pd.read_csv('faculty.csv',skipinitialspace = True)
data['degree'] = data['degree'].str.replace('.','')

def degree_types(dataframe):
    degrees = list(set(dataframe['degree']))
    all_degrees = ' '.join(list(dataframe['degree'])).split(' ')
    count_dict = defaultdict(int)
    for i in all_degrees:
        count_dict[i] += 1
    return count_dict


def num_titles(dataframe):
    raw_titles = list(dataframe['title'])
    titles = []
    for title in raw_titles:
        titles += re.findall(r'.*[\w+\sP]rofessor', title)
    titles_count_dict = defaultdict(int)
    for title in titles:
        titles_count_dict[title] += 1
    return titles_count_dict


def email_addresses(dataframe):
    emails = list(dataframe['email'])
    return emails


def email_domains(dataframe):
    emails = email_addresses(dataframe)
    domains = []
    for email in emails:
        domains += re.findall(r'@(.*)', email)
    return list(set(domains))
