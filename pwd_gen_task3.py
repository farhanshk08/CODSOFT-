import random
import string

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    string1=string.ascii_lowercase
    string2=string.ascii_uppercase
    string3=string.digits
    string4=string.punctuation
    
    string5=[]
    
    string5.extend(string1)
    string5.extend(string2)
    string5.extend(string3)
    string5.extend(string4)
    
    pwdLength=int(input("Enter the length of the password: "))
    
    random.shuffle(string5)
    
    print("".join(string5[0:pwdLength]))
    print("Thanks for using the Password Generator!")
  