import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
class Context:
    
    @staticmethod
    def path() -> str:
        return os.path.dirname(os.path.abspath(__file__))
    

if __name__ == '__main__':
    
    print(f'Context Path :::: {Context.path()}')