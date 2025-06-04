from pathlib import PurePath
def total_salary(path):
   total=0
   quantity=0
   try:
     with open(path, 'r', encoding="utf-8") as fh:
      lines = [el.strip() for el in fh.readlines()]
      lines.remove('')
      for el in lines:
         try:
           name, salary = el.split(',')
           total+=int(salary)
           quantity+=1
           average = total / quantity  
         except ValueError:
            print(f" Неправильний формат рядка: {el}, або файл пустий")
         
     print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
     return 
   except FileNotFoundError:
     fh_name=PurePath(path).name
     fh_parent=PurePath(path).parent
     print(f"Файл '{fh_name}' - не існує, або  шлях '{fh_parent}' - не вірний")    

path='D:\Morhun_Volodymyr\Mashine_learning\data_project\goit-algo-hw-03\salary.txt'

total_salary(path)
