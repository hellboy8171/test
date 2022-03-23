import csv
import os
from github import Github

g = ("hellboy8171", "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")
user = g.get_user()

#file = "C:\\Users\\Administrator.DEMO\\Desktop\\agrawal\\anuj.csv"
with open('//root//names.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        for i in range(3):
            repo = user.create_repo(line[i])
             

