from pathlib import PurePath
def total_salary(path):
   fh_name=PurePath(path).name
   fh_parent=PurePath(path).parent
   total=0
   quantity=0

   try:
     with open(path, 'r', encoding="utf-8") as fh:
      lines = [el.strip() for el in fh.readlines()]
      try:
        lines.remove('')
      except ValueError:
        pass
      for el in lines:
         try:
           name, salary = el.split(',')
           total+=float(salary)
           quantity+=1
           try:
             average = total / quantity
           except ZeroDivisionError:
            print(f"{quantity}=0")
         except ValueError:
            print(f" Неправильний формат рядка: {el}")
         if quantity==0:
          print("У файлі {fh_name} не має жодного коректного радка ")
          return None
     print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
     return total, average
   except FileNotFoundError:   
     print(f"Файл '{fh_name}' - не існує, або  шлях '{fh_parent}' - не вірний")    
     return None
path='salary.txt'

total_salary(path)
