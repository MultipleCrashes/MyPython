

class Link:

    def __init__(self, data):
        self.data = data 
        self.next = None 


def display_link(head):
    while head:
        print(head.data) 
        head = head.next 


if __name__=='__main__':
    link_obj = Link(10)
    link_obj.next = Link(20)
    link_obj.next = Link(30)
    display_link(link_obj)

