import os

if __name__ == "__main__":
    if '{{ cookiecutter.open_source_license }}' == "Not open source":
        os.remove('LICENSE')

    print(
        """
You are now ready to get started, however you should create a new github
repository for your new project and add your project using the following
commands (substitute REMOTE-REPOSITORY-URL with the remote repository url).

    cd {{ cookiecutter.repository_name }}
    git init
    git add --all
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin REMOTE-REPOSITORY-URL
    git push -u origin main
        """
    )