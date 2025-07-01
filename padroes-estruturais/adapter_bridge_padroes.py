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


# Arquivo: adapter/explicacao.md
'''
# Adapter

## O que é
Permite que interfaces incompatíveis trabalhem juntas, agindo como um adaptador.

## Exemplo usado
Um secador com tomada antiga sendo conectado a uma nova tomada, usando um adaptador.

## Pontos fortes
- Reutilização de código legado
- Fácil integração com sistemas existentes

## Pontos fracos
- Pode ocultar dependências reais
- Pode aumentar complexidade se muito usado

## Quando usar
- Quando você precisa que uma classe funcione com uma interface diferente da que foi projetada.
'''


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


# Arquivo: bridge/explicacao.md
'''
# Bridge

## O que é
Desacopla a abstração da implementação para que os dois possam evoluir independentemente.

## Exemplo usado
Formas geométricas com preenchimentos de cor separados, onde as combinações são flexíveis.

## Pontos fortes
- Facilita a extensão
- Reduz o número de subclasses
- Separa preocupações (abstração vs. implementação)

## Pontos fracos
- Pode ser mais complexo de entender inicialmente

## Quando usar
- Quando abstrações e implementações podem variar independentemente.
'''


# Arquivo: README.md
'''
# Padrões Estruturais - Engenharia de Software II

## Integrantes
- Arthur Xavier
- [Nome do outro integrante]

## Categoria: Estrutural

## Padrões estudados:
- Adapter
- Bridge

## Objetivo
Estudar e aplicar os padrões de projeto definidos no livro GoF, apresentando soluções com e sem padrão, além de analisar vantagens e desvantagens de cada abordagem.

## Conclusão
Com o estudo dos padrões Adapter e Bridge, observamos que ambos ajudam a desacoplar sistemas e promover flexibilidade. O Adapter é ideal para adaptar interfaces incompatíveis e o Bridge permite variar abstrações e implementações de forma independente.
'''
