from pydantic.dataclasses import dataclass
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel


class Location(BaseModel):
    x: int
    y: int

class Attack(BaseModel):
    blockId: str
    target: Location

class Build(Location):
    pass

class MoveBase(Location):
    pass

class Base(BaseModel):
    attack: int # сколько урона даёт
    health: int
    id: str
    isHead: bool
    lastAttack: Location
    range: int # насколько далеко
    x: int
    y: int

class EnemyBase(BaseModel):
    attack: int # сколько урона даёт
    health: int
    isHead: bool
    lastAttack: Location
    name: str
    x: int
    y: int

class Zombie:
    attack: int
    direction: str
    health: int
    id: str
    speed: int
    type: str
    waitTurns: int
    x: int
    y: int

class CommandType(Enum):
    ATTACK = 0
    BUILD = 1
    MOVE_BASE = 2

class Command:
    type: CommandType
    loc: Location

class ZombieType(Enum):
    NORMAL = "normal" # атакует одну клетку. Самоуничтожается после атаки.
    FAST = "fast" # атакует одну клетку. Самоуничтожается после атаки. Имеет повышенную скорость 2.
    BOMBER = "bomber" # атакует все клетки в радиусе 1 от себя. Самоуничтожается после атаки.
    LINER = "liner" # атакует все клетки базы расположенные рядом друг с другом вне зависимости от их количества. Самоуничтожается после атаки.
    JUGGERNAUT = "juggernaut" # уничтожает все клетки базы на которых окажется. В отличие от своих собратьев он не самоуничтожается, а всегда будет идти напролом, пока его не остановит игрок или специальные клетки.
    CHAOS_KNIGHT = "chaos_knight" # атакует клетку в которой оказался. Двигается в соответствии с правилами движения коня в шахматах. Движение происходит всегда на 3 клетки вперед и одну клетку в сторону, сторона и поворот Г определяется рандомно каждый ход. После атаки не самоуничтожается.
