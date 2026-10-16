'''
Problem 1: Wild Goose Chase
Understand
- Check whether the tail of the linked list points back to the head.
- Return True if it does, otherwise return False.
Plan
1. Return False if the list is empty.
2. Traverse the list using current.
3. When the tail is reached, check whether its next points to clues.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    if not clues:
        return False

    current = clues

    while current.next and current.next != clues:
        current = current.next

    return current.next == clues


clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")

clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))


'''
Problem 2: Breaking the Cycle
Understand
- Return the values of all nodes that belong to a cycle.
- Return an empty list if there is no cycle.
Plan
1. Keep a set of visited node objects.
2. Traverse the linked list.
3. If a node has already been visited, stop.
4. Once a cycle is found, collect the values of its nodes by following next until returning to the repeated node.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    visited = set()
    current = evidence

    while current and current not in visited:
        visited.add(current)
        current = current.next

    if current is None:
        return []

    cycle_start = current
    false_evidence = []

    while True:
        false_evidence.append(current.value)
        current = current.next

        if current == cycle_start:
            break

    return false_evidence


clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")

clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")

clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))



'''
Problem 3: Prioritizing Suspects
Understand
- Rearrange the linked list so nodes with values greater than threshold come first.
- Nodes with values less than or equal to threshold come afterward.
Plan
1. Create two separate linked lists using dummy nodes.
2. Add values greater than the threshold to the first list.
3. Add all other values to the second list.
4. Connect the first list to the second list.
5. Return the new head.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(suspect_ratings, threshold):
    greater_dummy = Node(0)
    smaller_dummy = Node(0)

    greater = greater_dummy
    smaller = smaller_dummy
    current = suspect_ratings

    while current:
        if current.value > threshold:
            greater.next = current
            greater = greater.next
        else:
            smaller.next = current
            smaller = smaller.next

        current = current.next

    smaller.next = None
    greater.next = smaller_dummy.next

    return greater_dummy.next if greater_dummy.next else smaller_dummy.next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))



'''
Problem 4: Puzzling It Out
Understand
- Merge two sorted linked lists into one sorted linked list.
- Reuse the original nodes instead of creating new nodes for each value.
Plan
1. Create a dummy node to start the merged list.
2. Compare the current values of both lists.
3. Attach the smaller node to the merged list.
4. Move the pointer forward in the list that supplied the node.
5. Attach any remaining nodes and return the merged head.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_timelines(known_timeline, witness_timeline):
    dummy = Node(0)
    current = dummy

    while known_timeline and witness_timeline:
        if known_timeline.value <= witness_timeline.value:
            current.next = known_timeline
            known_timeline = known_timeline.next
        else:
            current.next = witness_timeline
            witness_timeline = witness_timeline.next

        current = current.next

    if known_timeline:
        current.next = known_timeline
    else:
        current.next = witness_timeline

    return dummy.next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))


'''
Problem 5: A New Perspective
Understand
- Rotate a linked list to the right by k positions.
- Each rotation moves the last node to the front.
- If k is greater than the list length, use k % n to avoid unnecessary rotations.
Plan
1. Return the head if the list is empty or contains one node.
2. Find the list length and tail.
3. Connect the tail to the head to form a temporary circle.
4. Calculate the new tail position using n - (k % n) - 1.
5. Break the circle after the new tail and return the new head.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def rotate_right(evidence, k):
    if not evidence or not evidence.next:
        return evidence

    length = 1
    tail = evidence

    while tail.next:
        tail = tail.next
        length += 1

    k = k % length

    if k == 0:
        return evidence

    tail.next = evidence

    steps = length - k
    new_tail = evidence

    for _ in range(steps - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))