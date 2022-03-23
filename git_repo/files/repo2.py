from github import Github
import csv

#repo_list = ['rajat', 'cde', 'defg']

g = Github("hellboy8171", "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")
user = g.get_user()
# repo = user.create_repo('a1')
with open('//root//names.csv', 'r') as file:    
    csv_reader = csv.reader(file)    
    for line in csv_reader:        
        for i in range(3):
            a = line[i]          
            repo = user.create_repo(a)
