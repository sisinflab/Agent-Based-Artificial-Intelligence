class Constraint:
    def __init__(self, variables):
        self.variables = variables
        self.degree = len(variables)

    def check(self, state):
        return True


class UnaryConstraint(Constraint):
    def __init__(self, variable):
        self.variable = variable
        super(UnaryConstraint, self).__init__(variables=variable)

    def check(self, state):
        return True


class ValueConstraint(UnaryConstraint):

    def __init__(self, variable, accepted_values):
        super(ValueConstraint, self).__init__(variable)
        self.accepted_values = accepted_values

    def check(self, state):
        if self.variable in state:
            return state[self.variable] in self.accepted_values
        return True


class DifferentValues(Constraint):

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        return len(values) == len(set(values))


class EqualValues(Constraint):

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        if values:
            return len(set(values)) == 1
        else:
            return True


class MaximumCapacity(UnaryConstraint):
    def __init__(self, variable, max_capacity):
        super(MaximumCapacity, self).__init__(variable)
        self.maxCapacity = max_capacity

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        return all([values.count(x) <= self.maxCapacity for x in values])




'''
class MaximumCapacity(UnaryConstraint):
    def __init__(self, variable, max_capacity):
        super(MaximumCapacity, self).__init__(variable)
        self.maxCapacity = max_capacity
        
    def check(self, state):
        if self.variable in state:
            return len(state[self.variable]) <= self.maxCapacity
        return True


class UniqueValue(UnaryConstraint):
    def __init__(self, variable, values):
        super(UniqueValue, self).__init__(variable)
        self.values = values

    def check(self, state):
        if self.variable in state:
            in_list = [state[var] for var in self.variables if state[var] in self.values]
            return len(in_list) < 2
        return True
    
class NotInSame(Constraint):
'''