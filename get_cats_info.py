def get_cats_info(path):
    cats_info=[]
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
          el=line.strip().split(",")
          cats_info_dic={"id": el[0], "name": el[1], "age": el[2]}
          cats_info.append(cats_info_dic)

    return cats_info  
        



print(get_cats_info("Cat.txt"))
