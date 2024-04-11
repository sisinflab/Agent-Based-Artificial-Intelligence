class AC3:
    def __init__(self, csp):
        self.csp = csp

    def all_arcs(self):
        queue = []
        for cons in self.csp.constraints:
            if cons.degree == 2:
                queue.append(cons)
        return queue

    def add_neighbours(self, queue, arc):
        var, _ = arc.variables
        neighbours = [arc for arc in self.all_arcs() if arc.variables[1] == var]
        queue.extend(neighbours)

    def run(self, state):
        # initial queue with all the arcs in the problem
        queue = self.all_arcs()

        # while the queue is not empty
        while queue:
            # select an arc from the queue
            arc = queue.pop()
            if 0 in [len(v) for k, v in self.csp.domains.items()]:
                return False
            if self.csp.remove_inconsistent_values(arc=arc, actual_state=state):
                self.add_neighbours(queue, arc)
        return True
