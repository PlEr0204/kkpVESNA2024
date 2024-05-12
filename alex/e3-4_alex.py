from sympy import Symbol, simplify, And, Or, Not, Implies, Equivalent

def simplify_expression(expression_str):
  """
  Упрощает логическое выражение.

  Args:
      expression_str: Строка, представляющая логическое выражение.

  Returns:
      Упрощенное выражение в виде строки.
  """
  symbols = []
  for char in expression_str:
    if char.isalpha():
      symbols.append(Symbol(char))

  expression = eval(expression_str, {s.name: s for s in symbols})  # преобразуем строку в выражение
  simplified_expression = simplify(expression)
  return str(simplified_expression)

# Пример использования
expression = "(A|B)&((A|B)>>(A&B))" #ввод выражения
simplified = simplify_expression(expression)
print(f"Упрощенное выражение: {simplified}")
"""| Операция | Символ Python | Описание |
|---|---|---|
| И (конъюнкция) | `&` | Истинно, только если оба операнда истинны. |
| ИЛИ (дизъюнкция) | `|` | Истинно, если хотя бы один операнд истинен. |
| НЕ (отрицание) | `~` | Инвертирует значение операнда. |
| Импликация (если ... то) | `>>` | Истинно, кроме случаев, когда первый операнд истинен, а второй ложен. |
| Эквивалентность (тогда и только тогда) | `<=>` | Истинно, если оба операнда имеют одинаковое значение (истина или ложь). |"""
#пример ввода с демки задания 3: (A|B)&((A|B)>>(A&B))
#пример ввода задания 4 с демки: "(~y&x|~z&x|y&z)&(~(x&~z)|~z&y)" где x1=x x2=y x3=z

