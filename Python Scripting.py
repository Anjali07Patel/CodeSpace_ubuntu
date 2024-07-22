import os
import subprocess
from git import Repo

# Prompt user for repository URL
repo_url = input("Enter the repository URL: ")

# Prompt user for branch name
branch_name = input("Enter the branch name to add: ")

# Clone the repository
repo_name = os.path.basename(repo_url).replace('.git', '')
clone_dir = os.path.join(os.getcwd(), repo_name)
Repo.clone_from(repo_url, clone_dir)

# Navigate into the cloned repository directory
os.chdir(clone_dir)

# Add a new branch
subprocess.run(['git', 'checkout', '-b', branch_name])

# Display success message
print(f"Repository cloned and branch '{branch_name}' added successfully.")
