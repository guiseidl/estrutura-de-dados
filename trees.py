"""
Projeto 1 - Árvores e Balanceamento
Implementação: BST, AVL, Rubro-Negra
"""

# ─────────────────────────────────────────────────────────────
# BST – Árvore Binária de Busca
# ─────────────────────────────────────────────────────────────
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Substitui pelo menor da subárvore direita
            min_node = self._min(node.right)
            node.key = min_node.key
            node.right = self._remove(node.right, min_node.key)
        return node

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


# ─────────────────────────────────────────────────────────────
# AVL – Árvore AVL
# ─────────────────────────────────────────────────────────────
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def _h(self, n):
        return n.height if n else 0

    def _bf(self, n):
        return self._h(n.left) - self._h(n.right) if n else 0

    def _update(self, n):
        n.height = 1 + max(self._h(n.left), self._h(n.right))

    def _rot_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self._update(z)
        self._update(y)
        return y

    def _rot_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update(z)
        self._update(y)
        return y

    def _balance(self, n):
        self._update(n)
        bf = self._bf(n)
        if bf > 1:
            if self._bf(n.left) < 0:
                n.left = self._rot_left(n.left)
            return self._rot_right(n)
        if bf < -1:
            if self._bf(n.right) > 0:
                n.right = self._rot_right(n.right)
            return self._rot_left(n)
        return n

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        return self._balance(node)

    def search(self, key):
        n = self.root
        while n:
            if key == n.key:
                return n
            n = n.left if key < n.key else n.right
        return None

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            mn = node.right
            while mn.left:
                mn = mn.left
            node.key = mn.key
            node.right = self._remove(node.right, mn.key)
        return self._balance(node)

    def height(self):
        return self._h(self.root)


# ─────────────────────────────────────────────────────────────
# Rubro-Negra (Red-Black Tree)
# ─────────────────────────────────────────────────────────────
RED = True
BLACK = False


class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = BLACK
        self.root = self.NIL

    def insert(self, key):
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL
        self._bst_insert(node)
        self._fix_insert(node)

    def _bst_insert(self, node):
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            elif node.key > x.key:
                x = x.right
            else:
                return  # duplicata ignorada
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def _fix_insert(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._rot_left(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._rot_right(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_left(z.parent.parent)
        self.root.color = BLACK

    def _rot_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rot_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, key):
        n = self.root
        while n != self.NIL:
            if key == n.key:
                return n
            n = n.left if key < n.key else n.right
        return None

    def remove(self, key):
        z = self.search(key)
        if z is None:
            return
        self._delete(z)

    def _delete(self, z):
        y = z
        y_orig_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._min(z.right)
            y_orig_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_orig_color == BLACK:
            self._fix_delete(x)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _min(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rot_left(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._rot_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._rot_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rot_right(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._rot_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._rot_right(x.parent)
                    x = self.root
        x.color = BLACK

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node == self.NIL:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
