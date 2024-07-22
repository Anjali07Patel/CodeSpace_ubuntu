import git
import os

# Define the repository directory and feature branch name
repo_dir = '/workspaces/CodeSpace_ubuntu/Repo'  # Replace with your actual local repository path
feature_branch_name = 'feature'  # Replace with your desired feature branch name

# Define remote repository URL and clone path
remote_repo_url = 'https://github.com/Anjali07Patel/Login-Page.git'  # Replace with your actual remote repository URL
clone_path = '/workspaces/CodeSpace_ubuntu/Repo'  # Ensure this is an empty directory

# Clone the remote repository if it does not already exist
if not os.path.exists(clone_path):
    print(f"Cloning repository from {remote_repo_url} to {clone_path}")
    git.Repo.clone_from(remote_repo_url, clone_path)
else:
    print(f"Directory {clone_path} already exists. Skipping cloning.")

# Initialize the repository
repo = git.Repo(clone_path)
print(f"Opened repository at {repo.working_tree_dir}")

# List all branches
print("Existing branches:")
for branch in repo.branches:
    print(branch.name)

# Ensure we are on the master branch before creating a new one
repo.git.checkout('main')  # Change to an existing branch

# Check if the feature branch already exists
branches = [branch.name for branch in repo.branches]
if feature_branch_name in branches:
    print(f"Branch '{feature_branch_name}' already exists.")
else:
    # Create the new feature branch
    repo.git.branch(feature_branch_name)
    print(f"Branch '{feature_branch_name}' created.")

# Check out the feature branch
repo.git.checkout(feature_branch_name)
print(f"Checked out branch '{feature_branch_name}'.")
