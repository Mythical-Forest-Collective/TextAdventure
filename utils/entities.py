from dataclasses import dataclass
from collections import namedtuple

from yachalk import chalk

from utils import typer

CM = namedtuple("CurrentMax", "current max")

better_green = chalk.hex('#339933')

@dataclass
class Entity:
    name:str = "Entity"
    health:CM = CM(1, 1)
    mana:CM = CM(1, 1) # `mana.current` `mana.max`

    def say(self, *text, sep=' ', **kwargs):
        typer(chalk.yellow(f"[{chalk.blue(self.name)}] "), delay=0.025, end='')
        typer(better_green(sep.join(text)), sep=sep, **kwargs)

    def action(self, *text, sep=' ', **kwargs):
        typer(chalk.yellow(f"<{chalk.blue(self.name)}> "), delay=0.025, end='')
        typer(chalk.cyan_bright(sep.join(text)), sep=sep, **kwargs)


@dataclass
class Enemy(Entity):
    name:str = "Enemy"
    health:CM = CM(1, 1)
    mana:CM = CM(1, 1)
    moves:Moveset()

    def 

# class Player
