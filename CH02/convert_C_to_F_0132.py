

# NAME: Jace
# DATE: Ingram
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience



def main():
    convert_C_to_F()



def convert_C_to_F():
    
    # Don't forget to cast user input as a float!
    
    ########## ENTER YER CODE BELOW THIS LINE ##########

    Celsius = float(input("Enter a Temperature in celsius:"))
    Formula = float(9/5)
    Fahrenheit = ({Celsius} * {Formula} + 32)

    print(f"{Celsius} degrees Celsius is {Fahrenheit} degrees fahrenheit")
    






    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?





2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?





'''
