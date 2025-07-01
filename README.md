📘 ES - Padrões de Desenvolvimento
🎥 Links dos vídeos de apresentação:
Arthur Xavier – Adapter | Bridge
Link: https://drive.google.com/drive/folders/1v3kR1C-aXRUQ1zV-DubuTZOvjqQj-YCU?usp=sharing

Vitor Veiga – Abstract Factory | Builder
Link: https://drive.google.com/file/d/1pL2U6kk71HQ6cFgfA1opKC07b2R5L8Jl/view?usp=sharing

📌 Obs: O Arthur já havia demonstrado dois padrões da mesma categoria, portanto foi optado por apresentar dois padrões de uma categoria diferente.

----------------------------------------------- // ---------------------------------------------------

🔌 Adapter
✅ O que é
Permite que interfaces incompatíveis trabalhem juntas, agindo como um adaptador entre elas.

💡 Exemplo usado
Um secador com tomada antiga sendo conectado a uma nova tomada, usando um adaptador.

🔷 Pontos Fortes
Reutilização de código legado

Fácil integração com sistemas existentes

🔻 Pontos Fracos
Pode ocultar dependências reais

Pode aumentar a complexidade se muito usado

📍 Quando usar
Quando você precisa que uma classe funcione com uma interface diferente da que foi projetada.

----------------------------------------------- // ---------------------------------------------------

🌉 Bridge
✅ O que é
Desacopla a abstração da implementação, permitindo que os dois evoluam independentemente.

💡 Exemplo usado
Formas geométricas com preenchimentos de cor separados, onde as combinações são flexíveis.

🔷 Pontos Fortes
Facilita a extensão

Reduz o número de subclasses

Separa preocupações (abstração vs. implementação)

🔻 Pontos Fracos
Pode ser mais complexo de entender inicialmente

📍 Quando usar
Quando abstrações e implementações podem variar independentemente.

----------------------------------------------- // ---------------------------------------------------

🔨 Builder
✅ Objetivo
Separar a construção de um objeto complexo da sua representação final.

📍 Quando usar
Quando a criação de um objeto envolve muitos passos

Quando o objeto pode ter representações diferentes

🎯 Importância
Permite criar objetos passo a passo

Reutiliza o mesmo processo de construção para diferentes representações

🔷 Pontos Fortes
Separação clara entre construção e representação

Facilidade de customização

Controle total da montagem (ordem e etapas)

Alta reutilização

🔻 Pontos Fracos
Mais código e estrutura: requer criação de várias classes

Pode ser exagero para objetos simples

Menor legibilidade inicial para iniciantes

----------------------------------------------- // ---------------------------------------------------

🧰 Abstract Factory
✅ Objetivo
Fornecer uma interface para criar famílias de objetos relacionados ou dependentes, sem especificar classes concretas.

📍 Quando usar
Quando há várias famílias de produtos relacionados

Quando você quer garantir que os objetos de uma família sejam compatíveis entre si

🎯 Importância
Ajuda na troca de famílias de objetos sem alterar o código cliente

Garante consistência entre os objetos criados

🔷 Pontos Fortes
Isolamento de dependência: o cliente não precisa conhecer as classes concretas

Consistência entre os objetos de uma família

Flexibilidade para trocar famílias (ex: UI de Windows para Mac)

Organização: separa a criação da lógica de uso

🔻 Pontos Fracos
Complexidade: exige muitas classes e interfaces, mesmo para tarefas simples

Dificuldade na manutenção de novas famílias

Pode ser desnecessário para sistemas pequenos ou simples
