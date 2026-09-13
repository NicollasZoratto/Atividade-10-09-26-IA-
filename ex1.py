import networkx as nx

G = nx.Graph()
G.add_edge("São Paulo", "Campinas")
G.add_edge("Campinas", "Ribeirão Preto")
G.add_edge("São Paulo", "Santos")
G.add_edge("Santos", "Curitiba")
G.add_edge("Campinas", "Curitiba")
G.add_edge("Ribeirão Preto", "Belo Horizonte")

origem = "São Paulo"
destino = "Curitiba"

rota = nx.shortest_path(G, source=origem, target=destino)
print(f"Rota: {rota}")

tamanho = nx.shortest_path_length(G, source=origem, target=destino)
print(f"Tamanho do caminho: {tamanho}") 