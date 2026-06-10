# Target: A interface que o cliente já conhece e espera usar.
class ReadPlanilha:
    def ler_arquivo(self, caminho):
        # Lógica padrão (ex: ler XML ou XLSX)
        print(f"[Target] Lendo arquivo padrão do caminho: {caminho}")
        return "Dados do arquivo padrão"

# Adaptee: A classe útil, mas com métodos incompatíveis com o Target.
class Adaptee:
    def ler_csv(self, caminho):
        print(f"[Adaptee] Lendo CSV do caminho: {caminho}")
        return "Dados do CSV"
    
    def ler_json(self, caminho):
        print(f"[Adaptee] Lendo JSON do caminho: {caminho}")
        return "Dados do JSON"

# Adapter: Implementa a interface Target e "traduz" a chamada para o Adaptee.
class Adapter(ReadPlanilha):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def ler_arquivo(self, caminho):
        if caminho.endswith('.csv'):
            return self.adaptee.ler_csv(caminho)
        elif caminho.endswith('.json'):
            return self.adaptee.ler_json(caminho)
        else:
            return super().ler_arquivo(caminho)

class Client:
    def processar_planilha(self, leitor: ReadPlanilha, caminho):
        dados = leitor.ler_arquivo(caminho)
        print(f"Processando no Cliente: {dados}\n")

if __name__ == "__main__":
    cliente = Client()

    print("--- Cenário 1: Usando a classe padrão ---")
    leitor_padrao = ReadPlanilha()
    cliente.processar_planilha(leitor_padrao, "dados.xml")

    print("--- Cenário 2: Usando o Adapter para ler formatos novos ---")
    sistema_legado = Adaptee()
    
    adaptador = Adapter(sistema_legado)
    
    cliente.processar_planilha(adaptador, "dados.csv")
    cliente.processar_planilha(adaptador, "dados.json")