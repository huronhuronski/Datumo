<h3>Python app for <u>Datumo</u> recruitment process.</h3>

Application takes text file with list of numbers as an input and serves back output.txt file containing only pairs 
of numbers that add up to 12. If number was once used, it cannot form another pair. Application accepts only .txt files
for now, but list in it can be written sloppy, not necessarily in python notation, there can be other characters than 
numeric, app also recognizes decimal numbers. Does not yet read more than one line from text file.

To run the app in docker container, open terminal and:

1. initialize new local repo `git init` in desired location
2. `git pull https://github.com/huronhuronski/Datumo.git`

(or
1. clone remote github repo with `git clone https://github.com/huronhuronski/Datumo.git` in desired location
2. change directory to cloned repo `cd Datumo`)

3. build local docker image: `docker build --tag datumo-app .`
4. run image in a container: `docker run -p 5000:5000 datumo-app`
5. go to http://localhost:5000/

App should be up ready to accept first text file!

