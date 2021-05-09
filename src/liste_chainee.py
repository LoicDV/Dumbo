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

    def begin_remove(self):
        if self.size == 0:
            print("Votre liste chainée est vide ! Elle est de la forme : ")
            return self
        tmp = self.head.next
        res = self.head
        self.head = tmp
        self.size -= 1
        return res