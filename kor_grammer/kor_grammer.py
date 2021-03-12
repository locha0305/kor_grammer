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
                    #키워드 찾기
                    if word in grammer.grammer:
                        if word == "변수": #변수 선언문
                            line_ = line.split(" ") #띄어쓰기로 쪼갬
                            if line_[2] != '정의':
                                raise SyntaxError('{}'.format(line_[2])) #문법 오류
                            else:
                                self.result.append(grammer.grammer[word]['grammer']['변수'](line_[1])) #결과에 토큰을 추가
                            cursor += len(line_) #커서 점프
                            word = '' #단어 초기화
                    else:
                        raise SyntaxError('{}'.format(word)) #문법 오류
                else:
                    word += letter #단어에 글자 저장
                cursor += 1 #커서값 증가
            idx += 1 #줄번호 증가
        
        return self.result

gr = Grammer('변수 가 정의\n변수 나 정의\n')
print(gr.tokenize())