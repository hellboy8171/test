from github import Github

g = Github("hellboy8171", "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")
user = g.get_user()
repo = user.create_repo('pra')
