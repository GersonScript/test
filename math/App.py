from Divisao import Divisao

s = "123/123x123+123-123"

operators = "+-x/"

formatted_tokens = []
current_number = ""

for char in s:
    if char.isdigit():
        current_number += char
    elif char in operators:
        if current_number:
            formatted_tokens.append([int(current_number)])
            current_number = ""
        formatted_tokens.append([char])

if current_number:
    formatted_tokens.append([int(current_number)])


if (formatted_tokens[1][0] == "+"):
    operacao = f"{formatted_tokens[0][0]}{formatted_tokens[1][0]}{formatted_tokens[2][0]}"
    print(f"Adição {operacao}")
elif (formatted_tokens[1][0] == "-"):
    operacao = f"{formatted_tokens[0][0]}{formatted_tokens[1][0]}{formatted_tokens[2][0]}"
    print(f"Subtração {operacao}")
elif (formatted_tokens[1][0] == "x"):
    operacao = f"{formatted_tokens[0][0]}{formatted_tokens[1][0]}{formatted_tokens[2][0]}"
    print(f"Multiplicação {operacao}")
elif (formatted_tokens[1][0] == "/"):
    operacao = f"{formatted_tokens[0][0]}{formatted_tokens[1][0]}{formatted_tokens[2][0]}"
    divisao = Divisao(28244, 80)
    print(divisao.main())