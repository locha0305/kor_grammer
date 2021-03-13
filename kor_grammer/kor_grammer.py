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
                    elif letter == "{":
                        if word == "동안": #while문
                            line_ = line.split(" ") #띄어쓰기로 쪼갬
                            for tok in line_: #들여쓰기
                                    if tok == '':
                                        del line_[line_.index(tok)] #빈칸 없애기
                            if line_[0][-1] != '인':
                                raise SyntaxError("'인'이 없음") 
                
                            
                            if line_[1][-1] != '{':
                                raise SyntaxError("'{'가 없음")
                            else:
                                line_[1].strip('{')
                            jump = 0
                            block = ''
                            while self.code[idx + jump] != '}':
                                jump += 1
                                if jump >= 10 ** 3:
                                    raise SyntaxError("'}'가 없음")
                                else:
                                    block += self.code[idx + jump] + '\n'
                            word = '' #단어 초기화
                            idx += jump
                            instant_runner = type(self)(block.strip('}'))
                            self.result.append(keyword_tokens.TT_while_statement(line_[0].strip("인"), instant_runner.tokenize()))
                    elif letter == " ":
                        if word in grammer.grammer:
                            if word == "변수": #변수 선언문
                                line_ = line.split(" ") #띄어쓰기로 쪼갬
                                for tok in line_: #들여쓰기
                                    if tok == '':
                                        del line_[line_.index(tok)] #빈칸 없애기
                                if line_[-1] != '정의':
                                    raise SyntaxError('{}'.format(line_[2])) #문법 오류
                                else:
                                    self.result.append(grammer.grammer[word]['grammer']['변수'](line_[1])) #결과에 토큰을 추가
                                word = '' #단어 초기화
                                break #불필요한 에러 방지

                            elif word == "만약": #if문
                                line_ = line.split(" ") #띄어쓰기로 쪼갬
                                if line_[-1][-1] != '{':
                                    raise SyntaxError("'{'가 없음")
                                else:
                                    line_[-1] = line_[-1].strip('{') #{ 떼어냄
                                
                                if line_[-1] != '이라면':
                                    raise SyntaxError('{}'.format(line_[-1])) #문법 오류
                                
                                jump = 0
                                block = ''
                                while self.code[idx + jump] != '}':
                                    jump += 1
                                    if jump >= 10**3:
                                        raise SyntaxError("'}'가 없음")
                                    else:
                                        block += self.code[idx + jump] + '\n'
                                instant_runner = type(self)(block.strip('}')) #맨 뒤 '}' 떼기
                                self.result.append(keyword_tokens.TT_if_statement(line_[1], instant_runner.tokenize())) #if문안에 if문이 있을수 있어 토큰화 시켜 반환
                                word = '' #단어 초기화
                                
                                idx += jump
                                
                                break #불필요한 에러 방지
                            else:
                                word = ''
                        else:
                            word = ''
                    else:
                        pass      
                else:
                    word += letter #단어에 글자 저장
                cursor += 1 #커서값 증가
            idx += 1 #줄번호 증가
        
        return self.result


with open('test.txt', 'r', encoding='UTF-8') as file:
    f = ''.join(file.readlines())
print(f)
gr = Grammer(f)
print(gr.tokenize())

