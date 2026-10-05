'''
Problem 1: NFT Name Extractor
U - Understand

1. Share 2 questions you would ask to help understand the question:

Does each dictionary in the collection contain a "name" key?
Should the function return the NFT names in the same order as they appear in the collection?
P - Plan

2. Write out in plain English what you want to do:

I want to create an empty list to store the NFT names. Then I will loop through each NFT in the collection, get the value associated with the "name" key, and add it to the list. Finally, I will return the list of names.

3. Translate each sub-problem into pseudocode:

Define a function called extract_nft_names with a parameter nft_collection

Create an empty list called nft_names

For each NFT in nft_collection:
    Get the NFT's name
    Add the name to nft_names

Return nft_names
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def extract_nft_names(nft_collection):
    nft_names = []

    for nft in nft_collection:
        nft_names.append(nft["name"])

    return nft_names


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))


'''
Problem 2: NFT Collection Review
U - Understand

1. Share 2 questions you would ask to help understand the question:

What is wrong with using += to add each NFT name to the list?
Should each NFT name be stored as one complete string in the result list?
P - Plan

2. Write out in plain English what you want to do:

The bug is that nft_names += nft["name"] adds the individual characters of the NFT name to the list instead of adding the entire name as one element. I will replace += with .append() so that each complete NFT name is added to the list.

3. Translate each sub-problem into pseudocode:

Define a function called extract_nft_names with a parameter nft_collection

Create an empty list called nft_names

For each NFT in nft_collection:
    Add the entire NFT name to nft_names

Return nft_names
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def extract_nft_names(nft_collection):
    nft_names = []

    for nft in nft_collection:
        nft_names.append(nft["name"])

    return nft_names


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))


'''
Problem 3: Identify Popular Creators
U - Understand

1. Share 2 questions you would ask to help understand the question:

How many NFTs must a creator have for them to be considered popular?
Should each popular creator appear only once in the result?
P - Plan

2. Write out in plain English what you want to do:

I want to count how many NFTs each creator has made. I will use a dictionary where each creator is a key and their NFT count is the value. After counting all the creators, I will loop through the dictionary and add creators with more than one NFT to the result list.

3. Translate each sub-problem into pseudocode:

Define a function called identify_popular_creators with a parameter nft_collection

Create an empty dictionary called creator_counts

For each NFT in nft_collection:
    Get the creator

    If the creator is not in creator_counts:
        Add the creator with a count of 0

    Increase the creator's count by 1

Create an empty list called popular_creators

For each creator in creator_counts:
    If the creator's count is greater than 1:
        Add the creator to popular_creators

Return popular_creators
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def identify_popular_creators(nft_collection):
    creator_counts = {}

    for nft in nft_collection:
        creator = nft["creator"]

        if creator not in creator_counts:
            creator_counts[creator] = 0

        creator_counts[creator] += 1

    popular_creators = []

    for creator in creator_counts:
        if creator_counts[creator] > 1:
            popular_creators.append(creator)

    return popular_creators


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))


'''
Problem 4: NFT Collection Statistics
U - Understand

1. Share 2 questions you would ask to help understand the question:

What should the function return if the NFT collection is empty?
Should the average be calculated using the "value" of every NFT?
P - Plan

2. Write out in plain English what you want to do:

I want to calculate the total value of all NFTs and divide it by the number of NFTs. I will use a loop to add each NFT's value to a total. If the collection is empty, I will return 0 instead of trying to divide by zero.

3. Translate each sub-problem into pseudocode:

Define a function called average_nft_value with a parameter nft_collection

If the collection is empty:
    Return 0

Set total_value to 0

For each NFT in nft_collection:
    Add the NFT's value to total_value

Calculate the average by dividing total_value by the number of NFTs

Return the average
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def average_nft_value(nft_collection):
    if len(nft_collection) == 0:
        return 0

    total_value = 0

    for nft in nft_collection:
        total_value += nft["value"]

    return total_value / len(nft_collection)


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]

print(average_nft_value(nft_collection_2))

nft_collection_3 = []

print(average_nft_value(nft_collection_3))


'''
Problem 5: NFT Tag Search
U - Understand

1. Share 2 questions you would ask to help understand the question:

Can each NFT have multiple tags?
Should the function return the names of every NFT that contains the requested tag?
P - Plan

2. Write out in plain English what you want to do:

I want to search through each collection and then each NFT inside that collection. For every NFT, I will check its list of tags. If the requested tag is present, I will add that NFT's name to the result list. After checking all collections and NFTs, I will return the list.

3. Translate each sub-problem into pseudocode:

Define a function called search_nft_by_tag with parameters nft_collections and tag

Create an empty list called matching_nfts

For each collection in nft_collections:
    For each NFT in the collection:
        If tag is in the NFT's tags:
            Add the NFT's name to matching_nfts

Return matching_nfts
I - Implement

4. Translate the pseudocode into Python and share your final answer:
'''
def search_nft_by_tag(nft_collections, tag):
    matching_nfts = []

    for collection in nft_collections:
        for nft in collection:
            if tag in nft["tags"]:
                matching_nfts.append(nft["name"])

    return matching_nfts


nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))