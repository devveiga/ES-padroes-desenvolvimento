from abc import ABC, abstractmethod

# === Produto final ===
class Animal:
    def __init__(self):
        self.especie = None
        self.tamanho = None
        self.habito_alimentar = None

    def __str__(self):
        return f"Animal: {self.especie}, Tamanho: {self.tamanho}, Alimentação: {self.habito_alimentar}"

# === Interface Builder ===
class AnimalBuilder(ABC):
    def __init__(self):
        self.animal = Animal()

    @abstractmethod
    def construir_especie(self): pass

    @abstractmethod
    def definir_tamanho(self): pass

    @abstractmethod
    def definir_habito_alimentar(self): pass

    def get_animal(self):
        return self.animal

# === Concrete Builders ===
class CachorroBuilder(AnimalBuilder):
    def construir_especie(self):
        self.animal.especie = "Cachorro"

    def definir_tamanho(self):
        self.animal.tamanho = "Médio"

    def definir_habito_alimentar(self):
        self.animal.habito_alimentar = "Onívoro"

class ElefanteBuilder(AnimalBuilder):
    def construir_especie(self):
        self.animal.especie = "Elefante"

    def definir_tamanho(self):
        self.animal.tamanho = "Gigante"

    def definir_habito_alimentar(self):
        self.animal.habito_alimentar = "Herbívoro"

# === Diretor ===
class Zoologo:
    def construir_animal(self, builder: AnimalBuilder):
        builder.construir_especie()
        builder.definir_tamanho()
        builder.definir_habito_alimentar()
        return builder.get_animal()

# === Testando ===
diretor = Zoologo()

print("🐶 Construindo um Cachorro:")
cachorro = diretor.construir_animal(CachorroBuilder())
print(cachorro)

print("\n🐘 Construindo um Elefante:")
elefante = diretor.construir_animal(ElefanteBuilder())
print(elefante)
