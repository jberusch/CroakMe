# takes rpi IP as 1st & only command line arg

ssh root@$1 'screen -S backup -d -m python ~/CroakMe/main.py'

# to access terminal output in rpi: 
# screen -S backup -rd
