from abc import ABC, abstractmethod
from style import Style
from icon import Icon

class Component(ABC):
    def __init__(self,icon:Icon,key:str,value:str) -> None:
        self.icon = str()
        self.key = key
    
    def draw(self,style:Style,prefix:str,max_width:int,is_last:bool) -> list:
        pass

class Container(Component):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.container_icon
        self.children = []
    
    def add(self,component:Component) -> None:
        self.children.append(component)
    
    def draw(self,style,prefix,max_width,is_last) -> list:
        print_list = []
        print_line,next_prefix = style.draw_container(self.icon,self.key,prefix,max_width,is_last)
        print_list+=print_line
        for index,child in enumerate(self.children):
            is_last = index == len(self.children) - 1
            print_line = child.draw(style,next_prefix,max_width,is_last)
            print_list+=print_line
        return print_list

class Leaf(Component):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.leaf_icon
        self.value = value
    
    def draw(self,style,prefix,max_width,is_last) -> list:
        print_line,_ = style.draw_leaf(self.icon,self.key,self.value,prefix,max_width,is_last)
        return print_line