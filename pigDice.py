# pig dice program

if User_Total > Computer_Total:
    print("User Has Won")
    print("The User Score has {}, and the Computer has Score {}".format(User_Total,Computer_Total))

elif Computer_Total > User_Total:
    print("Computer Has Won")
    print("The User Score has {}, and the Computer has Score {}".format(User_Total,Computer_Total))
else:
    print("Match has Draw with User Score: {}, and the Computer Score: {}".format(User_Total,Computer_Total))
