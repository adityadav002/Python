class Grandparent:   # parent 1
    def show_grandparent(self):
        print("Grandparent: Wise and experienced.")

class Parent(Grandparent):  # parent 2 and child 1
    def show_parent(self):
        print("Parent: Responsible and caring.")

class Child(Parent):  # child 2
    def show_child(self):
        print("Child: Curious and playful.")

c = Child()

c.show_grandparent()
c.show_parent()
c.show_child()
