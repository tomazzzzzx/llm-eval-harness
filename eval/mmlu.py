class MMLUEvaluator:
    def __init__(self, fn, subjects=None): self.fn, self.subs = fn, subjects or ["abstract_algebra"]
    def evaluate(self):
        r = {}
        for s in self.subs:
            data = self.load(s)
            r[s] = sum(1 for q in data if self.fn(q["question"]).strip()==q["answer"])/max(len(data),1)
        r["overall"] = sum(r.values())/len(r); return r
    def load(self, s): return []
