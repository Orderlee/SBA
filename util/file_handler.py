from dataclasses import dataclass
'''
context path : ~/SBA/
modulePath: /titanic/data/
'''
@dataclass
class file_reader:

    context: str =''
    fname: str =''
    train: object = None
    test: object = None
    id: str = ''
    label: str =''