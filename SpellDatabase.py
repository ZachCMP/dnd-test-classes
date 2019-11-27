class SpellDatabase:
  def __init__(self, spells):
    self.spells = spells

  def getSpellByName(self, name):
    try:
      return self.spells[name]
    except:
      print('Name ' + '"' + name + '"' + ' not in spells')

  def getSpellsByLevel(self, level=0, spells=None):
    if not isinstance(level, int):
      raise Exception('Level must be an integer')
    if level > 9 or level < 0:
      raise Exception('Level must be an integer between 0 and 9')
    out = {}
    for name, info in (spells or self.spells).items():
      if info['level'] == level:
        out[name] = info
    return out

  def getSchoolNames(self):
    schools = []
    for name, info in self.spells.items():
      if info['school'] not in schools:
        schools.append(info['school'])
    return schools

  def getSpellsBySchool(self, school, spells=None):
    if not school:
      raise Exception('School is a required argument')
    if not isinstance(school, str):
      raise Exception('School must be a string')
    if school not in self.getSchoolNames():
      raise Exception('Not a valid school')
    out = {}
    for name, info in (spells or self.spells).items():
      if info['school'] == school:
        out[name] = info
    return out

  def search(self, level, school):
    context = {}
    for name, info in self.spells.items():
      if level:
        context = self.getSpellsByLevel(level, spells=context)
      if school:
        context = self.getSpellsBySchool(school, spells=context)
    return context