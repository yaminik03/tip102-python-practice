'''
Problem 1: Hundred Acre Wood
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should the function take any parameters?
Should the function print the message or return it?

P - Plan

2. Write out in plain English what you want to do:

I want to create a function called welcome() that prints the exact message "Welcome to The Hundred Acre Wood!". The function does not need any parameters.

3. Translate each sub-problem into pseudocode:
Define a function called welcome
    Print "Welcome to The Hundred Acre Wood!"

I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''

def welcome():
    print("Welcome to The Hundred Acre Wood!")
    
welcome()


'''
Problem 2: Greeting
U - Understand
1. Share 2 questions you would ask to help understand the question:

What information should the name parameter contain?
Should the function print the greeting or return it?
P - Plan

2. Write out in plain English what you want to do:

I want to create a function called greeting() that accepts a person's name as a parameter. The function will use that name to create and print the required greeting message.

3. Translate each sub-problem into pseudocode:
   Define a function called greeting with a parameter called name
       Create a greeting using the name
       Print the greeting
       
I - Implement

4. Translate the pseudocode into Python and share your final answer:
''' 

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")


greeting("Michael")
greeting("Winnie the Pooh")


'''
Problem 3: Catchphrase
U - Understand

1. Share 2 questions you would ask to help understand the question:

What should happen if the character is one of the four characters listed in the table?
What should happen if the character is not in the table?
P - Plan

2. Write out in plain English what you want to do:

I want to create a function called print_catchphrase() that accepts a character's name. I will use conditional statements to check which character was provided and print that character's catchphrase. If the character is not recognized, I will print the message saying that I do not know their catchphrase.

3. Translate each sub-problem into pseudocode:
Define a function called print_catchphrase with a parameter character

If character is "Pooh"
    Print "Oh bother!"

Else if character is "Tigger"
    Print "TTFN: Ta-ta for now!"

Else if character is "Eeyore"
    Print "Thanks for noticing me."

Else if character is "Christopher Robin"
    Print "Silly old bear."

Otherwise
    Print "Sorry! I don't know <character>'s catchphrase!"
    
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)


'''
Problem 4: Return Item
U - Understand

1. Share 2 questions you would ask to help understand the question:

What should the function return if x is outside the valid range of indexes?
Since the list is 0-indexed, should the first element be at index 0?
P - Plan

2. Write out in plain English what you want to do:

I want to create a function called get_item() that takes a list and an index. I will check whether the index is valid. If it is valid, I will return the element at that index. If it is not valid, I will return None.

3. Translate each sub-problem into pseudocode:
Define a function called get_item with parameters items and x

If x is greater than or equal to the length of items
    Return None

Otherwise
    Return the element at index x
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def get_item(items, x):
    if x >= len(items):
        return None
    return items[x]

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))


'''
Problem 5: Total Honey
U - Understand

1. Share 2 questions you would ask to help understand the question:

What should the function return if the list is empty?
Are we allowed to use the built-in sum() function?
P - Plan

2. Write out in plain English what you want to do:

I want to create a function called sum_honey() that adds all the numbers in the list. I will create an accumulator variable starting at 0, then use a for loop to add each jar's amount to the accumulator. Finally, I will return the total.

3. Translate each sub-problem into pseudocode:

Define a function called sum_honey with a parameter hunny_jars

Set total to 0

For each jar in hunny_jars
    Add the jar amount to total

Return total
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def sum_honey(hunny_jars):
    total = 0

    for jar in hunny_jars:
        total += jar

    return total


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))
