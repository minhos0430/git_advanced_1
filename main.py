from typing import List

def even_list(int_list: List[int]) -> List[int]:
 even: List[int] = []
 for number in int_list:
  if number % 2 == 0:
   even.append(number)

 return even