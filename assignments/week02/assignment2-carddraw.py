import requests

# Getting a fresh deck
deck_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
deck_response = requests.get(deck_url)
deck_data = deck_response.json()

deck_id = deck_data["deck_id"]

# Drawing 5 cards
deal_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
deal_response = requests.get(deal_url)
deal_data = deal_response.json()
cards = deal_data['cards']
hand = []
# https://stackoverflow.com/questions/17663299/creating-an-empty-set
values = set()
suits = set()

# Printing drawn cards and generate sets for later use
for card in cards:
    #https://www.w3schools.com/python/ref_string_capitalize.asp
    print(f"{card['value'].capitalize()} \t {card['suit'].capitalize()}")
    hand.append(f"{card['code']}")
    # https://www.w3schools.com/python/python_ref_set.asp
    # https://www.w3schools.com/python/python_sets.asp
    values.add(f"{card['value']}")
    suits.add(f"{card['suit']}")

# Replace words with numbers in values set
for value in values:
    if value == 'JACK':
        values.remove('JACK')
        values.add('11')
    if value == 'QUEEN':
        values.remove('QUEEN')
        values.add('12')
    if value == 'KING':
        values.remove('KING')
        values.add('13')
    if value == 'ACE':
        values.remove('ACE')
        values.add('14')

sorted_values=sorted(values)

# https://www.geeksforgeeks.org/python-list-sort-method/
hand.sort(key=lambda x: x[0])

if len(values) == 4:
    print("You have drawn a pair. Congratulations!")

if len(values) == 3:
    print("You have drawn three of a kind or two pairs. Congratulations!")

if len(suits) == 1:
    print("You have drawn a flush. Congratulations!")

if len(sorted_values) == 5:
    # https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-integers
    sorted_integers = sorted({int(x) for x in sorted_values})
    if sorted_integers[0] + 4 == sorted_integers[1] + 3 == sorted_integers[2] + 2 == sorted_integers[3] + 1 == sorted_integers[4]:
        print("You have drawn a straight. Congratulations!")
