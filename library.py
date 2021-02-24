class Library:
    def __init__(self, id, books, signUpTime, booksPerDay):
        self.id = id
        self.books = books
        self.signUpTime = signUpTime
        self.booksPerDay = booksPerDay

    def __repr__(self) -> str:
        books_string = f"Books:{len(self.books)}\n"
        signup_string = f"Sign Up:{self.signUpTime}\n"
        books_per_day_string = f"Books per Day:{self.booksPerDay}\n"
        book_scores = self.getBookScoreInfo()
        book_scores_string = f"Book Scores: Total: {book_scores['total_score']}, Mean: {book_scores['mean_score']}, Max: {book_scores['max_score']}, Min: {book_scores['min_score']}"
        library_string = f"\nLibrary:\n{books_string}{signup_string}{books_per_day_string}{book_scores_string}"
        return library_string
    
    def getBookScoreInfo(self):
        total_score = 0
        max_score = 0
        min_score = 10000
        for book in self.books:
            total_score += book.score
            if book.score > max_score:
                max_score = book.score
            if book.score < min_score:
                min_score = book.score

        return {
            "total_score": total_score,
            "max_score": max_score,
            "min_score": min_score,
            "mean_score": total_score / len(self.books)
        }