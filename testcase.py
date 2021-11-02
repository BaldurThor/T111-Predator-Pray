from prey import Prey

from island import Island

isl = Island(3)

Prey.set_breed_time(0)

prey = Prey(isl)

isl.register(prey)

print(isl)

assert str(isl).count('O') == 1

prey.breed()

print(isl)

assert str(isl).count('O') == 3