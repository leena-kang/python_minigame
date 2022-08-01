# creating an object = INITIALIZING the object

class Beach: 
   # parts = ['water', 'sand']        # class variable (use if attributes won't change for each object)
    def __init__(self, location, water_color, temperature):      # initialization function
        self.location = location        # instance variables (use if attributes change based on each object)
        self.water_color = water_color
        self.temperature = temperature
        self.heat_rating = 'hot' if temperature > 80 else 'cool'
        self.parts = ['water', 'sand']

    def add_part(self, part):
        self.parts.append(part)


def main():
    cape_cod_beach = Beach('Cape Cod', 'dark blue', 70)
    cancun_beach = Beach('Cancun', 'crystal blue', 90)
    cape_cod_beach.add_part('rock')
    la_beach = Beach('LA', 'turqoise', 85)
    italy_beach = Beach('Italy', 'blue', 82)
    italy_beach.add_part('rock')
    hot_not_rocky = []

    for beach in [cape_cod_beach, cancun_beach, la_beach, italy_beach]:
        if beach.heat_rating == 'hot' and 'rock' not in beach.parts:
            hot_not_rocky.append(beach)

    return hot_not_rocky

if __name__ == '__main__':
    beaches = main()
    print([beach.location for beach in beaches])
