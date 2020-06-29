""" market_list.py -- Codecademy project in Computer Science Course """
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

    def __str__(self):
        art_string = '{}. "{}". {}, {}.\n'.format(
            self.artist, self.title, self.year, self.medium)
        owner_string = 'Owner: {}, {}.\n'.format(
            self.owner.name, self.owner.location)
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

    num_clients = 0

    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.is_museum = is_museum
        self.location = location if is_museum else "Private Collection"
        self.wallet = wallet
        self.wishlist = []
        self.bucketlist = []

        Client.num_clients += 1

    def __str__(self):
        return "{}, {}, ${:,}.".format(
            self.name, self.location, self.wallet)

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            market_list.add_listing(new_listing)

    def buy_artwork(self, artwork, price):
        if artwork.owner != self:
            art_listing = None
            for listing in market_list.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
            if art_listing is not None:
                art_listing.art.owner.wallet += price
                art_listing.art.owner = self
                market_list.remove_listing(art_listing)
                self.wallet -= price

    def create_wishlist(self):

        for item in self.bucketlist:
            for listing in market_list.listings:
                if item.title == listing.art.title:
                    self.wishlist.append(listing.art)

    def show_wishlist(self):
        for item in self.wishlist:
            print(item)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __str__(self):
        return "{} ${:,} (USD).\n".format(
            self.art, self.price)


def print_status(collectors, pieces):
    print("Collectors:")
    for collector in collectors:
        print(collector)
    print()

    print("Art pieces:")
    for piece in pieces:
        print(piece)


edytta = Client("Edytta Halpirt", None, False, 15_000_000)
moma = Client("The MOMA", "New York", True, 100_000_000)
james = Client("James Bond", None, False, 18_000_000)
thurston = Client("Thurston Howell III", None, False, 10_000_000)
npm = Client("The National Pushkin Museum", "Moscow", True, 30_000_000)
clients = (moma, npm, edytta, thurston, james)

girl_with_a_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
vétheuil_in_the_fog = Art("Monet, Claude", "Vétheuil in the Fog", 1879, "oil on canvas", moma)
the_starry_night = Art("van Gogh, Vincent", "The Starry Night", 1889, "oil on canvas", moma)
the_red_vineyard = Art("van Gogh, Vincent", "The Red Vineyard", 1888, "oil on canvas", npm)
art_pieces = (girl_with_a_mandolin, vétheuil_in_the_fog,
              the_starry_night, the_red_vineyard)

print_status(clients, art_pieces)

market_list = Marketplace()
print("Listings: (empty -- nothing for sale)")
market_list.show_listings()
print()

edytta.sell_artwork(girl_with_a_mandolin, 6_000_000)
print("Listings: (\"Girl with a Mandolin\" for sale)")
market_list.show_listings()
print()

moma.buy_artwork(girl_with_a_mandolin, 6_000_000)
print("Listings: (empty -- \"Girl with a Mandolin\" sold; nothing for sale)")
market_list.show_listings()
print()

print_status(clients, art_pieces)

moma.sell_artwork(the_starry_night, 8_000_000)
print("Listings:")
market_list.show_listings()

edytta.bucketlist = (the_red_vineyard, the_starry_night)
print("Edytta's bucket list:")
for painting in edytta.bucketlist:
    print(painting)

print("Edytta's wishlist:")
edytta.create_wishlist()
edytta.show_wishlist()
