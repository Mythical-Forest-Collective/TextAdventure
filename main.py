from utils import typer
from utils.entities import Entity, CM

inf = float('inf')
Narrator = Entity("Narrator", CM(inf, inf), CM(inf, inf))

Narrator.say("Welcome young adventurer, would you like to tell me your name?", end=' ')

