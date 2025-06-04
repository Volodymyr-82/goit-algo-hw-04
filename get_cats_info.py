def get_cats_info(path):
    cats_info={}
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
          el=line.strip().split(",")
          cats_info={"id": el[0], "name": el[1], "age": el[2]}
            
          print(cats_info)



path="Cat.txt"
get_cats_info(path)
