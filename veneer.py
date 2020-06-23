# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0103
class Art:
    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.year = year
        self.medium = medium
        self.owner = owner

    def __repr__(self):
        art_string = f'{self.artist}. "{self.title}". {self.year}, {self.medium}.\n'
        owner_string = f'Owner: {self.owner.name}, {self.owner.location}.\n'
        return art_string + owner_string


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing_to_remove):
        self.listings.remove(listing_to_remove)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:
    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.is_museum = is_museum
        self.location = location if is_museum else "Private Collection"
        self.wallet = wallet

    def __repr__(self):
        return f"{self.name}, {self.location}, ${self.wallet:,}."

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)
            self.wallet += new_listing.price

    def buy_artwork(self, artwork, price):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
            if art_listing is not None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)
                self.wallet -= price


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f"{self.art} ${self.price:,} (USD).\n"

edytta = Client("Edytta Halpirt", None, False, 15000000)
moma = Client("The MOMA", "New York", True, 20000000)
print("Collectors:")
print(edytta)
print(moma)
print()

girl_with_a_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
vétheuil_in_the_fog = Art("Monet, Claude", "Vétheuil in the Fog", 1879, "oil on canvas", moma)
print("Art pieces:")
print(girl_with_a_mandolin)
print(vétheuil_in_the_fog)

veneer = Marketplace()
print("Listings: (should be empty)")
veneer.show_listings()
print()

edytta.sell_artwork(girl_with_a_mandolin, 6000000)
print("Listings: (should be \"Girl with a Mandolin\")")
veneer.show_listings()
print()

moma.buy_artwork(girl_with_a_mandolin, 6000000)
print("Listings: (should be empty)")
veneer.show_listings()
print()

print("Collectors: ")
print(edytta)
print(moma)
print()

print("Art pieces:")
print(girl_with_a_mandolin)
print(vétheuil_in_the_fog)
