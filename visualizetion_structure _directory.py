import sys, pathlib
from colorama import Fore, Back, Style, init

init(autoreset=True)

def visualization_structure_directory(path):
    directory = pathlib.Path(path)
    colors=[Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    i=0
    for path in directory.iterdir():
        #for color in colors:
       print(colors[i] + "└── " +f"📁 {path}/" + Style.DIM)
       i+=1
    return path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, передайте шлях до директорії як аргумент.")
        
    else:
        directory_path = sys.argv[1]
        visualization_structure_directory(directory_path) 

visualization_structure_directory(r"D:\Morhun_Volodymyr\Mashine_learning")


