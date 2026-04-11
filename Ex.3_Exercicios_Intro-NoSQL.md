# Gustavo L. de Carvalho

## 1. Definição e Características

**a) Caracterização:** Um banco de dados não-relacional (NoSQL) é caracterizado por não utilizar o modelo tabular fixo tradicional (linhas, colunas e chaves estrangeiras). Ele possui esquemas flexíveis e é projetado especificamente para escalabilidade distribuída, lidando nativamente com dados semiestruturados, não estruturados ou polimórficos.

**b) Vantagens:** A principal vantagem é a facilidade e o menor custo da escalabilidade horizontal. Além disso, oferecem flexibilidade de esquema (schema-less), o que acelera o desenvolvimento de software, e entregam altíssimo desempenho para operações massivas de leitura e escrita.

**c) Três situações práticas:**
* Plataformas de e-commerce e sistemas de recomendação, onde os atributos dos produtos mudam constantemente.
* Internet das Coisas (IoT), com necessidade de ingerir e armazenar uma enxurrada contínua de dados de sensores em tempo real.
* Jogos multiplayer modernos que precisam salvar estados complexos de jogadores (itens, missões, estatísticas) com baixíssima latência.

---

## 2. Tipos de Bancos de Dados Não-Relacionais

**a) Diferenças entre os quatro principais tipos:**
* **Orientados a Documentos:** Agrupam dados em documentos autodescritivos (como JSON ou BSON). São excelentes para representar dados hierárquicos e objetos complexos da aplicação diretamente no banco.
* **Chave-Valor:** O modelo mais enxuto. Cada item contém uma chave única e um valor bruto associado. Possuem velocidade extrema, sendo muito usados para armazenamento em cache.
* **Colunas Amplas:** Armazenam dados em partições agrupadas por famílias de colunas em vez de linhas horizontais. São projetados para fazer consultas analíticas eficientes em petabytes de dados espalhados por vários servidores.
* **Grafos:** Focados quase inteiramente nas relações entre os dados. Usam nós (entidades) e arestas (relacionamentos) para permitir a navegação ultrarrápida em redes complexas.

**b) Exemplos de ferramentas populares:**
* **Orientados a Documentos:** MongoDB, Couchbase.
* **Chave-Valor:** Redis, Amazon DynamoDB.
* **Colunas Amplas:** Apache Cassandra, HBase.
* **Grafos:** Neo4j, Amazon Neptune.

---

## 3. Comparação Prática

**a) Modelo Relacional vs. Modelo de Grafos:** No modelo relacional, estabelecer relacionamentos requer tabelas intermediárias e junções (JOINs) que se tornam extremamente lentas à medida que os dados crescem. No modelo de grafos, os relacionamentos são entidades de primeira classe (já vêm "conectados" fisicamente), tornando as buscas por conexões complexas incrivelmente velozes.

**b) Banco para redes sociais:** O modelo de Grafos seria, sem dúvida, o mais adequado.

**Justificativa:** O núcleo de uma rede social são as interações ("quem curte o que", "amigos em comum", "grupos em comum"). Bancos de grafos percorrem essas conexões de forma natural e com desempenho altíssimo, evitando o peso computacional de dezenas de cruzamentos de tabelas que um banco relacional exigiria.

---

## 4. Escalabilidade e Flexibilidade

**a) Escalabilidade Horizontal:** Ao invés de melhorar o hardware de um único servidor central (escalabilidade vertical), a escalabilidade horizontal distribui os dados e o processamento adicionando mais máquinas comuns (nós) ao cluster. Bancos NoSQL usam técnicas como sharding (fragmentação) para distribuir essa carga automaticamente.

**b) Flexibilidade de schema:** Em bancos orientados a documentos, diferentes registros podem ter atributos distintos na mesma coleção. Se um novo recurso for lançado no seu software e exigir um campo inédito, você não precisa fazer uma migração demorada e travar o banco para alterar a estrutura da tabela inteira, garantindo muita agilidade contínua ao desenvolvimento.

---

## 5. Estudo de Caso

**a) Caso real:** O Discord, a popular plataforma de comunicação, é um case clássico do uso de bancos de dados da família de Colunas Amplas (iniciaram com Apache Cassandra e depois migraram para ScyllaDB).

**b) Utilização e Benefícios:** O Discord utiliza essa tecnologia para armazenar bilhões de mensagens de chat geradas diariamente por todo o globo. O grande benefício obtido foi conseguir ingerir volumes massivos de escrita por segundo sem gargalos, garantindo alta disponibilidade (o sistema não cai se um servidor falhar) e latência muito baixa, escalando perfeitamente conforme a base de usuários saltava de milhares para milhões.
