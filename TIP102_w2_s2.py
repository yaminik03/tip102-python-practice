'''
Problem 1: Most Endangered Species
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should I return the name of the species with the smallest population?
If two species have the same population, should I return the one that appears first?
P - Plan

2. Write out in plain English what you want to do:

I want to look through each species and find the one with the smallest population. I will keep track of the species with the lowest population and return its name.

3. Translate each sub-problem into pseudocode:

Set the first species as the most endangered
Loop through the species list
If the current species has a smaller population:
    Update the most endangered species
Return its name
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def most_endangered(species_list):
    most_endangered = species_list[0]

    for species in species_list:
        if species["population"] < most_endangered["population"]:
            most_endangered = species

    return most_endangered["name"]


species_list = [
    {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
    {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
    {"name": "Vaquita", "habitat": "Marine", "population": 10}
]

print(most_endangered(species_list))


'''
Problem 2: Identifying Endangered Species
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should I count every observed species that appears in the endangered species string?
Are uppercase and lowercase species considered different?
P - Plan

2. Write out in plain English what you want to do:

I want to check each species in observed_species and count it if it is also in endangered_species.

3. Translate each sub-problem into pseudocode:

Create a set of endangered species
Set the count to 0
Loop through observed species
If the species is in the endangered set:
    Increase the count
Return the count
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def count_endangered_species(endangered_species, observed_species):
    endangered = set(endangered_species)
    count = 0

    for species in observed_species:
        if species in endangered:
            count += 1

    return count


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1))
print(count_endangered_species(endangered_species2, observed_species2))


'''
Problem 3: Navigating the Research Station
U - Understand

1. Share 2 questions you would ask to help understand the question:

Does the journey always start at index 0?
Should I add the distance between every consecutive observation point?
P - Plan

2. Write out in plain English what you want to do:

I want to create a dictionary that maps each observation point to its index. Then I will start at index 0, find each requested observation, calculate the distance from the previous observation, and add the distances together.

3. Translate each sub-problem into pseudocode:

Create a dictionary mapping each character to its index
Set current position to 0
Set total time to 0

Loop through each observation:
    Find its index
    Add the absolute difference between current position and new position
    Update current position

Return total time
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def navigate_research_station(station_layout, observations):
    positions = {}

    for i, letter in enumerate(station_layout):
        positions[letter] = i

    current_position = 0
    total_time = 0

    for observation in observations:
        new_position = positions[observation]
        total_time += abs(current_position - new_position)
        current_position = new_position

    return total_time


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))
print(navigate_research_station(station_layout2, observations2))


'''
Problem 4: Prioritizing Endangered Species Observations
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should species in priority_species appear in the exact order given?
Should species not in priority_species be sorted alphabetically?
P - Plan

2. Write out in plain English what you want to do:

I want to put the priority species first in the order given. Then I will add all species that are not priority species in ascending order.

3. Translate each sub-problem into pseudocode:

Create an empty result list

For each species in priority_species:
    Add every matching species from observed_species

Find species that are not in priority_species
Sort those species
Add them to the result

Return the result
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def prioritize_observations(observed_species, priority_species):
    result = []

    for species in priority_species:
        for observed in observed_species:
            if observed == species:
                result.append(observed)

    remaining = []

    for species in observed_species:
        if species not in priority_species:
            remaining.append(species)

    remaining.sort()
    result.extend(remaining)

    return result


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2))


'''
Problem 5: Calculating Conservation Statistics
U - Understand

1. Share 2 questions you would ask to help understand the question:

Should I repeatedly remove the smallest and largest population?
Should I count an average only once if the same average occurs multiple times?
P - Plan

2. Write out in plain English what you want to do:

I want to repeatedly find the smallest and largest population, calculate their average, and keep track of the averages in a set. The size of the set will tell me how many distinct averages there are.

3. Translate each sub-problem into pseudocode:

Sort the populations
Create an empty set for averages
Set left pointer to the beginning
Set right pointer to the end

While left is less than right:
    Calculate the average of the smallest and largest
    Add the average to the set
    Move left forward
    Move right backward

Return the size of the set
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def distinct_averages(species_populations):
    species_populations.sort()

    averages = set()
    left = 0
    right = len(species_populations) - 1

    while left < right:
        average = (species_populations[left] + species_populations[right]) / 2
        averages.add(average)

        left += 1
        right -= 1

    return len(averages)


species_populations1 = [4, 1, 4, 0, 3, 5]
species_populations2 = [1, 100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2))