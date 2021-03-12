import keyword_tokens

grammer = {
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
    }
}