# Address coordinates enricher using OpenCage- Enriquecimento de Endereços com Coordenadas Geográficas usando opencage


## 🌍 About the Project  

Lately, I have been facing the challenge of building **observability** both from a **technical perspective**, monitoring resources and integrations, and from a **business perspective**, exposing operational efficiency and bottlenecks to generate improvement ideas.  

Recently, I came up with the idea of exploring the **geographical dispersion** of some indicators to detect potential anomalies. However, the addresses stored in my database do not have **coordinates**, and most commercial observability tools (such as Grafana) require them.  

**Straight to the point: How can we obtain a coordinate based on an address?**  

This script reads a JSON file containing a list of addresses (street, number, city, state), iterates over the list, attempts to enrich it using the OpenCage API, and saves the enriched data in an output JSON file.  

### ⚠️ Key Considerations  

- In my case, the dataset contained only **2,000 addresses**, allowing execution within OpenCage’s **free tier**. If your dataset is larger, you may need to create a **partitioning strategy** or subscribe to a **paid plan**.  
- This script could be optimized using **parallel processing**, but it is important to be aware of **API rate limits**.  


## How to execute
1. Make sure you have python3 and pip installed on your PC.
2. **Install** the dependencies:
   ```sh
   pip install opencage
   ```
3. Update the file by setting your API key and defining the input file path.
4. Run the script using Python

---

## 🌍 Sobre o Projeto  

Nos últimos tempos, tenho encarado o desafio de construir observabilidade tanto do ponto de vista técnico, monitorando recursos e integrações, como do ponto de vista de negócio, expondo eficiência operacional e gargalos, e com isso criando ideias de melhoria.  

Recentemente, surgiu a ideia de tentar explorar a dispersão geográfica de alguns indicadores para observar eventuais anomalias. Entretanto, os endereços que possuo em minha base de dados não possuem coordenadas, e boa parte das ferramentas comerciais de observabilidade (no meu caso, Grafana) as utilizam.  

**Direto ao ponto: Como podemos conseguir a coordenada baseada em um endereço?**  

Este script lê um arquivo JSON contendo uma lista de endereços (rua, número, cidade, estado), itera sobre essa lista tentando enriquecê-la através da API do OpenCage e salva os dados enriquecidos em um arquivo JSON de saída.  

### ⚠️ Pontos de Atenção  

- No meu caso, a base a ser enriquecida continha apenas 2.000 endereços, o que permitiu a execução dentro do **free tier** do OpenCage. Se sua base for maior, talvez seja necessário criar uma estratégia de particionamento ou contratar um plano pago.  
- Este script poderia ser otimizado usando alguma estratégia de **paralelismo**, porém é necessário tomar cuidado com os **rate limits** da API.



## Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```sh
   pip install opencage
   ```
3. Altere no script sua API key e o caminho do arquivo.
4. Execute usando python.
