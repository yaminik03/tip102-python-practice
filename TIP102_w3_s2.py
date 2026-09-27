'''
Problem 1: Manage Performance Stage Changes
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should "Cancel" remove the most recently scheduled performance?
Should "Reschedule" bring back the most recently canceled performance?
P - Plan

2. Write out in plain English what you want to do:

Use two stacks:

One stack stores scheduled performances.
One stack stores canceled performances.
"Schedule X" adds X to the scheduled stack.
"Cancel" removes the most recent scheduled performance and puts it in the canceled stack.
"Reschedule" removes the most recently canceled performance and adds it back to the scheduled stack.

3. Translate each sub-problem into pseudocode:

Create scheduled stack
Create canceled stack

For each change:
    If change starts with "Schedule":
        Get the performance ID
        Add it to scheduled

    Else if change is "Cancel":
        If scheduled is not empty:
            Remove last scheduled performance
            Add it to canceled

    Else if change is "Reschedule":
        If canceled is not empty:
            Remove last canceled performance
            Add it to scheduled

Return scheduled
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def manage_stage_changes(changes):
    scheduled = []
    canceled = []

    for change in changes:
        if change.startswith("Schedule"):
            performance = change.split()[1]
            scheduled.append(performance)

        elif change == "Cancel":
            if scheduled:
                performance = scheduled.pop()
                canceled.append(performance)

        elif change == "Reschedule":
            if canceled:
                performance = canceled.pop()
                scheduled.append(performance)

    return scheduled


print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]))
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))



'''
Problem 2: Queue of Performance Requests
U - Understand

1. Share 2 questions you would ask to help understand the question:

Does a higher number mean higher priority?
If two requests have the same priority, should they stay in their original order?
P - Plan

2. Write out in plain English what you want to do:

Each request contains a priority and a performance name. We need to process the highest priority first.

We can sort the requests by their priority from highest to lowest and then return only the performance names.

3. Translate each sub-problem into pseudocode:

Sort requests by priority from highest to lowest

Create an empty result list

For each request:
    Add the performance name to result

Return result
I - Implement
'''
def process_performance_requests(requests):
    requests.sort(reverse=True)

    result = []

    for priority, performance in requests:
        result.append(performance)

    return result


print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))


'''
Problem 3: Collecting Points at Festival Booths
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should every booth's points be collected?
Should the function return the total number of points?
P - Plan

2. Write out in plain English what you want to do:

Use a stack to store all the point values. Then remove each value from the stack and add it to a total.

3. Translate each sub-problem into pseudocode:

Create an empty stack
Create total = 0

For each point:
    Add point to stack

While stack is not empty:
    Remove the top point
    Add it to total

Return total
I - Implement
'''
def collect_festival_points(points):
    stack = []

    for point in points:
        stack.append(point)

    total = 0

    while stack:
        total += stack.pop()

    return total


print(collect_festival_points([5, 8, 3, 10]))
print(collect_festival_points([2, 7, 4, 6]))
print(collect_festival_points([1, 5, 9, 2, 8]))


'''
Problem 4: Festival Booth Navigation
U - Understand

1. Share 2 questions you would ask to help understand the question:

Does "back" remove the most recently visited booth?
If "back" is used when there are no booths, should we simply do nothing?
P - Plan

2. Write out in plain English what you want to do:

Use a stack to keep track of the booths visited.

If the clue is a number, add it to the stack.
If the clue is "back", remove the most recently visited booth if one exists.
Return the remaining stack.

3. Translate each sub-problem into pseudocode:

Create an empty stack

For each clue:
    If clue is "back":
        If stack is not empty:
            Remove the last booth
    Otherwise:
        Add the booth to the stack

Return the stack
I - Implement
'''
def booth_navigation(clues):
    stack = []

    for clue in clues:
        if clue == "back":
            if stack:
                stack.pop()
        else:
            stack.append(clue)

    return stack


clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues))

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues))

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues))



'''
Problem 5: Merge Performance Schedules
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should we always start with the first character of schedule1?
What should happen when one schedule runs out of characters?
P - Plan

2. Write out in plain English what you want to do:

Use two pointers:

One points to schedule1.
One points to schedule2.

Add one character from each schedule at a time. When one schedule ends, add the remaining characters from the other schedule.

3. Translate each sub-problem into pseudocode:

Create an empty result
Set pointer1 = 0
Set pointer2 = 0

While either pointer is still inside its schedule:
    If pointer1 is valid:
        Add schedule1[pointer1]
        Move pointer1

    If pointer2 is valid:
        Add schedule2[pointer2]
        Move pointer2

Return result
I - Implement
'''
def merge_schedules(schedule1, schedule2):
    result = []
    left = 0
    right = 0

    while left < len(schedule1) or right < len(schedule2):
        if left < len(schedule1):
            result.append(schedule1[left])
            left += 1

        if right < len(schedule2):
            result.append(schedule2[right])
            right += 1

    return "".join(result)


print(merge_schedules("abc", "pqr"))
print(merge_schedules("ab", "pqrs"))
print(merge_schedules("abcd", "pq"))