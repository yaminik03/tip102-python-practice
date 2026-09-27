'''
Problem 1: Post Format Validator
U - Understand

1. Share 2 questions you would ask to help understand the question:

Do opening tags need to be closed with the matching type of closing tag?
Do the tags need to be closed in the reverse order that they were opened?
P - Plan

2. Write out in plain English what you want to do:

I want to use a stack to keep track of opening tags. When I see an opening tag, I will add it to the stack. When I see a closing tag, I will check whether it matches the most recent opening tag. At the end, the stack must be empty.

3. Translate each sub-problem into pseudocode:

Create an empty stack

Loop through each character in posts:
    If it is an opening tag:
        Add it to the stack
    Otherwise:
        If the stack is empty:
            Return False
        Remove the top tag from the stack
        If the tags do not match:
            Return False

Return True if the stack is empty
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def is_valid_post_format(posts):
    stack = []

    matching_tags = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for tag in posts:
        if tag in "([{":
            stack.append(tag)
        else:
            if not stack:
                return False

            opening_tag = stack.pop()

            if opening_tag != matching_tags[tag]:
                return False

    return len(stack) == 0


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))


'''
Problem 2: Reverse User Comments Queue
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should the comments be returned in the exact reverse order?
Should I use a stack to store and remove the comments?
P - Plan

2. Write out in plain English what you want to do:

I want to use a stack because a stack follows Last In, First Out. I will add every comment to the stack and then remove each comment from the top to create the reversed list.

3. Translate each sub-problem into pseudocode:

Create an empty stack
Create an empty result list

Loop through each comment:
    Add the comment to the stack

While the stack is not empty:
    Remove the top comment
    Add it to the result

Return the result
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def reverse_comments_queue(comments):
    stack = []
    result = []

    for comment in comments:
        stack.append(comment)

    while stack:
        result.append(stack.pop())

    return result


print(reverse_comments_queue([
    "Great post!",
    "Love it!",
    "Thanks for sharing."
]))

print(reverse_comments_queue([
    "First!",
    "Interesting read.",
    "Well written."
]))



'''
Problem 3: Check Symmetry in Post Titles
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should spaces, punctuation, and uppercase/lowercase differences be ignored?
Should I compare characters from both ends toward the middle?
P - Plan

2. Write out in plain English what you want to do:

First, I will create a version of the title containing only letters and convert everything to lowercase. Then I will use two pointers, one at the beginning and one at the end. I will compare the characters and move the pointers toward the middle.

3. Translate each sub-problem into pseudocode:

Create a cleaned version of the title:
    Keep only letters
    Convert letters to lowercase

Set left pointer to the beginning
Set right pointer to the end

While left is less than right:
    If the characters are different:
        Return False
    Move left forward
    Move right backward

Return True
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def is_symmetrical_title(title):
    cleaned_title = ""

    for char in title:
        if char.isalpha():
            cleaned_title += char.lower()

    left = 0
    right = len(cleaned_title) - 1

    while left < right:
        if cleaned_title[left] != cleaned_title[right]:
            return False

        left += 1
        right -= 1

    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))


'''
Problem 4: Engagement Boost
U - Understand

1. Share 2 questions you would ask to help understand the question:

Is the input already sorted in non-decreasing order?
Should I use two pointers to compare the absolute values at the beginning and end?
P - Plan

2. Write out in plain English what you want to do:

Because the numbers are already sorted, the largest square will come from either the most negative number on the left or the largest positive number on the right. I will use two pointers and place the larger square at the end of the result.

3. Translate each sub-problem into pseudocode:

Create a result list with the same length
Set left pointer to the beginning
Set right pointer to the end
Set position to the last position

While left <= right:
    Square the left number
    Square the right number

    If left square is larger:
        Put left square at position
        Move left forward
    Otherwise:
        Put right square at position
        Move right backward

    Move position backward

Return result
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def engagement_boost(engagements):
    # Create a result list with the same size as the input
    result = [0] * len(engagements)

    # Start one pointer at the beginning
    left = 0

    # Start the other pointer at the end
    right = len(engagements) - 1

    # We will fill the result from right to left
    position = len(engagements) - 1

    # Continue until the two pointers meet
    while left <= right:
        # Square the values at both pointers
        left_square = engagements[left] * engagements[left]
        right_square = engagements[right] * engagements[right]

        # Put the larger square at the current position
        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1

        # Move to the next position from the right
        position -= 1

    return result


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))



'''
Problem 5: Content Cleaner
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should a lowercase and uppercase version of the same letter cancel each other out?
Should I continue checking the string after removing a pair because new pairs can be created?
P - Plan

2. Write out in plain English what you want to do:

I will use a stack. For each character, I will check the character at the top of the stack. If the two characters are the same letter but have different capitalization, they cancel each other out. Otherwise, I will add the new character to the stack.

3. Translate each sub-problem into pseudocode:

Create an empty stack

Loop through each character:
    If the stack is not empty:
        Check the character at the top of the stack
        If they are the same letter with different capitalization:
            Remove the top character
            Continue

    Add the current character to the stack

Return the stack as a string
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def clean_post(post):
    stack = []

    for char in post:
        if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


print(clean_post("poOost"))
print(clean_post("abBAcC"))
print(clean_post("s"))