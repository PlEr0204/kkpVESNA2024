import re
def analyze_boolean_function(initial_function, truth_table):
  """
  Анализирует булеву функцию и минимизирует её на основе таблицы истинности.

  Args:
      initial_function: Строка, представляющая начальную функцию.
      truth_table: Список номеров наборов, где функция равна 1.

  Returns:
      Строка: Минимизированная функция, соответствующая таблице истинности.
  """

  def evaluate_function(function, variables):
    """Вычисляет значение булевой функции для заданных значений переменных."""
    for i, var in enumerate(variables):
      exec(f"{var} = {variables[i]}")
    return eval(function)

  def minimize_function(function, variables, truth_table):
    """Минимизирует булеву функцию с помощью карт Карно (не реализовано)."""
    # Здесь необходимо реализовать алгоритм минимизации (Карно)
    # ... 
    # Пока что вернём исходную функцию без изменений
    return function

  variables = sorted(set(re.findall(r"[a-z]\d*", initial_function)))
  
  # Проверка на соответствие таблице истинности
  for i in range(2*len(variables)):
    binary_representation = format(i, f"0{len(variables)}b")
    variable_values = [int(x) for x in binary_representation]
    if evaluate_function(initial_function, variable_values) != (i+1 in truth_table):
      return "Функция не соответствует таблице истинности"

  # Минимизация функции
  minimized_function = minimize_function(initial_function, variables, truth_table)
  return minimized_function

# Пример использования
initial_function = "A*B"
truth_table = [2, 5, 6]

result = analyze_boolean_function(initial_function, truth_table)
print(result)
