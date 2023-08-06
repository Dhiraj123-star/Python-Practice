from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from mod2 import Boo

def foo(b:Boo)->None:
    b.goo()

def zoo()->None:
    print('zooo')
