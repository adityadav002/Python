import random

names = [
    "Uncle Sharma",
    "Aunty Gupta",
    "Bablu the Rickshaw Wala",
    "Bollywood Baba",
    "Chintu from Chandni Chowk",
    "Techie Tiwari",
    "Cousin Bunty",
    "DJ Bhatura",
    "Pandit TikTokanand",
    "Swag Wale Babu"
]

actions = [
    "starts fight over pani puri spice level",
    "declares himself as next SRK",
    "mistakenly joins NASA while applying for IRCTC job",
    "gets arrested for stealing neighbor’s Wi-Fi during cricket match",
    "organizes protest to bring back Doordarshan dramas",
    "breaks Guinness record for longest WhatsApp forward",
    "opens startup to deliver samosas via drone",
    "sings item song in Parliament",
    "tried to bribe traffic cop with rasgulla",
    "claims to see Manmohan Singh blink"
]

places = [
    "Karol Bagh Metro Station",
    "Ambani’s backyard",
    "Chai tapri in Pune",
    "Bangalore traffic jam",
    "backstage at Bigg Boss",
    "Kolkata fish market",
    "Engineering college hostel",
    "Lonavala waterfall selfie spot",
    "Panvel toll naka",
    "local gym named ‘Gold’s Gym Duplicate’"
]

def play():
    name = random.choice(names)
    action = random.choice(actions)
    place = random.choice(places)
    print(f"News headLine: {name} {action} {place}\n")

while True:
    user_input = input("Ready for some masaledaar fake Indian news? (Yes/No): ").lower().strip()
    
    if user_input == 'yes':
        play()
    elif user_input == 'no':
        print("Exit.")
        break
    else:
        print("Enter valid choice.")
