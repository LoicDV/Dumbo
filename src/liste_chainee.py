import Node

class LC:
    def __init__(self):
        # Initialise une liste chainée vide.
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        # Traduit la liste chainée lors du print.
        res = ""
        tmp = self.head
        while tmp != None:
            res = res + str(tmp.data) + " --> "
            tmp = tmp.next
        res += "None"
        return res

    def isEmpty(self):
        """
        Retourne True si la liste chainée est vide.
        Retourne Faux sinon.
        """
        if self.size == 0:
            return True
        return False

    def length_LC(self):
        # Retourne la taille de la liste chainée.
        return self.size

    def isIn(self, obj):
        """
        Retourne True si l'objet se trouve dans la liste chainée.
        Retourne False si l'objet ne se trouve pas dans la liste chainée.
        """
        if self.size == 0:
            return False
        tmp = self.head
        while tmp != None:
            if tmp.data == obj:
                return True
            tmp = tmp.next
        return False

    def index_value(self, i):
        # Retourne la valeur (data) de la liste chainée à l'indice i.
        if i >= self.size:
            return None
        else:
            tmp = self.head
            compteur = 0
            while compteur != i:
                tmp = tmp.next
                compteur += 1
            return tmp.data

    def begin_insert(self, obj):
        if self.size == 0:
            out_list = Node.Node(obj)
            self.head = out_list
            self.tail = out_list
            self.size = 1
        else:
            out_list = Node.Node(obj)
            out_list.next = self.head
            self.head = out_list
            self.size += 1

    def end_insert(self, obj):
        if self.size == 0:
            out_list = Node.Node(obj)
            self.head = out_list
            self.tail = out_list
            self.size = 1
        else:
            out_list = Node.Node(obj)
            self.tail.next = out_list
            self.tail = out_list
            self.size += 1

    def begin_remove(self):
        if self.size == 0:
            print("Votre liste chainée est vide ! Elle est de la forme : ")
            return self
        tmp = self.head.next
        self.head = None
        self.head = tmp
        self.size -= 1

    def end_remove(self):
        if self.size == 0:
            print("Votre liste chainée est vide ! Elle est de la forme : ")
            return self
        tmp = self.head
        while tmp.next.next != None:
            tmp = tmp.next
        self.tail = tmp
        self.tail.next = None
        self.size -= 1

    def kill(self):
        # Reset votre liste chainée.
        self.head = None
        self.size = 0

    def insert_index(self, obj, i):
        """
        !!! Utilisation des fonctions begin_insert(self, obj) et end_insert(self, obj) !!!
        Permet d'ajouter le maillon obj à l'index i.
        """
        if i == 0:
            LC.begin_insert(self, obj)
        elif i == self.size - 1:
            LC.end_insert(self, obj)
        elif i > self.size:
            print("L'index est trop grand par rapport à la liste, votre liste chainée reste : ")
            print(self)
        else:
            compteur = 0
            tmp = self.head
            while compteur != i-1:
                tmp = tmp.next
                compteur += 1
            elem = Node.Node(obj)
            elem.next = tmp.next
            tmp.next = elem
            self.size += 1

    def remove_index(self, i):
        """
        !!! Utilisation des fonctions begin_remove(self) et end_remove(self) !!!
        Permet de retirer le maillon à l'index i.
        """
        if self.size == 0:
            return self
        if i == 0:
            LC.begin_remove(self)
        elif i == self.size - 1:
            LC.end_remove(self)
        elif i >= self.size:
            print("L'index est trop grand par rapport à la liste, votre liste chainée reste : ")
        else:
            compteur = 0
            tmp = self.head
            while compteur != i - 1:
                tmp = tmp.next
                compteur += 1
            tmp.next = tmp.next.next
            self.size -= 1