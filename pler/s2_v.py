print("x y z w")
for x in(0,1):
    for y in (0,1):
        for z in (0,1):
            for w in (0,1):
                if ((x<=y*(not(z)))+w)==0:
                    print(x,y,z,w)
#задание с решуЕГЭ:
"""
Логическая функция F задаётся выражением (x ∨ y) → (z ≡ x).

Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.

Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z.
"""
# решение с решуЕГЭ:
print("x y z")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x or y) <= (z == x)):
                print(x, y, z)