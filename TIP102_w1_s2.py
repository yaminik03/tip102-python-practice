'''
Problem 1: Reverse Sentence
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should the order of the words be reversed while keeping each individual word unchanged?
What should happen if the sentence contains only one word?
P - Plan

2. Write out in plain English what you want to do:

I want to separate the sentence into individual words, reverse the order of those words, and then join them back together into a single sentence. If there is only one word, reversing it should still return the original word.

3. Translate each sub-problem into pseudocode:

Define a function called reverse_sentence with a parameter sentence

Split the sentence into a list of words

Reverse the list of words

Join the reversed words together with spaces

Return the new sentence
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))


'''
Problem 2: Goldilocks Number
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should the selected number be strictly between the minimum and maximum values?
What should the function return if there are only two numbers and therefore no middle value?
P - Plan

2. Write out in plain English what you want to do:

I want to find a number that is not the smallest and not the largest number in the list. Since all the numbers are distinct, I can sort the list and return the second number. If there are fewer than three numbers, there is no number in the middle, so I will return -1.

3. Translate each sub-problem into pseudocode:

Define a function called goldilocks_approved with a parameter nums

If the list has fewer than 3 numbers
    Return -1

Sort the numbers from smallest to largest

Return the second number in the sorted list
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1
    nums.sort()
    return nums[1]

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))


'''
Problem 3: Delete Minimum
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should the minimum element be removed from the list each time before finding the next minimum?
Should the function return a new list rather than modifying the original list?
P - Plan

2. Write out in plain English what you want to do:

I want to repeatedly find the smallest number in the list, add it to a new result list, and remove it from the original list. I will continue until there are no elements left.

3. Translate each sub-problem into pseudocode:

Define a function called delete_minimum_elements with a parameter hunny_jar_sizes

Create an empty result list

While hunny_jar_sizes is not empty
    Find the minimum element
    Add the minimum element to the result list
    Remove the minimum element from hunny_jar_sizes

Return the result list
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def delete_minimum_elements(hunny_jar_sizes):
    result = []
    while hunny_jar_sizes:
        min_element = min(hunny_jar_sizes)
        result.append(min_element)
        hunny_jar_sizes.remove(min_element)
    return result

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))


'''
Problem 4: Sum of Digits
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should each individual digit be added together rather than treating the number as one value?
What should happen when the number contains only one digit?
P - Plan

2. Write out in plain English what you want to do:

I want to look at each digit in the number and add it to a running total. I can convert the number into a string so that I can loop through each individual digit. Then I will convert each digit back into an integer and add it to the total.

3. Translate each sub-problem into pseudocode:

Define a function called sum_of_digits with a parameter num

Set total to 0

Convert num to a string

For each digit in the string
    Convert the digit to an integer
    Add the digit to total

Return total
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def sum_of_digits(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total


num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))


'''
Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
U - Understand

1. Share 2 questions you would ask to help understand the question:

What is the starting value of tigger?
Which operations increase and decrease the value of tigger?
P - Plan

2. Write out in plain English what you want to do:

I want to start tigger at 1. For every operation, I will increase tigger by 1 if the operation is "bouncy" or "flouncy". I will decrease tigger by 1 if the operation is "trouncy" or "pouncy". Finally, I will return the final value.

3. Translate each sub-problem into pseudocode:

Define a function called final_value_after_operations with a parameter operations

Set tigger to 1

For each operation in operations:
    If operation is "bouncy" or "flouncy"
        Increase tigger by 1

    Otherwise
        Decrease tigger by 1

Return tigger
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def final_value_after_operations(operations):
    tigger = 1

    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            tigger += 1
        else:
            tigger -= 1

    return tigger


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))