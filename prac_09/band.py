from musician import Musician


class Band:

    def __init__(self, name):
        self.name = name
        self.musician = []

    def __repr__(self):
        for musician in self.musician:
            return f"{self.musician} plays {musician.instruments}"

    def add(self, musician):
        self.musician.append(musician)
        return musician

    def play(self):
        print(f"band {self.name} is playing: ")
        for musicians in self.musician:
            musicians.play()
