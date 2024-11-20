# Dupla: Maria Eduarda e Ludmilla - INFO2V

class Poligono:
    def _init_(self, numero_lados):
        self.numero_lados = numero_lados

    def get_num_lados(self):
        return self.numero_lados

    def set_num_lados(self, novo_num_lados):
        self.numero_lados = novo_num_lados

    def calcular_perimetro(self):
        perimetro = 0
        for i in range(self.numero_lados):
            lado = float(input(f"Digite o valor do lado {i + 1}: "))
            perimetro += lado
        print(f"O perímetro do polígono é: {perimetro}")

class TestarPoligono:
    def main(self):
        num_lados = int(input("Digite o número de lados do polígono: "))
        poligono = Poligono(num_lados)
        poligono.calcular_perimetro()

        novo_num_lados = int(input("Digite o novo número de lados: "))
        poligono.set_num_lados(novo_num_lados)
        poligono.calcular_perimetro()

if _name_ == "_main_":
    teste = TestarPoligono()
    teste.main()