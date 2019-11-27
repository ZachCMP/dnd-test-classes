class CharacterAdapter:
  def __init__(self, db):
    self.db = db
  
  def getSpellsForCharacter(self, character):
    return self.db.search(level=character.level, school=character.school)