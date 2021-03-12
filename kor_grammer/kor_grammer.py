import grammer
import keyword_tokens
import indentifier

class Grammer():
    def __init__(self, code):
        self.code = code.split("\n")
        self.result = []
    def tokenize(self):
        cursor = 0 #커서 초기화
        idx = 0 #줄번호 초기화

        letter = '' #글자 초기화
        word = '' #단어 초기화
        

        while idx < len(self.code):
            line = self.code[idx] #줄
            cursor = 0 #커서 초기화

            word = '' #단어 초기화
            letter = '' #글자 초기화
            
            while cursor < len(line):
                letter = line[cursor] #글자
                if letter in indentifier.identifier:
                    if letter == "는" or letter == "은": #변수값 설정문
                        if letter == "는":
                            line_ = line.split("는")
                        else:
                            line_ = line.split("은")
                        var_name = line_[0] #변수 이름
                        var_value = line_[1].split(" ")[1] #변수 값
                        self.result.append(keyword_tokens.TT_set_variable_value_statement(var_name, var_value)) #결과에 토큰을 추가
                        break #불필요한 에러 방지
                    
                    #키워드 찾기
                    else:
                        if word in grammer.grammer:
                            if word == "변수": #변수 선언문
                                line_ = line.split(" ") #띄어쓰기로 쪼갬
                                if line_[2] != '정의':
                                    raise SyntaxError('{}'.format(line_[2])) #문법 오류
                                else:
                                    self.result.append(grammer.grammer[word]['grammer']['변수'](line_[1])) #결과에 토큰을 추가
                                word = '' #단어 초기화
                                break #불필요한 에러 방지
                        else:
                            raise SyntaxError('{}'.format(word)) #문법 오류
                else:
                    word += letter #단어에 글자 저장
                cursor += 1 #커서값 증가
            idx += 1 #줄번호 증가
        
        return self.result

gr = Grammer('변수 가 정의\n가는 3\n가는 가+1\n변수 나 정의\n나는 가+1\n나는 나+가')
print(gr.tokenize())