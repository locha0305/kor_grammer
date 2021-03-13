import grammer
import keyword_tokens
import identifier

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
                if letter in identifier.identifier:
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

                            elif word == "만약": #if문
                                line_ = line.split(" ") #띄어쓰기로 쪼갬
                                if line_[2][-1] != '{':
                                    raise SyntaxError("'{'가 없음")
                                else:
                                    line_[2] = line_[2].strip('{') #{ 떼어냄
                                
                                if line_[2] != '이라면':
                                    raise SyntaxError('{}'.format(line_[2])) #문법 오류
                                else:
                                    jump = 0
                                    block = ''
                                    while self.code[idx + jump] != '}':
                                        jump += 1
                                        if jump >= 10**3:
                                            raise SyntaxError("'}'가 없음")
                                        else:
                                            block += self.code[idx + jump] + '\n'
                                    instant_runner = type(self)(block.strip(';').strip('}')) #맨 뒤 '}' 떼기
                                    self.result.append(keyword_tokens.TT_if_statement(line_[1], instant_runner.tokenize())) #if문안에 if문이 있을수 있어 토큰화 시켜 반환
                                word = '' #단어 초기화
                                
                                idx += jump
                                
                                break #불필요한 에러 방지


                        else:
                            pass
                            
                else:
                    word += letter #단어에 글자 저장
                cursor += 1 #커서값 증가
            idx += 1 #줄번호 증가
        
        return self.result

gr = Grammer('변수 가 정의\n가는 3\n만약 가==3 이라면{\n나는 5\n가는 3\n만약 가+나==8 이라면{\n가는 7\n}\n}')
print(gr.tokenize())