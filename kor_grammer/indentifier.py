class TT_blank(): #
    def __init__(self):
        pass

class TT_right_paren(): #)
    def __init__(self):
        pass

class TT_left_paren(): #(
    def __init__(self):
        pass

class TT_right_mid_paren(): #}
    def __init__(self):
        pass

class TT_left_mid_paren(): #{
    def __init__(self):
        pass

class TT_right_big_paren(): #]
    def __init__(self):
        pass

class TT_left_big_paren(): #[
    def __init__(self):
        pass

class TT_is(): #=
    def __init__(self):
        pass

identifier = {
    ' ' : TT_blank,
    ')' : TT_right_paren,
    '(' : TT_left_paren,
    '}' : TT_right_mid_paren,
    '{' : TT_left_mid_paren,
    ']' : TT_right_big_paren,
    '[' : TT_left_big_paren,
    '는' : TT_is,
    '은' : TT_is
}