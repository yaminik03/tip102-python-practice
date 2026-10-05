'''
Problem 1: Planning Your Daily Work Schedule
U - Understand

1. Share 2 questions you would ask to help understand the question:

Can the same task be used twice, or do we need two different tasks?
Should the function return only True or False?
P - Plan

2. Write out in plain English what you want to do:

We need to find two different task times that add up to the available time.

We can use a set to keep track of task times we have already seen. For each task, we calculate the time we need to reach the available time. If that needed time is already in the set, we found a pair.

3. Translate each sub-problem into pseudocode:

Create an empty set called seen

For each task time:
    Calculate the needed time:
        available time - current task time

    If needed time is in seen:
        return True

    Add current task time to seen

Return False
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def find_task_pair(task_times, available_time):
    seen = set()

    for task_time in task_times:
        needed_time = available_time - task_time

        if needed_time in seen:
            return True

        seen.add(task_time)

    return False


task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))


'''
Problem 2: Minimizing Workload Gaps
U - Understand

1. Share 2 questions you would ask to help understand the question:

Are the work sessions guaranteed to be in chronological order?
Should the gap be calculated from the end of one session to the start of the next session?
P - Plan

2. Write out in plain English what you want to do:

First, sort the work sessions by their start time.

Then, compare each session with the session immediately after it. We calculate the number of minutes between the end of the current session and the start of the next session.

We keep track of the smallest gap we find.

Because the times are given as integers like 1300, we need to convert them into minutes before subtracting.

3. Translate each sub-problem into pseudocode:

Sort the work sessions by start time

Set smallest gap to infinity

For each pair of consecutive sessions:
    Convert the first session's end time to minutes
    Convert the next session's start time to minutes

    Calculate the gap

    If the gap is smaller than smallest gap:
        Update smallest gap

Return smallest gap
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def find_smallest_gap(work_sessions):
    work_sessions.sort()

    smallest_gap = float("inf")

    for i in range(len(work_sessions) - 1):
        current_end = work_sessions[i][1]
        next_start = work_sessions[i + 1][0]

        current_end_minutes = (current_end // 100) * 60 + (current_end % 100)
        next_start_minutes = (next_start // 100) * 60 + (next_start % 100)

        gap = next_start_minutes - current_end_minutes

        if gap < smallest_gap:
            smallest_gap = gap

    return smallest_gap


work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))


'''
Problem 3: Expense Tracking and Categorization
U - Understand

1. Share 2 questions you would ask to help understand the question:

Can the same expense category appear multiple times?
If multiple categories have the same highest total, which category should be returned?
P - Plan

2. Write out in plain English what you want to do:

Create a dictionary to store the total amount for each category.

For every expense, add its amount to the correct category.

After calculating all the totals, find the category with the highest total. If there is a tie, the expected output returns the first category that reached the highest total.

3. Translate each sub-problem into pseudocode:

Create an empty dictionary called totals

For each expense:
    Get the category and amount

    If the category is not in totals:
        Add the category with a value of 0

    Add the amount to the category total

Set highest category to the first category
Set highest total to its total

For each category:
    If its total is greater than highest total:
        Update highest category
        Update highest total

Return totals and highest category
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def calculate_expenses(expenses):
    totals = {}

    for category, amount in expenses:
        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    highest_category = None
    highest_total = 0

    for category in totals:
        if totals[category] > highest_total:
            highest_total = totals[category]
            highest_category = category

    return totals, highest_category


expenses = [
    ("Food", 12.5),
    ("Transport", 15.0),
    ("Accommodation", 50.0),
    ("Food", 7.5),
    ("Transport", 10.0),
    ("Food", 10.0)
]

print(calculate_expenses(expenses))


expenses_2 = [
    ("Entertainment", 20.0),
    ("Food", 15.0),
    ("Transport", 10.0),
    ("Entertainment", 5.0),
    ("Food", 25.0),
    ("Accommodation", 40.0)
]

print(calculate_expenses(expenses_2))


expenses_3 = [
    ("Utilities", 100.0),
    ("Food", 50.0),
    ("Transport", 75.0),
    ("Utilities", 50.0),
    ("Food", 25.0)
]

print(calculate_expenses(expenses_3))

'''
Problem 4: Analyzing Word Frequency
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should uppercase and lowercase versions of the same word be treated as the same word?
If multiple words have the same highest frequency, should we return all of them?
P - Plan

2. Write out in plain English what you want to do:

Convert the text to lowercase so that words like "Word" and "word" are treated the same.

Remove punctuation by keeping only letters and spaces.

Split the text into individual words.

Use a dictionary to count how many times each word appears.

Then find the highest frequency and create a list containing every word with that frequency.

3. Translate each sub-problem into pseudocode:

Convert text to lowercase

Remove punctuation

Split text into words

Create an empty dictionary

For each word:
    If word is not in dictionary:
        Add it with a count of 0

    Increase its count by 1

Find the highest word frequency

Create a list of all words with that frequency

Return the dictionary and list
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def word_frequency_analysis(text):
    text = text.lower()

    cleaned_text = ""

    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char

    words = cleaned_text.split()

    word_counts = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 0

        word_counts[word] += 1

    highest_frequency = max(word_counts.values())

    most_frequent_words = []

    for word in word_counts:
        if word_counts[word] == highest_frequency:
            most_frequent_words.append(word)

    return word_counts, most_frequent_words


text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))


'''
Problem 5: Validating HTML Tags
U - Understand

1. Share 2 questions you would ask to help understand the question:

Do closing tags need to match the most recently opened tag?
Should the function return False if there is a closing tag without a matching opening tag?
P - Plan

2. Write out in plain English what you want to do:

We can use a stack because HTML tags need to close in the reverse order that they were opened.

When we see an opening tag, we put its name onto the stack.

When we see a closing tag, we check whether it matches the most recent opening tag.

If it does not match, return False.

At the end, the stack should be empty. If it is empty, all tags were properly closed.

3. Translate each sub-problem into pseudocode:

Create an empty stack

Find each tag in the HTML string

For each tag:
    If it is an opening tag:
        Add its name to the stack

    If it is a closing tag:
        If the stack is empty:
            return False

        Remove the most recent opening tag

        If it does not match the closing tag:
            return False

If the stack is empty:
    return True

Otherwise:
    return False
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def validate_html_tags(html):
    stack = []

    tags = html.split("<")

    for tag in tags:
        if tag == "":
            continue

        tag = tag.split(">")[0]

        if tag.startswith("/"):
            closing_tag = tag[1:]

            if not stack:
                return False

            opening_tag = stack.pop()

            if opening_tag != closing_tag:
                return False

        else:
            stack.append(tag)

    return len(stack) == 0


html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))