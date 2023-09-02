#!/usr/bin/python3
"""Defined Singly linked list and Node classes"""

class Node:
    """Class Node:
        defines a node structure of a singly linked list
        data (int):
            Private instance attribute to store integer included
            data entered must be an integer, otherwise a TypeError is raised
        next_node (Node / None):
            Private instance attribute that represent the next node
            Must be of type Node or None, otherwise a TypeError is raised
    """

    def __init__(self, data, next_node=None):
        """Initializes every instance created from class Node

        :param data: Integer to be included
        :param next_node: next node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node and isinstance(next_node, Node) is False:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Property(data) getter

        :return: the value of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Property(data) setter

        sets/resets the data of a node
        :param value: data to set
        :return: None
        """
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property(next_node) getter

        :return: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property (next_node) setter

        sets/resets the node of the list
        :param value:
        :return:
        """
        if value and isinstance(value, Node) is False:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Clas SinglyLinkedList:
        Defines a singly linked list
        head:
            Private instance attribute; represent the head of the list
        sorted_insert (method):
            inserts node in a sorted list
            value: Integer to be included
    """

    def __str__(self):
        """Prints out all the node's data of the list line by line
        :return: string representation of the list
        """
        elements = []
        while self.__head is not None:
            elements.append(str(self.__head.data))
            self.__head = self.__head.next_node

        return '\n'.join(elements)

    def __init__(self):
        """Instantiate list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in a sorted list
        :param value: Integer to be included
        :return: None
        """
        new = Node(value)

        # if new node value is smaller than head data
        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new  # Let new node be the head
        else:
            prev = None
            current = self.__head
            while current and value >= current.data:
                prev = current
                current = current.next_node

            if prev:
                prev.next_node = new
            new.next_node = current
