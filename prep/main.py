from typing import List
from . import Book
from . import Library

makeInts = lambda xs: list(map(int, xs))


def readNthLine(input_file, n):
    with open(input_file) as f:
        return f.readlines()[n].rstrip("\n")


# returns number of books, libraries, and days
def getMetadata(input_file):
    metadata = readNthLine(input_file, 0)

    return list(map(int, metadata.split(" ")))


# returns list of Book objects
def getBooks(input_file):
    books = readNthLine(input_file, 1).split(" ")
    books = makeInts(books)

    return [Book(i, score) for i, score in enumerate(books)]


# returns list of Library objects
def getLibraries(input_file):
    bookCollection = getBooks(input_file)
    libraryObjects = []

    with open(input_file) as f:
        libraries = f.readlines()[2:]

    for i in range(0, len(libraries) - 1, 2):
        numberOfBooks, signupTime, booksPerDay = libraries[i].split(" ")
        books = makeInts(libraries[i + 1].split(" "))
        # print(books)
        books = [bookCollection[j] for j in books]

        # print(numberOfBooks)
        # print(signupTime)
        # print(booksPerDay)

        libraryObject = Library(i // 2, books, signupTime, booksPerDay)
        libraryObjects.append(libraryObject)

    return libraryObjects


def addLibraryOutputEntry(library):
    # produce the first line: library ID + books
    library_entry = f"{str(library.id)} {len(library.scanned_books)}\n"
    # produce the second line: book IDs in order
    library_entry += " ".join(library.scanned_books) + "\n"
    return library_entry


def produceOutputFile(file_name, libraries):
    """
  - libraries: list of libraries in order of sign signup
  - library is an object and has books to submit in order in a data structure (list?)
  """
    with open(file_name, 'w') as f:
        f.write(str(len(libraries)))
        for library in libraries:
            library_entry = addLibraryOutputEntry(library)
            f.write(library_entry)


### Dataset Insight Area
def summarise_dataset(input_file):
    # get global vars - book num, lib num, days
    num_books, num_libraries, days = getMetadata(input_file)
    books = getBooks(input_file)
    libraries = getLibraries(input_file)
    print(
        f"Number of books: {num_books}; Number of libraries: {num_libraries}. Days: {days}"
    )
    print(f"Books: {len(books)}")
    print(f"Libraries: {libraries}")
    # get library objects and book objects
    #input_libraries = getLibraries()


def sortLibrariesByTotalScore(libraries: List[Library],
                              bookCollection: List[Book]) -> List[Library]:
    def getLibraryTotalScore(library: Library, bookCollection: List[Book]):
        score = 0

        book: Book
        for book in library.books:
            score += book.score

        return score

    sortedLibraries = sorted(
        libraries,
        key=lambda library: getLibraryTotalScore(library, bookCollection))

    return sortedLibraries

def sortLibrariesByMeanScore(libraries: List[Library], bookCollection: List[Book]) -> List[Library]:
  def getLibraryMeanScore(library: Library, bookCollection: List[Book]):
    score = 0
      
    book: Book
    for book in library.books:
      score += book.score
        
    return score / len(library.books)
    
  sortedLibraries = sorted(libraries, key=lambda library: getLibraryMeanScore(library, bookCollection))

  return sortedLibraries

def main(input_file):
    # read input

    # get global vars - book num, lib num, days
    getMetadata(input_file)
    # get library objects and book objects
    input_libraries = getLibraries(input_file)

    # do computation

    # find out the ordering of libraries - store in libraries [] in order
    sorted_libraries = []
    # find out the ordering of books within libraries (descending score sort??)
    for library in sorted_libraries:
        library.sort_books()

    # produce output
    produceOutputFile('test.txt', sorted_libraries)


if __name__ == "__main__":
    input_file = "a.txt"
    summarise_dataset(input_file)
    main(input_file)
