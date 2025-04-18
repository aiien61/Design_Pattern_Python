class SchedulingRule:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler
        return handler
    
    def apply(self, job):
        if self.next:
            return self.next.apply(job)
        return f"❌ 沒有適用的排程規則: {job['job_id']}"
    
# FIFO Rule
class FIFORule(SchedulingRule):
    def apply(self, job):
        if job['urgent'] is False and job['batch_size'] <= 50:
            return f"✅ 使用 FIFO 規則排程: {job['job_id']}"
        return super().apply(job)
    
# LPT Rule
class LPTRule(SchedulingRule):
    def apply(self, job):
        if job['batch_size'] > 100:
            return f"✅ 使用 LPT 規則排程: {job['job_id']}"
        return super().apply(job)

# EDD Rule
class EDDRule(SchedulingRule):
    def apply(self, job):
        if job['due_days'] < 2:
            return f"✅ 使用 EDD 規則排程: {job['job_id']}"
        return super().apply(job)

if __name__ == "__main__":
    fifo = FIFORule()
    lpt = LPTRule()
    edd = EDDRule()

    fifo.set_next(lpt).set_next(edd)

    jobs = [
        {"job_id": "J01", "urgent": False, "batch_size": 30, "due_days": 5},
        {"job_id": "J02", "urgent": True, "batch_size": 120, "due_days": 4},
        {"job_id": "J03", "urgent": True, "batch_size": 10, "due_days": 1},
        {"job_id": "J04", "urgent": False, "batch_size": 90, "due_days": 10},
    ]

    for job in jobs:
        print(fifo.apply(job))
