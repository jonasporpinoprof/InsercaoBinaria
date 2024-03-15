class Node:
    def __init__(self, key):
        self.left = None  # Nó filho esquerdo
        self.right = None  # Nó filho direito
        self.val = key  # Valor do nó

def insert(root, key):
    # Se a árvore estiver vazia, retorna um novo nó como raiz
    if root is None:
        return Node(key)
    else:
        # Se o valor a ser inserido for menor que o valor da raiz, insere na subárvore esquerda
        if key < root.val:
            root.left = insert(root.left, key)
        # Caso contrário, insere na subárvore direita
        else:
            root.right = insert(root.right, key)
    return root

def print_tree(root, level=0):
    # Função para imprimir a árvore
    if root:
        print_tree(root.right, level + 1)  # Imprime a subárvore direita
        print('  ' * level + str(root.val))  # Imprime o valor do nó atual
        print_tree(root.left, level + 1)  # Imprime a subárvore esquerda

def inorder(root):
    # Função para percorrer a árvore em ordem e imprimir os valores
    if root:
        inorder(root.left)  # Visita a subárvore esquerda
        print(root.val)  # Visita o nó atual
        inorder(root.right)  # Visita a subárvore direita

# Exemplo de uso:
root = None  # Inicializa a raiz da árvore como vazia
root = insert(root, 50)  # Insere um nó com valor 50 na árvore
insert(root, 30)  # Insere outros nós na árvore
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

