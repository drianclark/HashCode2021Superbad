class Book:
  def __init__(self, id, score):
    self.score = score
    self.id = id
    self.library = None
    
  def __repr__(self) -> str:
    return f"{self.id}:{self.score}"
