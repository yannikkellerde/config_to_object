# Automatically generated type hinting file for a .ini file

from typing import NamedTuple, List, Tuple

class Test(NamedTuple):
    parameter:List[int]
    do_thing:bool

class Params(NamedTuple):
    story:str
    words:Tuple[str]

class Config(NamedTuple):
    Test:Test
    Params:Params