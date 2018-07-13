# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hashmap = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if (len(self.hashmap[query.ind]) == 0) :
                print(" ")
            else:
                self.write_chain(cur for cur in reversed(self.hashmap[query.ind]))
        else:
            ind = self._hash_func(query.s)
            if query.type == 'find':
                lis = self.hashmap[ind]
                if query.s in lis:
                    print("yes")
                else:
                    print("no")
            if query.type == 'add':
                lis = self.hashmap[ind]
                if query.s not in lis:
                    lis.append(query.s)
            if query.type == 'del':
                if query.s in self.hashmap[ind]:
                    self.hashmap[ind].remove(query.s)
            if query.type == 'inspect':
                print(self.hashmap)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
