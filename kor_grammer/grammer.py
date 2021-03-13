import keyword_tokens
import identifier

grammer = {
    "type_tokens":[
        "variable", "value", "statement", "block"
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
            "만약" : None, "statement" : None, "이라면" : None, "{" : identifier.TT_left_mid_paren, "block" : None, "}" : identifier.TT_right_mid_paren
        }
    }
}