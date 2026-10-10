'''
Problem 1: Mutual Friends
Understand
- Find friends shared by two Villager objects.
- Return the names of those mutual friends in a list.
Plan
1. Loop through the current villager's friends.
2. Check whether each friend is also in new_contact.friends.
3. If so, add the friend's name to the result list.
Implement
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        mutuals = []
        for friend in self.friends:
            if friend in new_contact.friends:
                mutuals.append(friend.name)
        return mutuals


bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]

print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))


'''
Problem 2: Linked Up
Understand
- A linked list consists of nodes connected through their next attributes.
- Connect the four nodes in the specified order.
Plan
1. Set kk_slider.next to harriet.
2. Set harriet.next to saharah.
3. Set saharah.next to isabelle.
4. The last node points to None by default.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)


'''
Problem 3: Daily Tasks
Understand
- Add a new node to the beginning of a linked list.
- The new node becomes the head, and its next points to the previous head.
Plan
1. Create a new Node containing task.
2. Set its next to head.
3. Return the new node.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_first(head, task):
    new_node = Node(task, head)
    return new_node

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))


'''
Problem 4: Halve List
Understand
- Traverse the linked list using a pointer called current.
- Divide each node's value by two.
- Return the original head after updating the values.
Plan
1. Start at head.
2. Use a while loop to visit each node.
3. Divide current.value by 2.
4. Move to the next node.
5. Return head.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def halve_list(head):
    current = head

    while current:
        current.value = current.value / 2
        current = current.next

    return head

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))


'''
Problem 5: Remove Last
Understand
- Remove the tail, which is the last node in the linked list.
- If the list is empty, return None.
- If the list has only one node, removing the tail makes the list empty.
Plan
1. Check whether head is None or has no next node.
2. If either condition is true, return None.
3. Otherwise, traverse until current.next.next is None.
4. Set current.next to None to remove the last node.
5. Return head.
Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_tail(head):
    if head is None or head.next is None:
        return None

    current = head

    while current.next.next:
        current = current.next

    current.next = None
    return head

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))