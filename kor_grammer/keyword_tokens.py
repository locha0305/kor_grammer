class TT_variable_statement():
    def __init__(self, variable_name):
        self.variable_name = variable_name
    def __repr__(self):
        return 'var {}'.format(self.variable_name)

class TT_set_variable_value_statement():
    def __init__(self, variable_name, value):
        self.variable_name = variable_name
        self.value = value
    def __repr__(self):
        return '{} = {}'.format(self.variable_name, self.value)

class TT_if_statement():
    def __init__(self, statement, block):
        self.statement = statement
        self.block = block
    def __repr__(self):
        return 'if({})'.format(self.statement) + '{' + str(self.block) + '}'

class TT_while_statement():
    def __init__(self, statement, block):
        self.statement = statement
        self.block = block
    def __repr__(self):
        return 'while({})'.format(self.statement) + '{' + str(self.block) + '}'