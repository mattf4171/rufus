"""

Was it Rufus? - Proto AI assessment

Matthew Fernandez 
01/12/2022

Task is to create a program that prints specific facts about a local git repository. 

Input:
git_dir -> directory in which to assess git status

Output:
active branch (boolean)
whether repository files have been modified (boolean)
whether the current head commit was authored in the last week (boolean)
whether the current head commit was authored by Rufus (boolean)

"""

import sys
import os
from git import Repo

# Class that encompasses all the functionality needed for "was it Rufus"
class Rufus:

	def __init__(self, git_dir):
		self.git_dir = git_dir

	def git_repo_specs(self):
		
		# Run git status using GitPython library to interact with Git

		repo = Repo(self.git_dir)
		git_status = str(repo.git.status()).replace("\t"," ").split("\n")
		
		# active branch (boolean)

		active_branch = git_status[0].split(" ")[2]
		print("active branch: {}".format(active_branch))
		

		# whether repository files have been modified (boolean)
		# check if 'nothing to commit..' is found in the output of git status 
		check_modified = 'nothing to commit, working tree clean'
		modified = True 
		for line in git_status:
			if check_modified in line:
				modified = False

		print("local changes: {}".format(modified))
		
	
		# whether the current head commit was authored in the last week (boolean)
		# run git log using GitPython
		# if git_log list has values, then we know there was a recent commit.

		git_log = str(repo.git.log()).replace("\t", " ").split("\n")
		recent_commit = False
		if len(git_log) > 0:
			recent_commit = True

		print("recent commit: {}".format(recent_commit))	# use git log to see this

		# whether the current head commit was authored by Rufus (boolean)
		# locally reassign name to Rufus 
		# git config --local user.name "Rufus"

		rufus = False
		for line in git_log:
			#latest commit at top so break once found Author 
			if 'Author:' in line:
				word_tokens = line.split(" ")
				for idx, word in enumerate(word_tokens):
					if "Author" in word:
						# the following string is the author name
						if word_tokens[idx+1] == "Rufus":
							rufus = True 

		print("blame Rufus: {}".format(rufus))

if __name__ == "__main__":
	
	#
	# This is my local directory that was used for testing purposes
	#
	# C:\Users\matth\OneDrive\Desktop\Education\rufus_prontoAI
	#
	print(os.getcwd())
	value = input("Input directory in which to assess git status: ")
	new_rufus = Rufus(value)
	new_rufus.git_repo_specs()