"""
Projeto 3 – Benchmark de Ordenação
Algoritmos: Merge Sort e Quick Sort
"""

import time
import random
import statistics


# ─────────────────────────────────────────────────────────────
# Merge Sort – O(n log n) em todos os casos
# ─────────────────────────────────────────────────────────────
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ─────────────────────────────────────────────────────────────
# Quick Sort – O(n log n) médio, O(n²) pior caso
# ─────────────────────────────────────────────────────────────
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


# ─────────────────────────────────────────────────────────────
# Experimentos
# ─────────────────────────────────────────────────────────────
def benchmark(sort_fn, arr):
    t0 = time.perf_counter()
    sort_fn(arr[:])          # cópia para não modificar original
    return time.perf_counter() - t0


def run_sort_experiment(n_values, runs=30, seed=42):
    random.seed(seed)
    results = {}
    for n in n_values:
        ms_best, ms_avg, ms_worst = [], [], []
        qs_best, qs_avg, qs_worst = [], [], []

        for _ in range(runs):
            # Casos de entrada
            random_arr  = random.sample(range(n * 5), n)
            sorted_arr  = list(range(n))            # melhor caso Merge Sort
            reversed_arr = list(range(n, 0, -1))    # pior caso Quick Sort naïve

            # Merge Sort
            ms_best.append(benchmark(merge_sort,   sorted_arr))
            ms_avg.append( benchmark(merge_sort,   random_arr))
            ms_worst.append(benchmark(merge_sort,  reversed_arr))

            # Quick Sort
            qs_best.append( benchmark(quick_sort,  sorted_arr))
            qs_avg.append(  benchmark(quick_sort,  random_arr))
            qs_worst.append(benchmark(quick_sort,  reversed_arr))

        results[n] = {
            'MergeSort': {
                'best':  {'mean': statistics.mean(ms_best),  'std': statistics.stdev(ms_best)},
                'avg':   {'mean': statistics.mean(ms_avg),   'std': statistics.stdev(ms_avg)},
                'worst': {'mean': statistics.mean(ms_worst), 'std': statistics.stdev(ms_worst)},
            },
            'QuickSort': {
                'best':  {'mean': statistics.mean(qs_best),  'std': statistics.stdev(qs_best)},
                'avg':   {'mean': statistics.mean(qs_avg),   'std': statistics.stdev(qs_avg)},
                'worst': {'mean': statistics.mean(qs_worst), 'std': statistics.stdev(qs_worst)},
            },
        }
    return results


if __name__ == '__main__':
    N_VALUES = [500, 2000, 8000]
    RUNS = 30

    print("=== Experimento: Benchmark de Ordenação ===")
    results = run_sort_experiment(N_VALUES, RUNS)
    for n, data in results.items():
        print(f"\nn = {n}")
        for algo, cases in data.items():
            for case_name, stats in cases.items():
                print(f"  {algo} [{case_name}]: {stats['mean']*1000:.4f} ms ± {stats['std']*1000:.4f} ms")
