class Divisao:
    def __init__(self, dividendo, divisor):
        self.dividendo = self.converter_numero(dividendo)
        self.divisor = self.converter_numero(divisor)
        self.resultado_geral = []
        self.resultado_restos = []

    def converter_numero(self, entrada):
        try:
            numero = float(entrada)
            return int(numero) if numero.is_integer() else numero
        except ValueError:
            return "Valor inválido"

    def igualar_casas_decimais(self, entrada1, entrada2):
        str1, str2 = str(entrada1), str(entrada2)

        casas_decimais1 = len(str1.split(".")[1]) if "." in str1 else 0
        casas_decimais2 = len(str2.split(".")[1]) if "." in str2 else 0

        max_casas_decimais = max(casas_decimais1, casas_decimais2)
        fator = 10 ** max_casas_decimais

        return entrada1 * fator, entrada2 * fator

    def primeiro_passo(self, lista_dividendo, divisor):
        concatenado = ""
        for digito in lista_dividendo:
            concatenado += digito
            if int(concatenado) >= divisor:
                break
        return int(concatenado)

    def contar_casas_decimais_depois(self, valor):
        partes = str(valor).split(".")
        return len(partes[1]) if len(partes) > 1 else 0

    def main(self):
        resultado = ""
        contagem_casas_decimais = self.contar_casas_decimais_depois(self.dividendo / self.divisor)

        if isinstance(self.dividendo, (int, float)) and isinstance(self.divisor, (int, float)):
            if self.dividendo % 1 != 0 or self.divisor % 1 != 0:
                dividendo, divisor = self.igualar_casas_decimais(self.dividendo, self.divisor)
                lista_dividendo = list(str(int(dividendo)))
                number = self.primeiro_passo(lista_dividendo, divisor)
                quociente = number // divisor
                resto = number % divisor
                posicao_corte = len(str(number))
                nova_lista_dividendo = lista_dividendo[posicao_corte:]
                self.resultado_geral.append(quociente)

                for digito in nova_lista_dividendo:
                    sub_resto = int(f"{resto}{digito}")
                    quociente = sub_resto // divisor
                    resto = sub_resto % divisor
                    self.resultado_geral.append(quociente)

                if contagem_casas_decimais > 4:
                    if resto < divisor:
                        novo_sub_resto = int(f"{resto}0")
                        self.resultado_restos.append(novo_sub_resto)
                        self.resultado_geral.append(",")
                        for _ in range(4):
                            novo_quociente = novo_sub_resto // divisor
                            novo_resto = novo_sub_resto % divisor
                            novo_sub_resto = int(f"{novo_resto}0")
                            self.resultado_restos.append(novo_sub_resto)
                            self.resultado_geral.append(novo_quociente)
                else:
                    if resto < divisor:
                        novo_sub_resto = int(f"{resto}0")
                        self.resultado_restos.append(novo_sub_resto)
                        self.resultado_geral.append(",")
                        for _ in range(contagem_casas_decimais):
                            novo_quociente = novo_sub_resto // divisor
                            novo_resto = novo_sub_resto % divisor
                            novo_sub_resto = int(f"{novo_resto}0")
                            self.resultado_restos.append(novo_sub_resto)
                            self.resultado_geral.append(novo_quociente)

                resultado += f"{self.dividendo} / {self.divisor}\n"
                resultado += f"{dividendo} / {divisor}\n"
                resultado += f"{self.resultado_restos[0]}     {''.join(map(str, self.resultado_geral))}\n"

                for item in self.resultado_restos[1:]:
                    resultado += f" {item}\n"
            else:
                dividendo, divisor = self.dividendo, self.divisor
                lista_dividendo = list(str(dividendo))
                number = self.primeiro_passo(lista_dividendo, divisor)
                quociente = number // divisor
                resto = number % divisor
                posicao_corte = len(str(number))
                nova_lista_dividendo = lista_dividendo[posicao_corte:]
                self.resultado_geral.append(quociente)

                for digito in nova_lista_dividendo:
                    sub_resto = int(f"{resto}{digito}")
                    quociente = sub_resto // divisor
                    resto = sub_resto % divisor
                    self.resultado_geral.append(quociente)
                    self.resultado_restos.append(sub_resto)

                if contagem_casas_decimais > 4:
                    if resto < divisor:
                        novo_sub_resto = int(f"{resto}0")
                        self.resultado_restos.append(novo_sub_resto)
                        self.resultado_geral.append(",")
                        for _ in range(4):
                            novo_quociente = novo_sub_resto // divisor
                            novo_resto = novo_sub_resto % divisor
                            novo_sub_resto = int(f"{novo_resto}0")
                            self.resultado_restos.append(novo_sub_resto)
                            self.resultado_geral.append(novo_quociente)
                else:
                    novo_sub_resto = int(f"{resto}0")
                    self.resultado_restos.append(novo_sub_resto)
                    self.resultado_geral.append(",")
                    for _ in range(contagem_casas_decimais):
                        novo_quociente = novo_sub_resto // divisor
                        novo_resto = novo_sub_resto % divisor
                        novo_sub_resto = int(f"{novo_resto}0")
                        self.resultado_restos.append(novo_sub_resto)
                        self.resultado_geral.append(novo_quociente)

                resultado += f"{dividendo} / {divisor}\n"
                resultado += f"{self.resultado_restos[0]} {''.join(map(str, self.resultado_geral))}\n"

                for item in self.resultado_restos[1:]:
                    resultado += f"{item}      \n"

        return resultado

# Exemplo de uso
divisao = Divisao(10, 2)
print(divisao.main())