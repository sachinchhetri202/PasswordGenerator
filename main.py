''' 
    * Generate a strong password for yourself using Python 
    * @author Sachin Chhetri <sachinchhetri202@gmail.com>
    * Use of Array, Random and exceptions handle.  
'''
    
import string
import random

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    # print(s1)
    s2 = string.ascii_lowercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    while True:
        try:
            pwlen = int(input("Enter desired password length: \n")) 
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            # print(s) ******  THIS prints out the sorted string stored in s   ******
            random.shuffle(s)   # suffling the s list with this method
            # print(s) ******  Prints out the suffeled version of s  *****
            a = ("".join(s[0:pwlen]))
            print("The password we generated for you is:")
            print(a)
            print("\n")
        except ValueError:
            print("Please enter a valid digit and try again.\n")
    
