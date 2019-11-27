class Character:
  def __init__(self, adapter, level=None, stats=None, school=None):
    self.level = level
    self.stats = stats
    self.school = school
    self.adapter = adapter

  def getAvailableSpells(self):
    return self.adapter.getSpellsForCharacter(self)