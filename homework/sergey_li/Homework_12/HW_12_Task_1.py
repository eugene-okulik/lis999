class Flower:
    def __init__(self, name, color, price, lifetime, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.lifetime = lifetime
        self.stem_length = stem_length

    def __repr__(self):
        return f"{self.name}({self.color}, {self.price}, {self.lifetime}, {self.stem_length})"


class Rose(Flower):
    def __init__(self, color, price, lifetime, stem_length, thorns=True):
        super().__init__("Rose", color, price, lifetime, stem_length)
        self.thorns = thorns


class Tulip(Flower):
    def __init__(self, color, price, lifetime, stem_length, smell="light"):
        super().__init__("Tulip", color, price, lifetime, stem_length)
        self.smell = smell


class Orchid(Flower):
    def __init__(self, color, price, lifetime, stem_length, pot=True):
        super().__init__("Orchid", color, price, lifetime, stem_length)
        self.pot = pot


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifetime(self):
        if not self.flowers:
            return 0
        return sum(f.lifetime for f in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        self.flowers.sort(key=lambda f: getattr(f, attribute, None))

    def find_by_lifetime(self, min_days):
        return [f for f in self.flowers if f.lifetime >= min_days]

    def show_bouquet(self):
        for flower in self.flowers:
            print(flower)


rose = Rose("red", 5, 4, 15)
tulip = Tulip("blue", 3, 10, 9)
orchid = Orchid("white", 20, 15, 12)

bouquet_1 = Bouquet([tulip, rose, orchid])
bouquet_1.sort_by("price")
bouquet_1.show_bouquet()
print(bouquet_1.total_price())
bouquet_1.sort_by("lifetime")
bouquet_1.show_bouquet()
