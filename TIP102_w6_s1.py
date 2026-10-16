'''
Problem 1: Building a Playlist
Understand
- Create three nodes in order: "Uptown Funk", "Party Rock Anthem", and "Bad Romance".
- Connect each node using its next attribute.
Plan
1. Create the last node first.
2. Connect "Party Rock Anthem" to "Bad Romance".
3. Connect "Uptown Funk" to "Party Rock Anthem".
Implement
'''
class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()

bad_romance = SongNode("Bad Romance")
party_rock = SongNode("Party Rock Anthem", bad_romance)
top_hits_2010s = SongNode("Uptown Funk", party_rock)

print_linked_list(top_hits_2010s)


'''
Problem 2: Top Artists
Understand
- Count how many times each artist appears in the linked list.
- Return a dictionary containing each artist and their frequency.
Plan
1. Create an empty dictionary.
2. Traverse the linked list using current.
3. Add each artist to the dictionary or increase their count.
4. Return the dictionary.
Implement
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def get_artist_frequency(playlist):
    frequencies = {}
    current = playlist

    while current:
        if current.artist in frequencies:
            frequencies[current.artist] += 1
        else:
            frequencies[current.artist] = 1

        current = current.next

    return frequencies

playlist = SongNode("Saturn", "SZA",
            SongNode("Who", "Jimin",
            SongNode("Espresso", "Sabrina Carpenter",
            SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))


'''
Problem 3: Glitching Out
Understand
- Remove the first node that matches the given song.
- The bug occurs because current = current.next.next moves the local pointer without updating the previous node's next reference.
Plan
1. Return None if the list is empty.
2. If the head matches, return the next node.
3. Otherwise, traverse the list.
4. When the next node matches, update current.next to skip that node.
5. Return the original head.
Implement
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def remove_song(playlist_head, song):
    if not playlist_head:
        return None

    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head

    while current.next:
        if current.next.song == song:
            current.next = current.next.next
            return playlist_head

        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA",
            SongNode("Simple Twist of Fate", "Bob Dylan",
            SongNode("Dreams", "Fleetwood Mac",
            SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))


'''
Problem 4: On Repeat
Understand
- Determine whether a linked list contains a cycle.
- Use slow and fast pointers. The slow pointer moves one node at a time, and the fast pointer moves two nodes at a time.
- If they meet, a cycle exists.
Plan
1. Start both pointers at the head.
2. Move the slow pointer one step and the fast pointer two steps.
3. If they meet, return True.
4. If the fast pointer reaches the end, return False.
Implement
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")

song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))


'''
Problem 5: Looped
Understand
- Find the length of a cycle in a linked list.
- Use slow and fast pointers to detect the cycle.
- Once they meet, keep one pointer moving around the cycle to count its nodes.
Plan
1. Initialize slow and fast pointers at the head.
2. Move them one and two steps at a time.
3. If they meet, set the cycle length to 1.
4. Move another pointer around the cycle until it returns to the meeting node, counting each step.
5. Return the count, or 0 if no cycle exists.
Implement
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            length = 1
            current = slow.next

            while current != slow:
                length += 1
                current = current.next

            return length

    return 0

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")

song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))