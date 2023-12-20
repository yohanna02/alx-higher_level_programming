#!/usr/bin/python3
"""
This module defines a simple singly linked list class.

Class:
    Node: Represents a Node.

Attributes:
    None
"""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference to the next node.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value (Node): The new reference to the next node.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.
    """
    def __init__(self):
        """
        Initializes a SinglyLinkedList instance.

        Attributes:
            head (Node): The head node of the linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and\
                    value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representing the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
