# 프로퍼티 url, parser , path, api, apikey 전부 str 타입
from dataclasses import dataclass

@dataclass
class Entity:
    url: str = ''
    parser: str = ''
    path: str = ''
    api: str = ''
    apikey: str = ''
    csv_filename: str = ''
    columns: object =None
    tag: str =''
    attrs: str = ''
    weekday_dict: str = ''
    replace_txt: str = ''