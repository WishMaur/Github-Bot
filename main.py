import os

def makeCommits(days: int):
    return makeCommitsHelper(days, 0)

def makeCommitsHelper(days: int, total_commits: int):
    if days < 1:
        os.system('git push')
        return total_commits
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')
        
        # staging 
        os.system('git add data.txt')

        # commit 
        os.system('git commit --date="' + dates + '" -m "First commit for the day!"')
        
        # Update total commits
        total_commits += 1

        return makeCommitsHelper(days - 1, total_commits)

total_commits = makeCommits(1)
print("Total commits made:", total_commits)
