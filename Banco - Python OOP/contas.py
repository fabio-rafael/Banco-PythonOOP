class ExceptionBalanco(Exception):
  pass



class Conta:
    def __init__(self, nome_conta, quantia_inicial):
        self.nome = nome_conta
        self.balanco = float(quantia_inicial)

    def getBalanco(self):
        print(f"\nConta do titular: '{self.nome}' | Balanço = {self.balanco:.2f}€\n")

    def deposito(self, quantia):
        self.balanco += float(quantia)
        print(f"\nDepósito Completo.")
        self.getBalanco()

    def verlevantamento(self, quantia):
        if self.balanco >= float(quantia):
            return
        else:
            raise ExceptionBalanco(f"\nDesculpe a conta de '{self.nome}' só tem um balanço  de {self.balanco:.2f}€, não pode executar essa operação.")

    def levantamento(self, quantia):
        try:
            self.verlevantamento(quantia)
            self.balanco -= float(quantia)
            print("\nLevantamento Completo.")
            self.getBalanco()
        except ExceptionBalanco as error:
            print(f'\n\nLevantamento indisponível: {error}')

    def transferencia(self, quantia, nome_conta):
        try:
            print('\n*********** \n\nA começar transferência...')
            self.verlevantamento(quantia)
            self.levantamento(quantia)
            nome_conta.deposito(quantia)
            print('\nTransferência Completa! \n\n ')
        except ExceptionBalanco as error:
            print(f'\nTransferência interrompida: {error}')


class jurosCompostos(Conta):
    def deposito(self, quantia, taxa, meses):
        taxa_decimal = float(taxa) / 100
        montante = float(quantia) * (1 + taxa_decimal / 12) ** meses
        self.balanco += montante
        print(f"\nMontante após {meses} meses: {self.balanco:.2f}€")
        self.getBalanco()


class contaPoupanca(jurosCompostos):
    def __init__(self, quantia, nome):
        super().__init__(nome, quantia)
        self.taxa = 0.03  # Taxa padrão

    def set_taxa_percentual(self, taxa_percentual):
        # Converte a taxa de percentual para decimal (ex: 3% para 0.03)
        self.taxa = float(taxa_percentual) / 100

    def simular_impacto_anual(self, anos):
        montante_inicial = self.balanco
        for _ in range(int(anos)):
            self.balanco *= (1 + self.taxa)
        print(f"\nSimulação de conta poupança após {anos} anos:")
        print(f"Montante inicial: {montante_inicial:.2f}€")
        print(f"Montante final: {self.balanco:.2f}€")
        print("*******************************************\n")
        






