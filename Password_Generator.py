#need some revisions on this

#important modules for Password Generator
import random 
import string

def main():
    print("Welcome to my Password generator!")

#set an inputted number to variable length

    length = int(input("\nEnter Password length: "))

#data
    ipis_ni_pards = string.ascii_letters
    manok_ni_bobby = string.punctuation
    pards_vs_bobby_sabong = string.digits
#adding data's    
    all = ipis_ni_pards + manok_ni_bobby + pards_vs_bobby_sabong
    
    password = "".join(random.sample(all, length))
    
    print(password)
    
    
#to execute the main function    
main()