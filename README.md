# Estruturas, Pesquisa e Ordenação de Dados – 2026/1
## Trabalhos Práticos – 1º Bimestre

**Curso:** Análise e Desenvolvimento de Sistemas  
**Curso:** Guilherme Seidl, Vagner Giraldino, Gustavo Ferreira, Lucas delabernarda
**Instituição:** UniCesumar – Campus Ponta Grossa  
**Disciplina:** Estruturas, Pesquisa e Ordenação de Dados  
**Professor:** Prof. MSc. Gabriel Passos de Jesus  

---

## Estrutura do Repositório

```
.
├── projeto1/
│   ├── trees.py          # BST, AVL, Rubro-Negra
│   └── experiments.py    # TSP + experimentos comparativos
├── projeto2/
│   └── search.py         # Busca Sequencial, Binária e em Árvore
├── projeto3/
│   └── sorting.py        # Merge Sort e Quick Sort
├── generate_reports.py   # Gerador de relatórios PDF
└── README.md
```

---

## Requisitos

- Python 3.8+
- Bibliotecas: `matplotlib`, `reportlab`, `numpy`

```bash
pip install matplotlib reportlab numpy
```

---

## Execução

### Projeto 1 – Árvores e Balanceamento

```bash
cd projeto1
python experiments.py
```

Executa os experimentos de inserção nas três árvores (BST, AVL, Rubro-Negra) e a heurística TSP Vizinho Mais Próximo. Imprime resultados no console com média e desvio padrão de 30 execuções para n ∈ {500, 2000, 8000}.

### Projeto 2 – Sistemas de Busca

```bash
cd projeto2
python search.py
```

Compara busca sequencial, binária e em BST para n ∈ {500, 2000, 8000}, 30 execuções.

### Projeto 3 – Benchmark de Ordenação

```bash
cd projeto3
python sorting.py
```

Avalia Merge Sort e Quick Sort nos casos melhor, médio e pior para n ∈ {500, 2000, 8000}, 30 execuções.

### Gerar Relatórios PDF

```bash
python generate_reports.py
```

Gera os três relatórios técnicos em PDF na pasta `outputs/`.

---

## Reprodutibilidade

Todos os experimentos utilizam `random.seed(42)`. Os resultados são reproduzíveis em qualquer máquina com Python 3.8+ e as dependências instaladas.

---

## Algoritmos Implementados

| Projeto | Algoritmos |
|---------|-----------|
| 1 | BST, AVL, Rubro-Negra, TSP Nearest Neighbor |
| 2 | Busca Sequencial, Busca Binária, Busca em BST |
| 3 | Merge Sort, Quick Sort |

---

## Complexidade Assintótica

| Estrutura/Algoritmo | Melhor | Médio | Pior |
|--------------------|--------|-------|------|
| BST (inserção/busca) | O(log n) | O(log n) | O(n) |
| AVL (inserção/busca) | O(log n) | O(log n) | O(log n) |
| Rubro-Negra (inserção/busca) | O(log n) | O(log n) | O(log n) |
| Busca Sequencial | O(1) | O(n) | O(n) |
| Busca Binária | O(1) | O(log n) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| TSP Nearest Neighbor | — | O(n²) | O(n²) |
