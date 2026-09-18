'''
Problem 1: Festival Lineup
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should each artist be mapped to the set time at the same index?
What should the function return if both lists are empty?
P - Plan

2. Write out in plain English what you want to do:

I want to create a dictionary where each artist is matched with their set time. I can use the index of each artist to find the matching set time.

3. Translate each sub-problem into pseudocode:

Create an empty dictionary
Loop through the artists using their indexes
Add each artist as a key
Add the matching set time as the value
Return the dictionary
I - Implement

4. Translate the pseudocode into Python and share your final answer:
    '''
def lineup(artists, set_times):
    schedule = {}

    for i in range(len(artists)):
        schedule[artists[i]] = set_times[i]

    return schedule


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


'''
Problem 2: Planning App
U - Understand

1. Share 2 questions you would ask to help understand the question:

What should be returned if the artist is in the schedule?
What should be returned if the artist is not in the schedule?
P - Plan

2. Write out in plain English what you want to do:

I want to check if the artist exists in the festival schedule. If they exist, I will return their information. Otherwise, I will return a message saying the artist was not found.

3. Translate each sub-problem into pseudocode:

Check if artist is in festival_schedule
If it is:
    Return the artist's information
Otherwise:
    Return {"message": "Artist not found"}
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {"message": "Artist not found"}


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule))
print(get_artist_info("Taylor Swift", festival_schedule))


'''
Problem 3: Ticket Sales
U - Understand

1. Share 2 questions you would ask to help understand the question:

Are the dictionary values the number of tickets sold?
Should the function add the ticket sales for every ticket type?
P - Plan

2. Write out in plain English what you want to do:

I want to add together all of the ticket numbers in the dictionary and return the total.

3. Translate each sub-problem into pseudocode:

Create a total starting at 0
Loop through the values in ticket_sales
Add each value to total
Return total
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def total_sales(ticket_sales):
    total = 0

    for tickets in ticket_sales.values():
        total += tickets

    return total


ticket_sales = {
    "Friday": 200,
    "Saturday": 1000,
    "Sunday": 800,
    "3-Day Pass": 2500
}

print(total_sales(ticket_sales))


'''
Problem 4: Scheduling Conflict
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should an artist only be included if they are in both schedules?
Should the set times also have to be exactly the same?
P - Plan

2. Write out in plain English what you want to do:

I want to find artists that appear in both venue schedules and have the same set time. I will store those artists and times in a new dictionary.

3. Translate each sub-problem into pseudocode:

Create an empty dictionary
Loop through the artists in venue1_schedule
If the artist is also in venue2_schedule:
    If both set times are the same:
        Add the artist and set time to the dictionary
Return the dictionary
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}

    for artist in venue1_schedule:
        if artist in venue2_schedule:
            if venue1_schedule[artist] == venue2_schedule[artist]:
                conflicts[artist] = venue1_schedule[artist]

    return conflicts


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))


'''
Problem 5: Best Set
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should I count how many times each artist appears in the votes?
If two artists have the same number of votes, can I return either artist?
P - Plan

2. Write out in plain English what you want to do:

I want to count how many votes each artist receives. Then I want to find the artist with the highest number of votes.

3. Translate each sub-problem into pseudocode:

Create an empty dictionary for vote counts
Loop through each artist in votes
If the artist is already in the dictionary:
    Increase their count by 1
Otherwise:
    Add the artist with a count of 1

Find the artist with the highest vote count
Return that artist
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def best_set(votes):
    counts = {}

    for artist in votes.values():
        if artist in counts:
            counts[artist] += 1
        else:
            counts[artist] = 1

    best_artist = None
    highest_votes = 0

    for artist in counts:
        if counts[artist] > highest_votes:
            highest_votes = counts[artist]
            best_artist = artist

    return best_artist


votes1 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))