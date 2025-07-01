# Estrutura do projeto:
# pasta: padroes-estruturais
# subpastas: adapter/, bridge/

# Arquivo: adapter/sem_padrao.py
# Exemplo SEM padrão Adapter
class TomadaAntiga:
    def conectar_redondo(self):
        return "Conectado usando pino redondo (tomada antiga)"

class Secador:
    def ligar(self, tomada):
        print(tomada.conectar_redondo())

# Tentando conectar um dispositivo novo (incompatível com a tomada antiga)
class TomadaNova:
    def conectar_chato(self):
        return "Conectado usando pino chato (tomada nova)"

# Isso não funciona diretamente:
# secador = Secador()
# secador.ligar(TomadaNova())  # Erro! Interface incompatível


# Arquivo: adapter/com_adapter.py
# Aplicando padrão Adapter
class TomadaAntiga:
    def conectar_redondo(self):
        return "Conectado usando pino redondo (tomada antiga)"

class TomadaNova:
    def conectar_chato(self):
        return "Conectado usando pino chato (tomada nova)"

# Adapter
class AdaptadorTomada(TomadaAntiga):
    def __init__(self, nova):
        self.nova = nova

    def conectar_redondo(self):
        return self.nova.conectar_chato()

class Secador:
    def ligar(self, tomada):
        print(tomada.conectar_redondo())

# Teste
secador = Secador()
secador.ligar(AdaptadorTomada(TomadaNova()))  # Funciona



# Arquivo: bridge/sem_padrao.py
# Exemplo SEM padrão Bridge
class Forma:
    def desenhar(self):
        pass

class Circulo(Forma):
    def desenhar(self):
        print("Desenhando círculo com preenchimento vermelho")

class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando quadrado com preenchimento vermelho")

# Se quiser mudar a cor, tem que criar novas classes para cada cor!


# Arquivo: bridge/com_bridge.py
# Aplicando padrão Bridge
class Cor:
    def aplicar_cor(self):
        pass

class Vermelho(Cor):
    def aplicar_cor(self):
        return "vermelho"

class Azul(Cor):
    def aplicar_cor(self):
        return "azul"

class Forma:
    def __init__(self, cor):
        self.cor = cor

    def desenhar(self):
        pass

class Circulo(Forma):
    def desenhar(self):
        print(f"Desenhando círculo com preenchimento {self.cor.aplicar_cor()}")

class Quadrado(Forma):
    def desenhar(self):
        print(f"Desenhando quadrado com preenchimento {self.cor.aplicar_cor()}")

# Teste
forma1 = Circulo(Vermelho())
forma2 = Quadrado(Azul())
forma1.desenhar()
forma2.desenhar()


