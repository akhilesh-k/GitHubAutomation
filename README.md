## Github Automation

**Utility script to setup project evironment with a single command.**

I have created a shell script and a python script which uses Github API that will automate the project development environment for me.

### Functionalities:

- Set up a folder
- Creates a VS-Code workspace
- Creates GitHub repository
- Adds the git remote to the git environment in directory.
- Clones the Repository
- Starts tracking everything with git add
- Push the initial commit to the repository
- Opens the project in visual studio code

### Dependecies:

- Github account
- API Token
- Python3
- JSON
- Requests

### Setup:

`cp create.py ~/`

`cp .command.sh ~/`

`source ~/command.sh`

Finally open your `.zshrc` or `.bashrc` file and add there also.

### Usage:

Run `create project_name` inside the directory where you wanna intitalize your project.

I watched a flutter tutorial by [Kalle Hallden](https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ), where he used this awesome command and voila, created a project and all live on Github within seconds. Took me few hours to figure it out and implemented it. Thanks to [Prashasy](https://github.com/prashasy) who woke up late and helped me figuring out the API things! :)))
