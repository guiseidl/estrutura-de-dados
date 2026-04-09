"""
Projeto 1 – Heurística do Caixeiro-Viajante (Nearest Neighbor)
e experimentos comparativos com BST, AVL e Rubro-Negra
"""

import time
import random
import math
import statistics

from trees import BST, AVL, RedBlackTree


# ─────────────────────────────────────────────────────────────
# Heurística do Caixeiro-Viajante – Vizinho Mais Próximo
# ─────────────────────────────────────────────────────────────
def tsp_nearest_neighbor(cities):
    """cities: lista de tuplas (x, y)"""
    n = len(cities)
    visited = [False] * n
    route = [0]
    visited[0] = True
    for _ in range(n - 1):
        last = route[-1]
        best_dist = float('inf')
        best_city = -1
        for j in range(n):
            if not visited[j]:
                dx = cities[last][0] - cities[j][0]
                dy = cities[last][1] - cities[j][1]
                d = math.hypot(dx, dy)
                if d < best_dist:
                    best_dist = d
                    best_city = j
        route.append(best_city)
        visited[best_city] = True
    return route


def route_length(cities, route):
    total = 0.0
    n = len(route)
    for i in range(n):
        a = cities[route[i]]
        b = cities[route[(i + 1) % n]]
        total += math.hypot(a[0] - b[0], a[1] - b[1])
    return total


# ─────────────────────────────────────────────────────────────
# Experimentos com Árvores
# ─────────────────────────────────────────────────────────────
def run_tree_experiment(n_values, runs=30, seed=42):
    """
    Para cada tamanho n em n_values, executa `runs` experimentos
    medindo tempo de inserção de n chaves aleatórias nas três árvores.
    Retorna dict com resultados.
    """
    random.seed(seed)
    results = {}
    for n in n_values:
        bst_times, avl_times, rb_times = [], [], []
        for r in range(runs):
            keys = random.sample(range(n * 10), n)

            # BST
            tree = BST()
            t0 = time.perf_counter()
            for k in keys:
                tree.insert(k)
            bst_times.append(time.perf_counter() - t0)

            # AVL
            tree = AVL()
            t0 = time.perf_counter()
            for k in keys:
                tree.insert(k)
            avl_times.append(time.perf_counter() - t0)

            # Rubro-Negra
            tree = RedBlackTree()
            t0 = time.perf_counter()
            for k in keys:
                tree.insert(k)
            rb_times.append(time.perf_counter() - t0)

        results[n] = {
            'BST':  {'mean': statistics.mean(bst_times),  'std': statistics.stdev(bst_times)},
            'AVL':  {'mean': statistics.mean(avl_times),  'std': statistics.stdev(avl_times)},
            'RB':   {'mean': statistics.mean(rb_times),   'std': statistics.stdev(rb_times)},
        }
    return results


def run_tsp_experiment(n_values, runs=30, seed=42):
    random.seed(seed)
    results = {}
    for n in n_values:
        times, lengths = [], []
        for _ in range(runs):
            cities = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]
            t0 = time.perf_counter()
            route = tsp_nearest_neighbor(cities)
            elapsed = time.perf_counter() - t0
            times.append(elapsed)
            lengths.append(route_length(cities, route))
        results[n] = {
            'time_mean':   statistics.mean(times),
            'time_std':    statistics.stdev(times),
            'length_mean': statistics.mean(lengths),
            'length_std':  statistics.stdev(lengths),
        }
    return results


if __name__ == '__main__':
    N_VALUES = [500, 2000, 8000]
    RUNS = 30

    print("=== Experimento: Inserção nas Árvores ===")
    tree_results = run_tree_experiment(N_VALUES, RUNS)
    for n, data in tree_results.items():
        print(f"\nn = {n}")
        for name, stats in data.items():
            print(f"  {name}: média={stats['mean']*1000:.4f} ms  desvio={stats['std']*1000:.4f} ms")

    print("\n=== Experimento: TSP Nearest Neighbor ===")
    tsp_results = run_tsp_experiment([20, 50, 100], RUNS)
    for n, data in tsp_results.items():
        print(f"\nn = {n} cidades")
        print(f"  Tempo: {data['time_mean']*1000:.4f} ms ± {data['time_std']*1000:.4f} ms")
        print(f"  Rota:  {data['length_mean']:.2f} ± {data['length_std']:.2f}")
