dictionary = {'piece': 'a separate or limited portion or quantity of something',
              'animal': 'any member of the kingdom Animalia, comprising multicellular organisms that have a well-defined shape and usually limited growth, can move voluntarily, actively acquire food and digest it internally',
              'eat': 'to take into the mouth and swallow for nourishment',
              'airplane': 'a heavier-than-air aircraft kept aloft by the upward thrust exerted by the passing air on its fixed wings and driven by propellers, jet propulsion, etc.'}

keys = list(dictionary.keys())
values = list(dictionary.values())
lens = [len(x) for x in values]

min = min(lens)
max = max(lens)
index_min = lens.index(min)
index_max = lens.index(max)

print("Max is " + keys[index_max] + ": " + values[index_max])
print("Min is " + keys[index_min] + ": " + values[index_min])
