import random


class MemberInQueue:
    def __init__(self, name):
        self.name = name
        self.weight = random.randint(1, 100)


class PrioityQueue:
    def __inin__(self):
        self.pqueue = list()

    def enqueue(self, name):
        member = MemberInQueue(name)
        self.pqueue.append(member)
        self.pqueue.sort(key=lambda x: x.weight, reverse=True)

    def dequeue(self):
        return self.pqueue[0] if len(self.pqueue) > 0 else None

    def trace_overall(self):
        print([(member.name, member.weight) for member in self.pqueue])


if __name__ == "__main__":
    member_prioity_queue = PrioityQueue()
    member_prioity_queue.enqueue("Peter")
    member_prioity_queue.trace_overall()
    member_prioity_queue.enqueue("Machi")
    member_prioity_queue.trace_overall()
    member_prioity_queue.enqueue("Jayce")
    member_prioity_queue.trace_overall()

    # thread-safe
