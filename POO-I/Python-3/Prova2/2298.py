# cria uma classe pra fazer o controle dos pontos, de acordo com as condições descritas no problema
class points_controller:
    # inicia o controlador com uma lista de cartas
    def __init__(self, cards):
        # define a lista de cartas como atributo do controlador
        self.cards = cards
        # deixa as cartas em ordem crescente
        self.cards.sort()

    # métodos privados de points_controller

    # teste para ver se as cartas atendem a primeira condição:
    def __count_condition_1(self):
        for i in range(4):
            if self.cards[i+1] != self.cards[i] + 1:
                return 0
        return self.cards[0] + 200

    # teste para ver se as cartas atendem a segunda condição:
    def __count_condition_2(self):
        if self.cards.count(self.cards[0]) > 3:
            return self.cards[0] + 180
        elif self.cards.count(self.cards[1]) > 3:
            return self.cards[1] + 180
        return 0

    # teste para ver se as cartas atendem a terceira ou quarta condição:
    def __count_condition_3_4(self):
        first_count = self.cards.count(self.cards[0])
        second_count = self.cards.count(self.cards[3])
        if first_count == 3:
            if second_count == 2:
                return self.cards[0] + 160
            else:
                return self.cards[0] + 140
        elif second_count == 3:
            if first_count == 2:
                return self.cards[3] + 160
            else:
                return self.cards[3] + 140
        return 0

    # teste para ver se as cartas atendem a quinta ou a última condição:
    def __count_condition_5_6(self):
        first_count = self.cards.count(self.cards[0])
        second_count = self.cards.count(self.cards[2])
        third_count = self.cards.count(self.cards[4])
        if first_count == 2:
            if second_count == 2:
                greater, minor = self.__get_greater_and_minor(
                    self.cards[0], self.cards[2])
                return 3 * greater + 2 * minor + 20
            elif third_count == 2:
                greater, minor = self.__get_greater_and_minor(
                    self.cards[0], self.cards[4])
                return 3 * greater + 2 * minor + 20
            return self.cards[0]
        elif second_count == 2:
            if third_count == 2:
                greater, minor = self.__get_greater_and_minor(
                    self.cards[2], self.cards[4])
                return 3 * greater + 2 * minor + 20
            return self.cards[2]
        elif third_count == 2:
            return self.cards[4]
        return 0

    # método para pegar o maior valor entre 2 números
    def __get_greater_and_minor(self, n1, n2):
        # poderia ter usado o sort() com reverse=True
        greater = n1
        minor = n2
        if n2 > n1:
            greater = n2
            minor = n1
        return greater, minor

    # método público do controlador
    # faz todos os testes de condição e retorna seus pontos respectivos
    def get_points(self):
        ret = self.__count_condition_1()
        if ret != 0:
            return ret
        ret = self.__count_condition_2()
        if ret != 0:
            return ret
        ret = self.__count_condition_3_4()
        if ret != 0:
            return ret
        return self.__count_condition_5_6()


N = int(input())
for i in range(1, N + 1):
    # instancia um novo points_controller, deixando a lista de cartas como parâmetro
    controller = points_controller([int(w) for w in input().split()])
    # pega os pontos do controlador
    points = controller.get_points()
    # imprime os resultados na tela, seguindo a formatação indicada no problema
    print('Teste ' + str(i))
    print(points, end='\n\n')
