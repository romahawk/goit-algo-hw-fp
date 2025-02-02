class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def insertion_sort_list(head):
    if not head:
        return head

    sorted_list = ListNode(float('-inf'))
    current = head

    while current:
        prev = sorted_list
        while prev.next and prev.next.value < current.value:
            prev = prev.next

        next_node = current.next
        current.next = prev.next
        prev.next = current
        current = next_node

    return sorted_list.next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return dummy.next

#

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def create_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next

if __name__ == "__main__":
    # Створення прикладу списку
    values = [4, 2, 1, 3]
    head = create_list(values)
    print("Оригінальний список:")
    print_list(head)

    # Реверсування списку
    reversed_head = reverse_list(head)
    print("Реверсований список:")
    print_list(reversed_head)

    # Сортування списку методом вставок
    sorted_head = insertion_sort_list(reversed_head)
    print("Відсортований список (методом вставок):")
    print_list(sorted_head)

    # Створення другого списку для об'єднання
    values2 = [5, 3, 6]
    head2 = create_list(values2)
    sorted_head2 = insertion_sort_list(head2)

    # Об'єднання двох відсортованих списків
    merged_head = merge_sorted_lists(sorted_head, sorted_head2)
    print("Об'єднаний відсортований список:")
    print_list(merged_head)
