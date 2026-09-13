import networkx as nx
import timeit

G = nx.Graph()
G.add_edge("São Paulo", "Campinas", weight=95)
G.add_edge("Campinas", "Ribeirão Preto", weight=220)
G.add_edge("São Paulo", "Santos", weight=70)
G.add_edge("Santos", "Curitiba", weight=410)
G.add_edge("Campinas", "Curitiba", weight=490)
G.add_edge("Ribeirão Preto", "Belo Horizonte", weight=550)

origem = "São Paulo"
destino = "Curitiba"

rota_dijkstra = nx.shortest_path(G, source=origem, target=destino, weight='weight', method='dijkstra')
print(f"Rota (Dijkstra): {rota_dijkstra}")

rota_bellman = nx.shortest_path(G, source=origem, target=destino, weight='weight', method='bellman-ford')
print(f"Rota (Bellman-Ford): {rota_bellman}")

print(f"Resultados idênticos? {rota_dijkstra == rota_bellman}")

tempo_dijkstra = timeit.timeit(
    lambda: nx.shortest_path(G, source=origem, target=destino, weight='weight', method='dijkstra'),
    number=10000
)

tempo_bellman = timeit.timeit(
    lambda: nx.shortest_path(G, source=origem, target=destino, weight='weight', method='bellman-ford'),
    number=10000
)

print(f"Tempo Dijkstra (10k execuções): {tempo_dijkstra:.5f} segundos")
print(f"Tempo Bellman-Ford (10k execuções): {tempo_bellman:.5f} segundos")