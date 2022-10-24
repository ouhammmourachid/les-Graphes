

class Node:
    
    def __init__(self,name:str=None) -> None:
        self.name:str= name
        
    def __str__(self) -> None:
        return f'Node({self.name}'
