# FILE NAME - password.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



def main():
    generate_password()

def generate_password():

  
    ########## ENTER YER CODE BELOW THIS LINE ##########

    import random
    import string
    generate_password = int(input("Enter a seed for the random number generation: "))
    random.seed(generate_password)
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = 8
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"your random password is:{password}")



    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Your random password is:
_fUhI78-

'''



'''

Enter a seed for the random number generation: 22
Your random password is:
#hAtO21(

'''



'''

Enter a seed for the random number generation: 0
Your random password is:
)yNbI87)

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 






2. What value do you see in the `string` module?






'''



