
import sys
import os
import bcrypt

def getDatabase(test):
    if test==True:
        cwd = os.getcwd()
        path = cwd
        path= os.path.join(path,"testdb.csv")
        print(path)
        return path
    else:
        cwd = os.getcwd()
        path = cwd
        path= os.path.join(path,"db.csv")       
        return path


def storeUsernameAndPassword(username,password,testdb=False):
    path= getDatabase(testdb)
    doesuserexistinDb= retrieveifusernameexistsinDb(username,testdb)
    if doesuserexistinDb==True:
        return False
    if path:
        file1 = open(path, "a")  # append mode
        hashedpassword= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashpwstr= hashedpassword.decode('utf-8')
        file1.write(username)
        file1.write(",")
        file1.write(hashpwstr)        
        file1.write("\n")
        file1.close()
        return True

def retrieveifusernameandpasswordexistsinDb(username,password,testdb=False):
    path=getDatabase(testdb)
    with open(path) as file:
        for line in file:
            out1= line.split("\n")
            outs= out1[0].split(",")
            storedusername= outs[0]
            storedpassword= outs[1]
            byte_data_password = storedpassword.encode('utf-8')
            if(storedusername== username):
                if bcrypt.checkpw(password.encode('utf-8'),byte_data_password):
                    return True
                else:
                    return False
    return False

def retrieveifusernameexistsinDb(username,testdb=False):
    path=getDatabase(testdb)
    with open(path) as file:
        for line in file:
            out1= line.split("\n")
            outs= out1[0].split(",")
            storedusername= outs[0]
            if(storedusername== username):
                return True
    return False


            
            
            

def main():
    print("Welcome to System 123")
    print("Please enter details to login")
    username= input("Enter Username:")
    password= input("Enter Password:")
    checkifusernameexist= retrieveifusernameexistsinDb(username)
    if checkifusernameexist== False:
        storeUsernameAndPassword(username,password)
        #checknow if it exists in DB
        checkifusernameexist1= retrieveifusernameandpasswordexistsinDb(username,password)
        if checkifusernameexist1== True:
            print("Program Ends")

if __name__ == '__main__':
    main()
