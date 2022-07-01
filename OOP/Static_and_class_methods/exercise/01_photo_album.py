from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = []

    @property
    def photos(self):
        return self.__photos

    @photos.setter
    def photos(self, value):
        for page in range(self.pages):
            value.append([])
        self.__photos = value

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for page_number in range(self.pages):
            if len(self.photos[page_number]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[page_number].append(label)
                return f"{label} photo added successfully on page {page_number + 1} slot {len(self.photos[page_number])}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11
        output = separator + "\n"
        for page in self.photos:
            output += ' '.join(["[]" for _ in page]) + '\n'
            output += separator + '\n'
        return output.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
