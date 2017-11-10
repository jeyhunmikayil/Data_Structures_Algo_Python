class Node:
    # konstruktor
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # node-un data field-ini mənimsətmək  üçün metod
    def set_data(self, data):
        self.data = data

    # node-un data field-ini almaq üçün metod
    def get_data(self):
        return self.data

    # node-un növbəti field-ini mənimsətmək üçün metod
    def set_next_node(self, next_node):
        self.next_node = next_node

    # node-un növbəti field-ini almaq üçün metod
    def get_next_node(self):
        return self.next_node

    # əgər bir node sonrakına point edirsə, true qaytar
    def has_next(self):
        return self.next_node is not None

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def circular_list_length(self):
        current_node = self.head

        if current_node == None:
            return 0

        count = 1
        current_node = current_node.get_next_node()
        # Dövri əlaqəli listdə yenidən head node-a gedib çıxmışıq ya yox, onu yoxlayırıq.
        while current_node != self.head:
            current_node = current_node.get_next_node()
            count = count + 1

        return count

    def print_data_circular_list(self):
        current_node = self.head

        if current_node == None:
            return 0

        print(current_node.get_data())
        current_node = current_node.get_next_node()
        while current_node != self.head:
            current_node = current_node.get_next_node()
            print(current_node.get_data())
