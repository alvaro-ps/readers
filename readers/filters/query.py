from .filters import Filter
from .value_getters import ValueGetter
from .operations import Operation

class Query(object):
    def __init__(self, operator, op1, op2, **kwargs):
        try:
            self.op1 = ValueGetter(op1, **kwargs)
        except ValueError as err:
            try:
                self.op1 = Query(**op1)
            except TypeError as err:
                raise err
        try:
            self.op2 = ValueGetter(op2, **kwargs)
        except ValueError as err:
            try:
                self.op2 = Query(**op2)
            except TypeError as err:
                self.op2 = op2
        self.operator = Operation(operator)

        #self.op2 = Filter.fromConfig(op2)

    def __str__(self):
        return '(' + ' - '.join([str(self.op1), str(self.operator), str(self.op2)]) + ')'

    def __repr__(self):
        return self.__str__()

    def __call__(self, js):
        """
        Walks the tree and returns the boolean
        """
        op1 = self.op1(js)
        try:
            op2 = self.op2(js)
        except TypeError as err:
            op2 = self.op2

        return self.operator(op1, op2)
