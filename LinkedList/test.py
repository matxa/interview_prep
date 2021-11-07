#!/usr/bin/env python3
from linked_list import LinkedList
arr = [12, 1, -1, 32, 10]
# TEST
linked_list = LinkedList()
linked_list.add_from_array(arr)
print("LinkedList has {} nodes".format(linked_list.length()))
linked_list.print_ll()
