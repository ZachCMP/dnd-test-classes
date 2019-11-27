import json

from SpellDatabase import SpellDatabase
from CharacterAdapter import CharacterAdapter
from Character import Character

with open('Spells.json') as json_file:
  spells = json.load(json_file)

  db = SpellDatabase(spells)
  adapter = CharacterAdapter(db)

  character = Character(adapter, level=4, school='Evocation', stats={})

  print(character.getAvailableSpells())