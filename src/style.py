from abc import ABC, abstractmethod
from typing import Union

# 定义用于树结构绘制的符号
VERTICAL = "│"
HORIZONTAL = "─"
TEE = "├─"
ELBOW = "└─"
# 定义用于矩形结构绘制的符号
BOX_TOP_LEFT = "┌─"
BOX_TOP_RIGHT = "─┐"
BOX_BOTTOM_LEFT = "└─"
BOX_BOTTOM_RIGHT = "─┘"
BOX_HORIZONTAL = "─"
BOX_VERTICAL = "│"
BOX_TEE_BOTTOM = "─┴─"
BOX_TEE_RIGHT = "─┤"
BOX_TEE_LEFT = "├─"

class StyleFactory(ABC):
    @abstractmethod
    def create_style(self) -> 'Style':
        pass

class TreeStyleFactory(StyleFactory):
    def create_style(self) -> 'Style':
        return TreeStyle()

class RectangleStyleFactory(StyleFactory):
    def create_style(self) -> 'Style':
        return RectangleStyle()

class Style(ABC):
    @abstractmethod
    def draw_container(self,icon:str,key:str,prefix:str,max_width:int,is_last:bool) -> Union[list,str]:
        pass

    @abstractmethod
    def draw_leaf(self,icon:str,key:str,value:str,prefix:str,max_width:int,is_last:bool) -> Union[list,str]:
        pass

    @abstractmethod
    def beautification(self,print_list:list) -> list:
        pass

class TreeStyle(Style):
    def draw_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) -> Union[list,str]:
        connector = ELBOW if is_last else TEE
        print_line = f"{prefix}{connector}{icon}{key}"
        extension = "   " if is_last else f"{VERTICAL}  "
        return [print_line],prefix+extension

    def draw_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) -> Union[list,str]:
        connector = ELBOW if is_last else TEE
        if value == 'None':
            print_line = f"{prefix}{connector}{icon}{key}"
        else:
            print_line = f"{prefix}{connector}{icon}{key}: {value}"
        return [print_line],''
    
    def beautification(self, print_list: list) -> list:
        return print_list

class RectangleStyle(Style):
    def draw_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) -> Union[list,str]:
        connector = BOX_TEE_LEFT
        line = f"{connector}{icon}{key} {HORIZONTAL * (max_width-len(prefix)-len(key)-len(connector)-2)}{BOX_TEE_RIGHT}"
        print_line = f"{prefix}{line}"
        extension = f"{VERTICAL}  "
        return [print_line],prefix+extension

    def draw_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) -> Union[list,str]:
        connector = BOX_TEE_LEFT
        if value == 'None':
            line = f"{connector}{icon}{key} {HORIZONTAL * (max_width-len(prefix)-len(key)-len(connector)-2)}{BOX_TEE_RIGHT}"
            print_line = f"{prefix}{line}"
        else:
            line = f"{connector}{icon}{key}: {value} {HORIZONTAL * (max_width-len(prefix)-len(key)-len(connector)-len(value)-4)}{BOX_TEE_RIGHT}"
            print_line = f"{prefix}{line}"
        return [print_line],''
    
    def beautification(self, print_list: list) -> list:
        new_print_list = []
        for index,l in enumerate(print_list):
            if index==0:
                for i,s in enumerate(l):
                    if s=="├":
                        l = l[:i]+BOX_TOP_LEFT+l[i+2:]
                    elif s=="┤":
                        l = l[:i-1]+BOX_TOP_RIGHT+l[i+1:]
            elif index==len(print_list)-1:
                for i,s in enumerate(l):
                    if i==0 and s=="│":
                        l = l[:i]+BOX_BOTTOM_LEFT+l[i+2:]
                    elif s=="│" or s=="├":
                        l = l[:i-1]+BOX_TEE_BOTTOM+l[i+2:]
                    elif s=="┤":
                        l = l[:i-1]+BOX_BOTTOM_RIGHT+l[i+1:]
            new_print_list.append(l)
        return new_print_list
