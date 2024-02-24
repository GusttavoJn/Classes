class GerenciadorContatos:

    def __init__(self):
        self.contatos = []
    
    def adicionar_contatos(self, nome, telefone):
        self.contatos.append((nome, telefone))

    def remover_contato(self, nome):
        self.contatos = [(n, t) for n, t in self.contatos if n != nome]

    def buscar_contato(self, nome):
        for n, t in self.contatos:
            if n == nome:
                return t
        return "Contato não encontrado"    
    
    def listar_contato(self):
        for n, t in self.contatos:
            print(f'Nome: {n}, Telefone: {t}')

gerenciador = GerenciadorContatos()
gerenciador.adicionar_contatos('Amanda', '123456767')
gerenciador.adicionar_contatos('Alex', '1231231245')

gerenciador.listar_contato()
print('-' * 20)

print(f"Buscar contato de Amanda: {gerenciador.buscar_contato('Amanda')}")
print(f"Buscar contato de Pedro: {gerenciador.buscar_contato('Pedro')}")

gerenciador.remover_contato('Alex')
print('-' * 20)
gerenciador.listar_contato()


