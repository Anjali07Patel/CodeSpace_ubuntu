import git

# Open an existing local repository
my_repo = git.Repo('/home/codespace/.oh-my-zsh/.git')
print(f"Opened repository at {my_repo.working_tree_dir}")

# Clone a remote repository
# Check out via HTTPS
git.Repo.clone_from('https://github.com/Anjali07Patel/python_program.git', 'python_program-https')
print("Cloned repository via HTTPS into 'python_program-https'")



my_repo = git.Repo('/home/codespace/.oh-my-zsh/.git')
# Create a copy of the existing repo
my_repo.clone('/home/codespace/.oh-my-zsh/.git')
print(f"Cloned local repository into '/home/codespace/.oh-my-zsh/.git'")
