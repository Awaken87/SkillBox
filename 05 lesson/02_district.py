# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as folks_1
from district.central_street.house1.room2 import folks as folks_2
from district.central_street.house2.room1 import folks as folks_3
from district.central_street.house2.room2 import folks as folks_4
from district.soviet_street.house1.room1 import folks as folks_5
from district.soviet_street.house1.room2 import folks as folks_6
from district.soviet_street.house2.room1 import folks as folks_7
from district.soviet_street.house2.room2 import folks as folks_8

s = ', '
print('На районе живут', s.join(folks_1), s.join(folks_2), s.join(folks_3), s.join(folks_4), s.join(folks_5),
      s.join(folks_6), s.join(folks_7), s.join(folks_8))


