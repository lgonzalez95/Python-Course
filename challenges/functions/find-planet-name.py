def get_planet(planed_id):
    planets = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune',
               9: 'Pluto'}
    if planets.get(planed_id) is None:
        return "Invalid planet name"
    else:
        return planets.get(planed_id)


print(get_planet(11))
