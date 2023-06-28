# Colocar imports e coisas gerais, classes e etc

import pygame

import typing as tp

from events import Events

from src.animated import *
from src.watcher import *

def animated_or(value):
    if isinstance(value,Animated):
        return value.get_current()
    return value