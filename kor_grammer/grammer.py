import keyword_tokens
import identifier

grammer = {
    "type_tokens":[
        "variable", "value", "statement", "block", "list", "function"
    ],
    "변수" : {
        "grammer" : {
            "변수" : keyword_tokens.TT_variable_statement, "variable" : None, "정의" : None
        }

    },
    "변수 값 설정" : {
        "grammer" : {
            "type1" : {
                "variable" : None, "은" : None, "value" : None
            },
            "type2" : {
                "variable" : None, "는" : None, "value" : None
            }
        }
    },
    "만약" : {
        "grammer" : {
            "만약" : keyword_tokens.TT_if_statement, "statement" : None, "이라면" : None, "{" : identifier.TT_left_mid_paren, "block" : None, "}" : identifier.TT_right_mid_paren
        }
    },
    "동안" : {
        "grammer" : {
            "statement" : None, "인" : None, "동안" : None, "{" : identifier.TT_left_mid_paren, "block" : None, "}" : identifier.TT_right_mid_paren
        }
    },
    "대해" : {
        "grammer" : {
            "list" : None, "인" : None, "variable" : None, "에" : None, "대해" : None, "{" : identifier.TT_left_mid_paren, "block" : None, "}" : identifier.TT_right_mid_paren
        }
    },
    "함수" : {
        "grammer" : {
            "함수" : None, "function" : None, "정의" : None, "{" : identifier.TT_left_mid_paren, "block" : None, "}" : identifier.TT_right_mid_paren
        }
    }
}