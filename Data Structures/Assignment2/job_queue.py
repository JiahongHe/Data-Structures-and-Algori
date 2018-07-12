# python3
from queue import PriorityQueue

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    class Worker:
        def __init__(self, i):
            self.id = i;
            self.nextFreeTime = 0;

        def __gt__(self, other):
            if self.nextFreeTime == other.nextFreeTime:
                return self.id > other.id
            else:
                return self.nextFreeTime > other.nextFreeTime

        def __lt__(self, other):
            if self.nextFreeTime == other.nextFreeTime:
                return self.id < other.id
            else:
                return self.nextFreeTime < other.nextFreeTime

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        queue = PriorityQueue();
        for i in range(self.num_workers):
            queue.put(self.Worker(i))
        for i in range(len(self.jobs)):
            worker = queue.get()
            self.assigned_workers[i] = worker.id
            self.start_times[i] = worker.nextFreeTime
            worker.nextFreeTime += self.jobs[i]
            queue.put(worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

