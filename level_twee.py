'''def sumTwoIntegers(a, b):
    return a * b
    #returning something can save it into a variable. 

sumOf1and2 = sumTwoIntegers(4,2)
print(sumOf1and2)'''



# note that 'input1' is a placeholder that refers to whatever is passed in as the first argument. 
# it is not the name of the argument but the argument itself.
# else has no conditions after



def func_findmax(numbers):
    maximum = numbers[0]
    #index '0' is the first element. we cycle through the for loop, defining 'each' as a different input.
    #meaning, numbers represents '0' as the first comparative element in this list. It starts as the first max element
    #but as we cycle through, 'each' is compared to '0' as 'each' is assigned to different values
    for each in numbers:
        if each > maximum:
            maximum = each
    return maximum


234


input1 = input("What's the first input? ")
input2 = input("What's the next input? ")
input3 = input("What's the next input? ")
input4 = input("What's the final input? ")

numbers = [input1, input2, input3, input4]

#printing a variable can only be placed after you say it exists. if Alex called 'print this' in the function, we don't have the result.
result = func_findmax(numbers)
print(result) 