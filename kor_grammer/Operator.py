import identifier

class TT_add(): 
    def __init__(self):
        pass

class TT_sub():
    def __init__(self):
        pass

class TT_mul():
    def __init__(self):
        pass

class TT_div():
    def __init__(self):
        pass

class TT_pow():
    def __init__(self):
        pass

class TT_equal():
    def __init__(self):
        pass

class TT_not_equal():
    def __init__(self):
        pass

class TT_bigger():
    def __init__(self):
        pass

class TT_bigger_or_equal():
    def __init__(self):
        pass

class TT_smaller():
    def __init__(self):
        pass

class TT_smaller_or_equal():
    def __init__(self):
        pass

class TT_or():
    def __init__(self):
        pass

class TT_and():
    def __init__(self):
        pass

class TT_end_of_statement():
    def __init__(self):
        pass

class TT_mod():
    def __init__(self):
        pass

class TT_int_div():
    def __init__(self):
        pass


operator = {
    'one_char' : {
        '+' : TT_add,
        '-' : TT_sub,
        '*' : TT_mul,
        '/' : TT_div,
        '^' : TT_pow,
        '%' : TT_mod,
        '>' : TT_smaller,
        '<' : TT_bigger,
        '(' : identifier.TT_left_paren,
        ')' : identifier.TT_right_paren,
        '[' : identifier.TT_left_big_paren,
        ']' : identifier.TT_right_big_paren,
        '$' : TT_end_of_statement
    },
    'two_char' : {
        '==' : TT_equal,
        '!=' : TT_not_equal,
        '>=' : TT_smaller_or_equal,
        '<=' : TT_bigger_or_equal,
        '&&' : TT_and,
        '||' : TT_or,
        '//' : TT_int_div
    }
}