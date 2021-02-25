
class Scanner:

  def __init__(self):
    self.scan_log = {}

  def log(self, book):
      """ keep a log of all books we have scanned
      scan_log {
          book_id : times_scanned
      }
      return 1 if duplicate else 0
      """
      if book.id in self.scan_log:
          self.scan_log[book.id] += 1
          return 1
      else:
          self.scan_log[book.id] = 1
          return 0
