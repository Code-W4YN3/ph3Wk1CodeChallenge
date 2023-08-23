import string

letter_values = dict(zip(string.ascii_lowercase, range(1,27)))
print(letter_values)

def constant_value(string):
  sum_list = []
  sum = 0

  for i in string:
      if(i not in "aeiou"):
          sum += letter_values.get(i)
      else:
          sum_list.append(sum)
          sum = 0
  sum_list.append(sum)

  print(sum_list)
  return(max(sum_list))

constant_value("strength")