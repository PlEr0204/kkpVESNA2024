def check_trajectory(current, target, operations, inside, outside, trajectory, restrictions, a_count=0, range_a_count=0):
    global commands_string
    global extracted_limit
    global extracted_left
    global extracted_right
    if current == target:
        return all(x in trajectory for x in inside) and not any(x in trajectory for x in outside)
    if current > target or current in outside:
        return 0
    count = 0
    for op in operations:
        new_value = eval(f"{current}{op}")
        violates_restriction = False
        for r in restrictions:
            if op == r["command"]:
                if r["left"] <= current < r["right"]:
                    if a_count + 1 > r["limit"] or (op in commands_string  and range_a_count + 1 > extracted_limit):
                        violates_restriction = True
                        break
                if current >= r["right"]:  # Reset only for the specific command
                    if op in commands_string:
                        range_a_count = 0 
                    a_count = 0  
        if not violates_restriction:
            new_a_count = a_count# + (1 if op  in commands_string else 0)
            new_range_a_count = range_a_count + (1 if op in commands_string and extracted_left <= current < extracted_right else 0)
            count += check_trajectory(new_value, target, operations, inside, outside, 
                                      trajectory + [new_value], restrictions, new_a_count, new_range_a_count)
    return count

# ... (rest of the program remains unchanged)

# Основная программа
n = int(input("Введи количество операций: "))
operations = []
print("Вводи операции по порядку в формате: +3, *2, ...")
for i in range(n):
    operations.append(input())
a = int(input("Введи левую границу: "))
b = int(input("Введи правую границу: "))
numbers_inside = []
n1 = int(input("Введи количество чисел по траектории: "))
for i in range(n1):
    numbers_inside.append(int(input()))
numbers_outside = []
n2 = int(input("Введи количество чисел исключающих: "))
for i in range(n2):
    numbers_outside.append(int(input()))

has_restrictions = input("Есть ли ограничения на использование команд? (да/нет): ")
restrictions = []
extracted_limit=0
extracted_left=0
extracted_right =0
if has_restrictions.lower() == "да":
    num_restrictions = int(input("Введи количество ограничений: "))
    for i in range(num_restrictions):
        command = input(f"Введи команду для ограничения {i+1}: ")
        limit = int(input(f"Введи допустимое количество использований команды {command}: "))
        left = int(input(f"Введи левую границу диапазона для ограничения: "))
        right = int(input(f"Введи правую границу диапазона для ограничения: "))
        restrictions.append({"command": command, "limit": limit, "left": left, "right": right})
commands_string=""
for r in restrictions:
    commands_string += r["command"] + " "
if len(restrictions)!=0:
    extracted_limit = restrictions[-1]["limit"]
    extracted_left = restrictions[-1]["left"]
    extracted_right = restrictions[-1]["right"]
result = check_trajectory(a, b, operations, numbers_inside, numbers_outside, [a], restrictions)
print("Количество программ:", result)
