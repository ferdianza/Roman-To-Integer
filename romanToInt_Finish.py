#introduce
#this is program to covert roman number to integer
#so the aloritm is :
    #1. the first number if less then second number it will subtrac
    #2. the first number if more then second number it will add

    #NOTE
    #1. if it substraction it will be just for first and second number, and the second number can't be process with the thirth number,
    #so the thirtd number will process with next number
    #2. if it addition it will be procress with next number until we found substraction or number finish


#First I make a function to covert roman string to int:
def romanToInt(roman):
    result = 0
    if roman in "Ii":
        result = 1
    elif roman in "Vv":
        result = 5
    elif roman in "Xx":
        result = 10
    elif roman in "Ll":
        result = 50
    elif roman in "Cc":
        result = 100
    elif roman in "Dd":
        result = 500
    elif roman in "Mm":
        result = 1000
    else:
        result = 0
    return result
#this is form. so user can input the roman string

user_in = input("Enter the roman number: ")

# variable
v1 = 0 #variable for first string
v2 = 0 #variable for second string
total = 0 #total result
subs = False #this boolean to check substrac action


for rom in range(len(user_in)): #it looping by string length
    v1 = romanToInt(user_in[rom]) #v1 will equal with function base on index string user

    #it is if when rom+1 is less then lenght of string to prevent function out of range because over than sting lenght
    if rom+1 < len(user_in):

        v2 = romanToInt(user_in[rom+1::]) #v2 will equal with function base on index 1 and so on, remember index start by 0

        if v2 == 0: #because v2 is index1 and soon so it will storage more then 1 string so function will give 0 result
            v2 = romanToInt(user_in[rom+1]) #so to avoid out of range error, this index+1 will storage because v2 is more than 1 string

            if v1 < v2: #this is to substrac because v1 less then v2
                v1 = v2 - v1
                total += v1
                subs = True #this boolean is important to inform program that substraction is happened then the second number will not process with thirts number

            elif total == 0: #this for 1st number, because total will be 0 and first number not less then second number
                total += v1

            elif total < v1 or subs == True: #if result less then v1 or ther is have substrac number before so program will skip this by give 0
                v1 = 0

            else:
                total += v1

        #if rom+1 equal with lengt string so it will be last number in roman will calculation

        #but it will check if any substrac before this command will not running

        elif v1 >= v2 and subs == False: #no substrack before program will add v1 to total
            total += v1

        elif v1 >= v2 and subs == True : #yes any substrac before so program will make the value 0
            v1 = 0

        else:
            total -= v1

    # for the last number have not v2
    else:
        total += v1


print("the integer number = " + str(total))