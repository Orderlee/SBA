from dataclasses import dataclass

@dataclass
class Entity:
    context: str = ''
    fname: str =''
    train: object = None
    test: object = None
    id: str= ''
    label: str =''
