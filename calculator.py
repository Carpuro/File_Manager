import math

'Welcome message and menu options'
def welcomeMessage():
    print ("Welcome to Carlos Pulido's Calculator")
    print ("Please, select the operation to perform")
    print ("1. Addition")
    print ("2. Substraction" )
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Exponentiation")
    print ("6. Square Root")
    print ("7. Sine")
    print ("8. Cosine")
    print ("9. Tangent")

    operationOption = int(input("Enter the operation number: "))
    return (operationOption)


def defineVariables():
    num1 = float(input("Submit the first number: "))
    num2 = float(input("If aplicable submit the second number: "))
    return(num1, num2)


def operationChoice(operationOption, num1, num2):
    operationResult = float

    if   operationOption ==1:
        operationResult = num1+num2                 #Addition Operation
    elif operationOption ==2:
        operationResult = num1-num2                 #Substraction Operation
    elif operationOption ==3:
        operationResult = num1*num2                 #Multiplication Operation
    elif operationOption ==4:
        operationResult = num1/num2                 #Division Operation
    elif operationOption ==5:
        operationResult = math.pow(num1, num2)      #Potentiation Operation
    elif operationOption ==6:
        operationResult = math.sqrt(num1)           #Square Root Operation
    elif operationOption ==7:
        operationResult = math.sin(num1)            #Sine Operation
    elif operationOption ==8:
        operationResult = math.cos(num1)            #Cosine Operation
    elif operationOption ==9:
        operationResult = math.tan(num1)            #Tangent Operation             
    else:
        operationResult = ("Option no available, please try again")    
    return(operationResult)

def repeatCalculator():
    while True:
        welcomeMessage()
        operationOption = welcomeMessage()
        num1, num2 = defineVariables()
        result = operationChoice(operationOption, num1, num2)
        print("The result is: ", result)
        repeatAnswer = input ("Do you want to perform another calculation (yes/no)")
        if repeatAnswer.lower() != "yes":
            print ("Thank you for using the Carlos Pulido's Calculator")
            break

repeatCalculator()