import sys
from pathlib import Path
from colorama import Fore, Style, Back



def visualization_structure(path):
    path=Path(path)
    depth=0
    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"❌ Шлях {path} не існує або не є директорією.")
        return

    for item in path.iterdir():
        indent = "└──" * depth
        if item.is_dir():
            print(Fore.BLUE + indent +"──" +f"📁 {item.name}")
            visualization_structure(item) 
            depth+=1
        else:
            print(Fore.GREEN +indent +"──"+ f"📄 {item.name}")
    return



visualization_structure(r"D:\Morhun_Volodymyr\Mashine_learning\data_project")
