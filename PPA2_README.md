#Running Instructions
If running the Jenkinsfile make sure that there are no docker containers named app and newm. Additionally, make sure that there isn't a 
docker network named Web before running the Jenkinsfile.
If you are running the normal program then make sure that you have a mysql database running before running the actual program. Additionally,
make sure that your mysql contains a database called BMI and another caller RETIREMENT. Then you will want to go into BMI_DB.py and 
RETIREMENT.py and change the parameters inside the connect called to your database host, username, and password. Lastly, you will want to
run the PPA2.py program to begin using the program
