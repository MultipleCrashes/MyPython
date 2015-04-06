import Queue

class job(object):
        def __init__(self,priority,description,sector):
                self.priority=priority
                self.description=description
                self.sector=sector
                print 'Job,sector',description,sector
                return
        def __cmp__(self,other):
                return cmp(self.priority,other.priority)

q=Queue.PriorityQueue()
q.put(job(3,'Mid-level job','IT'))
q.put(job(10,'Low-level job','Engg'))
q.put(job(1,'Important Job','Science'))


while not q.empty():
        next_job=q.get()
        print 'processing job,description,sector -->',next_job.description,next_job.sector,next_job.priority
