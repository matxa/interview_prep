#!/usr/bin/env python3
from linked_list import LinkedList
arr = [16, 18, 15, 14, 13, 11, 5, 3, 12, 1, 2, 19, 9, 20, 4]
# TEST
linked_list = LinkedList()
linked_list.add_from_array(arr)
print("LinkedList has {} nodes with the sum of {}".format(linked_list.length(), linked_list.list_sum()))
linked_list.print_ll()
linked_list.reverse()
print("LinkedList has {} nodes with the sum of {}".format(linked_list.length(), linked_list.list_sum()))
linked_list.print_ll()
