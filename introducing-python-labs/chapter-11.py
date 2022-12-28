# all paths
import sys as system
for place in system.path:
    print(place)

# default values
from collections import defaultdict
bestiary = defaultdict(lambda: 'Huh?')
bestiary['dog'] = '4'
print(bestiary['cat'])
print(bestiary['dog'])

# another example of default usage
food_counter = defaultdict(int) #initiated as always exist so it will not thow an exception
for food in ['spam', 'coffee', 'spam', 'eggs']:
    food_counter[food] += 1  #this would thow exception without defaultdict
for food, count in food_counter.items():
    print(food, count)

#same as above but with Counter function
from collections import Counter
breakfast = ['spam', 'coffee', 'spam', 'eggs']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
#combining counters
lunch = ['spaghetti', 'coffee', 'soup', 'pudding']
lunch_counter = Counter(lunch)
all_meals = breakfast_counter + lunch_counter
print(all_meals)

#iteration tools
import itertools
for item in itertools.cycle([1,2,3]):
    print(item)
