class Data:
    def __init__(self, dia, mes, ano):
        print("Construindo o tempo...")
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def tempo(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))
