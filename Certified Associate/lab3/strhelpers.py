from random import shuffle as s_shuffle
def reverse(name):
      return name[::-1]

def str_shuffle(name):
      name_list=list(name)
      s_shuffle(name_list)
      return "".join(name_list)
