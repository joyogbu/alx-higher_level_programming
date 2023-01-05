#!/usr/bin/python3
"""Defining a linked list classes"""


class Node:
    """Represent a node in the singly lisnked list"""

    def __init__(self, data, next_node=None):
        """Initalizing a new node

        Args:
        data(int): node data
        next_node(Node): next node to the new node
        """
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """get new node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set new node data"""
        if not(isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get Node next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set Node next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """reoresenting methods for the the singly linked list"""
    def __init__(self):
        """initializing list with head node"""
        self.__head = None

    def sorted_insert(self, value):
        """adding nodes to the list"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while (curr.next_node is not None and curr.next_node.data < value):
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """representing the print method of the list"""
        values = []
        curr = self.__head
        while(curr):
            values.append(str(curr.data))
            curr = curr.next_node
        return('\n'.join(values))
