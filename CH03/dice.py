# FILE NAME - dice.py

# NAME: jace ingram
# DATE: 9-25-2024
# BRIEF DESCRIPTION:  rolls a die



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



def main():
    roll_die()

def roll_die():
    
  
    ########## ENTER YER CODE BELOW THIS LINE ##########


    import random
    user_seed = int(input("Enter a seed for the random number generation: "))
    random.seed(user_seed)
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)

    print('Die roll one is', die_one,'\nDie roll two is', die_two)







    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Die roll one is 5
Die roll two is 2

'''



'''

Enter a seed for the random number generation: 22
Die roll one is 2
Die roll two is 2

'''



'''

Enter a seed for the random number generation: -30
Die roll one is 5
Die roll two is 3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the purpose of "seeding" the random number generator?
so you can get an exact output





'''



