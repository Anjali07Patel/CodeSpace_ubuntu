#!/bin/bash

# Prompt user for repository URL
read -p "Enter the repository URL: " repo_url

# Prompt user for branch name
read -p "Enter the branch name to add: " branch_name

# Clone the repository
git clone $repo_url

# Navigate into the cloned repository directory
repo_name=$(basename "$repo_url" .git)
cd $repo_name

# Add a new branch
git checkout -b $branch_name

# Display success message
echo "Repository cloned and branch $branch_name added successfully."
