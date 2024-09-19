from collections import namedtuple

City = namedtuple('City', 'name country population')
 
seoul = City('Seoul', 'Korea', 973.3)

print(seoul.name, seoul.country, seoul.population)