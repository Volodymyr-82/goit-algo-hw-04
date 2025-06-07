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
        indent = "  " * depth  
        if item.is_dir():
            print(Fore.BLUE + indent +"└── " +f"📁 {item.name}")
            visualization_structure(item) 
            depth+=1
        else:
            print(Fore.GREEN +indent +"└── "+ f"📄 {item.name}")
    return



#visualization_structure(r"D:\Morhun_Volodymyr\Mashine_learning\data_project")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "⚠️  Вкажи шлях до директорії як аргумент.")
        print(Fore.YELLOW + "📌 Приклад: python visualizetion_structure_directory.py D:\\MyFolder")
    else:
        start_path = sys.argv[1]
        print(Fore.CYAN + f"\n📂 Структура директорії: {start_path}\n")
        visualization_structure(start_path)