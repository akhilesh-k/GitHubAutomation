#!/bin/bash

function create() {
    cd
    python3 create.py $1
    cd /Users/Your_Project_Directory/$1
    git init
    git remote add origin https://github.com/your_user_name/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -f origin master
    code .
}