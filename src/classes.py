from loguru import logger
import pathlib

class Material():
    def __init__(self):
        super().__init__()
        
        self.name = ()
        self.maps = dict() # словарь в который складываем пары "название": "путь к текстуре"
        self.output_scheme = dict() # сюда кладем пары "название_текстуры": "4 кортежа(название, канал)""


    def set_name(self):
        pass

    def add_map(self):
        pass

    def remove_map(self):
        pass

    def set_export_path(self):
        pass

    

    
