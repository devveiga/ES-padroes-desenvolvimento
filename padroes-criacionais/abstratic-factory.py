from abc import ABC, abstractmethod

# === Interfaces de produtos ===
class Herbivoro(ABC):
    @abstractmethod
    def comer_planta(self):
        pass

class Carnivoro(ABC):
    @abstractmethod
    def comer(self, herbivoro: Herbivoro):
        pass

# === Implementações dos produtos para a Floresta ===
class Veado(Herbivoro):
    def comer_planta(self):
        return "Veado comendo plantas da floresta"

class Onca(Carnivoro):
    def comer(self, herbivoro: Herbivoro):
        return f"Onça caçando e comendo o {herbivoro.__class__.__name__}"

# === Implementações dos produtos para o Deserto ===
class Antilope(Herbivoro):
    def comer_planta(self):
        return "Antílope comendo cactos do deserto"

class Leao(Carnivoro):
    def comer(self, herbivoro: Herbivoro):
        return f"Leão devorando o {herbivoro.__class__.__name__}"

# === Abstract Factory ===
class AnimalFactory(ABC):
    @abstractmethod
    def criar_herbivoro(self) -> Herbivoro:
        pass

    @abstractmethod
    def criar_carnivoro(self) -> Carnivoro:
        pass

# === Concrete Factories ===
class FlorestaFactory(AnimalFactory):
    def criar_herbivoro(self):
        return Veado()

    def criar_carnivoro(self):
        return Onca()

class DesertoFactory(AnimalFactory):
    def criar_herbivoro(self):
        return Antilope()

    def criar_carnivoro(self):
        return Leao()

# === Código cliente ===
def simular_ecossistema(factory: AnimalFactory):
    herbivoro = factory.criar_herbivoro()
    carnivoro = factory.criar_carnivoro()

    print(herbivoro.comer_planta())
    print(carnivoro.comer(herbivoro))

# Testando
print("🐾 Ecossistema Floresta")
simular_ecossistema(FlorestaFactory())

print("\n🐪 Ecossistema Deserto")
simular_ecossistema(DesertoFactory())
