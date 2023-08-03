codecs = ["cp1252", "cp437", "utf - 16"]
with open('C:/Users/kyms/Desktop/2 курс/Теория формальных языков/КР/лаб 4/codef4.txt', "r",encoding = 'utf - 8') as f:
    s= f.read()

TokenList=[]
now = 0
CS ='H'
strk =1
num = ['0','1','2','3','4','5','6','7','8','9']
errors = False
while (now< len(s)-1):
    if CS == 'H': #H
        while (s[now] in ['\t', '\n', ' ']):
            if s[now] == '\n':
                strk+=1
            now+=1
        if s[now] in ['!', '=', '<', '>']:

            CS = 'RA'
            continue
        if s[now] == '{':

            CS = 'COMM'
            continue
        if s[now] in ['+', '-', '|']:

            CS = 'SUM'
            continue
        if s[now] in ['*', '/','&']:

            CS= 'MUL'
            continue
        if s[now]=='!':

            CS = 'NOT'
            continue
        if s[now].isalpha() or s[now] == '_':

            CS = 'ID' 
            continue
        elif s[now] in ['.','+','-'] or s[now] in ['0', '1','2','3','4','5','6','7','8','9']:

            CS = 'NM'
            continue
        elif s[now] == ":":

            CS = 'ASGN'
            continue
        else:

            CS = 'DLM'
            continue
        break
    if CS == 'MUL':
        if s[now] in ['*','/']:
            b = {'MUL': s[now]}
            TokenList.append(b)
            now+=1
            CS = 'H'
            continue
        if s[now] == '&':
            now+=1
            if s[now] == '&':
                b = {'MUl': s[now-1]+s[now]}
                TokenList.append(b)
                now+=1
                CS = 'H'
                continue
            else:
                error_sim = s[now]
                CS = 'ERR'
                continue
    if CS == 'SUM':
        if s[now] == '+':
            b = {'SUM': s[now]}
            TokenList.append(b)
            now+=1
            CS = 'H'
            continue
        if s[now] == '-':
            b = {'SUM': s[now]}
            TokenList.append(b)
            now+=1
            CS = 'H'
            continue
        if s[now] == '|':
            now+=1
            if s[now] == '|':
                b = {'SUM': s[now-1]+s[now]}
                TokenList.append(b)
                now+=1
                CS = 'H'
                continue
            else:
                error_sim = s[now]
                CS = 'ERR'
                continue
        break
    if CS == 'RA':
        if s[now] == '!':
            now+=1
            if s[now] == '=':
                b = {'ratio': s[now-1]+s[now]}
                TokenList.append(b)
                now+=1
                CS = 'H'
                continue
            else:
                b = {'negative': s[now-1]}
                TokenList.append(b)
                CS = 'H'
                continue
        if s[now] == '=':
            now+=1
            if s[now] == '=':
                b = {'ratio': s[now-1]+s[now]}
                TokenList.append(b)
                now+=1
                CS = 'H'
                continue
            else:
                CS = 'H'
                continue
        if s[now] == '<':
            now+=1
            if s[now] == '=':
                b = {'ratio': s[now-1]+s[now]}
                TokenList.append(b)
                now+=1
                CS = 'H'
                continue
            else:
                b = {'ratio': s[now-1]}
                TokenList.append(b)
                CS = 'H'
                continue            
        if s[now] == '>':
            now+=1
            if s[now] == '=':
                b = {'ratio': s[now-1]+s[now]}
                TokenList.append(b)
                now+=1
                CS = 'H'
                continue
            else:
                b = {'ratio': s[now-1]}
                TokenList.append(b)
                CS = 'H'
                continue
        break
    if CS == 'ASGN': #ASGN
        now+=1
        num=0
        if s[now] == '=':
            b = {'assignment': s[now-1]+s[now]}
            TokenList.append(b)
            now+=1
            CS = 'H'
            continue
        else:
            error_sim = s[now]
            CS = 'ERR'
            continue
        break
    if CS == 'COMM':#COMM
        str=""
        er=0
        while s[now]!= '}':
            if now == len(s)-1:
                print ('error, out of range comm')
                er=1
                CS = 'ERR'
                error_sim = s[len(s)-1]
                break
            if s[now] == '\n':
                er=1
                CS = 'ERR'
                error_sim = '/n'
                break          
            str += s[now]
            now+=1
        if er == 1:
            continue
        str +=s[now]
        now+=1
        b = {'COMM': str}
        TokenList.append(b)
        CS = 'H'
        continue
    if CS == 'DLM':#DLM
        if s[now] is '(' or ')':
            if s[now] is '(':
                b = {'open_mark': s[now]}
            else:
                b = {'close_mark': s[now]}
            TokenList.append(b)
            now+=1
            CS = 'H'
            continue
        else:
            error_sim = s[now]
            now+=1
            CS = 'ERR'
            continue
        break
    if CS == 'ERR':
        errors = True
        print("Неизвестный символ:", '"',error_sim, '"', "строка: ",strk)
        CS = 'H' 
        break
    if CS == 'ID':
        str=""
        var ='0'
        if s[now] in ['0','1','2','3','4','5','6','7','8','9']:
            CS = 'NM'
            break
        while (s[now].isalpha()) or (s[now] in ['0','1','2','3','4','5','6','7','8','9']) or (s[now] == '_') or s[now]==',':
            if s[now] ==',':
                break
            else:
                str+=s[now]
                now+=1
        if str in ['for', 'to', 'next', 'step']:
            if str == 'for':
               b = {'FOR': str}
            elif str == 'to':
                b = {'TO': str}
            elif str == 'next':
                b = {'NEXT': str}
            elif str == 'step':
                b = {'STEP': str}
            TokenList.append(b)
        elif str in ['while']:
            b = {'WHILE': str}
            TokenList.append(b)
        elif str == 'readln':
            b = {'READLN': str}
            TokenList.append(b)
        elif str == 'writeln':
            b = {'WRITELN': str}
            TokenList.append(b)
        elif str in ['program', 'var', 'begin', 'end']:
            if str == 'begin':
                b = {'OP_START': str}
            elif str == 'var':
                b = {'var': str}
            elif str == 'end':
                b = {'OP_END': str}
            else:
                b = {'STRUCT_PROG': str}
            TokenList.append(b)
        elif str in ['int','float','bool']:
            b= {'DATA_TIPE': str}
            TokenList.append(b)
        elif str in ['if', 'else']:
            if str == 'if':
                b = {'COND': str}
            else:
                b = {'ELSE': str}
            TokenList.append(b)
        elif str in ['true', 'false']:
            b = {'TRUE': str}
            TokenList.append(b)
        else:
            b = {'variable': str}
            TokenList.append(b)
        if s[now] == ',':
            b = {'RAZD': ','}
            TokenList.append(b)
            now+=1
            CS='H'
            continue
        else:            
            CS='H'
            continue
    if CS == 'NM':
        num=""
        dot_was=0
        E_was =0
        sim_was=0
        err=0
        while s[now] == '+' or s[now] == '-' or s[now] == 'e' or s[now] == 'E' or s[now] in ['0','1','2','3','4','5','6','7','8','9'] or s[now] == '.':
            if s[now] in ['+','-'] and s[now-1] != ('E' or 'e'):
                CS = 'SUM'
                break
            if s[now] == '&':
                CS = 'MUL'
                break
            if s[now] == '.':
                if dot_was == 1 or E_was ==1 or sim_was ==1:
                    err =1
                    break
                else:
                    num+=s[now]
                    dot_was=1
                    if now<len(s)-1:
                        now+=1
                    continue
            elif s[now] == 'E' or s[now] == 'e':
                if E_was ==1 or dot_was ==0:
                    err =1
                    break
                else:
                    num+=s[now]
                    E_was = 1
                    if now<len(s)-1:
                        now+=1
                    continue
            elif s[now] == '+' or s[now] == '-':
                if E_was==0:
                    err =1
                    break
                elif num[len(num)-1] not in ['E', 'e']:
                    err=1
                    break
                else:
                    num+=s[now]
                    sim_was = 1
                    if now<len(s)-1:
                        now+=1
                    continue
            else:
                if s[now].isalpha():
                    err =1
                    break
                else:
                    num+=s[now]
                if now<len(s)-1:
                    now+=1
                else:
                    break 
        if err ==0:
            b = {'numbers': num}
            TokenList.append(b)
            CS = 'H'
            if now==len(s)-1:
                break
            continue
        else:
            error_sim = s[now]
            if now<len(s):
                now+=1
            CS = 'ERR'
            continue

#if errors is False:
#    for i in range(len(TokenList)):
#        print(TokenList[i])
    #print ("строк в коде: ", strk)
#TokenList.pop(len(TokenList)-1)
#СРАНЫЙ СИНТАКСИС
op_op=0
def error():
    global lex
    print('ERROR', TokenList[lex], "элемент №", lex)
    EXIT()
LexTablet=[]
for lex in TokenList:
    temp = list(lex.keys())
    LexTablet.append(temp)
LexTablet1 =[]
for x in range(len(LexTablet)):
    LexTablet1.append(LexTablet[x][0])

lex = 0
opop=0
rat =0
def set_opop():
    global opop
    
    opop+=1

def get_opop():
    global opop
    return opop
def get_lex():
    global lex

    lex+=1




def mog():
    global rat
    if LexTablet1[lex] in ['variable', 'numbers', 'TRUE', 'negative', 'open_mark', 'SUM','MUL']:
        if LexTablet1[lex] is 'open_mark':
            get_lex()
            EXMPL()
            get_lex()
            if LexTablet1[lex] is 'close_mark':
                get_lex()    
                return 0
        else:
            get_lex()
            if LexTablet1[lex] == 'ratio':
                rat+=1
                return 0
            elif LexTablet1[lex] == 'SUM':
                oper()
                return 0
            elif LexTablet1[lex] == 'MUL':
                slog()
                return 0
            else: 
                
                return 0
def slog():
    global rat
    mog()
    if rat ==1:
        return 0
    get_lex()
    if LexTablet1[lex] is 'MUL':
        get_lex()
        mog()
    elif LexTablet1[lex] is 'ratio':
        rat+=1
        return rat
    else: error()
def oper():
    global rat
    slog()
    if rat == 1:
        return 0
    get_lex()
    if LexTablet1[lex] is 'SUM':
        get_lex()
        slog()
    elif LexTablet1[lex] is 'ratio':
        rat+=1
        return 0
    else: error()
def EXMPL():
    global rat
    if rat == 0:
        oper()
        if rat == 1:
            get_lex()
            oper()
            rat =0
        else:
            get_lex()
            if LexTablet1[lex] == 'ratio':
                get_lex()
                oper()
    else:
        error()
    


def start():
    if LexTablet1[lex] == 'STRUCT_PROG':
        get_lex()
        VAR()
    else:
        error()
def VAR():
    if LexTablet1[lex] == 'var':
        get_lex()
        TIPE()
    else:
        error()
def TIPE():
    if LexTablet1[lex] == 'DATA_TIPE':
        get_lex()
        VALT()
    else:
        error()
def VALT():
    if LexTablet1[lex] == 'variable':
        get_lex()
        if LexTablet1[lex] == 'RAZD':
            get_lex()
            TIPE()
        elif LexTablet1[lex] == 'OP_START':
            get_lex()
            OP_START()
        else:
            error()
    else:
        error()
def comm():
    get_lex()
def end():
    
    global opop
    global lex
    
    if get_opop()==1:
        opop-=1
        print("ok!")
        EXIT()
    elif get_opop()>1:
        
        opop-=1
        get_lex()
        if LexTablet1[lex] in ['OP_START', 'OP_END', 'variable', 'COND', 'FOR', 'WHILE', 'READLN', 'WRITELN']:
            s()
    elif get_opop()<=0:
        error()
def OP_START(): 
    global lex
    global opop
    set_opop()
    
    if LexTablet1[lex] == 'COMM':
        comm()
    if LexTablet1[lex] in ['OP_START', 'OP_END', 'variable', 'COND', 'FOR', 'WHILE', 'READLN', 'WRITELN']:
        if LexTablet1[lex] == 'OP_START':
            get_lex()
            OP_START()  
        elif LexTablet1[lex] == 'OP_END':
            end()
            get_lex()
            if LexTablet1[lex] == 'OP_START':
                OP_START()
            elif LexTablet1[lex] == 'OP_END':
                end()
        elif LexTablet1[lex] in ['variable', 'COND', 'FOR', 'WHILE', 'READLN', 'WRITELN']:
            s()
        else:
            error()
def s():
    global lex
    if LexTablet1[lex] == 'variable':
        variable()
    elif LexTablet1[lex] == 'OP_START':
        get_lex()
        OP_START()
        
    elif LexTablet1[lex] == 'OP_END':
        end()
    elif LexTablet1[lex] == 'COND':
        COND()
    elif LexTablet1[lex] == 'FOR':
        FOR()
    elif LexTablet1[lex] == 'WHILE':
        WHILE()
    elif LexTablet1[lex] == 'READLN':
        READLN()
    else:
        WRITELN()
def WRITELN():
    get_lex()
    EXMPL()
def READLN():
    global lex
    get_lex()
    if LexTablet1[lex] != 'variable':
        error()
    get_lex()
    s()
def WHILE():
    global lex
    get_lex()
    if LexTablet1[lex] == 'open_mark':
        get_lex()
        EXMPL()
        get_lex()
        if LexTablet1[lex] == 'close_mark':
            OP_START()
        else:
            error()
    else: 
        error()
    get_lex()
    s()
def FOR():
    global lex
    get_lex()
    if LexTablet1[lex] == 'variable':
        get_lex()
        if LexTablet1[lex] == 'assignment':
            get_lex()
            EXMPL()
        get_lex()
        if LexTablet1[lex] == 'TO':
            get_lex()
            EXMPL()
            get_lex()
            if LexTablet1[lex] == 'STEP':
                EXMPL()
            OP_START()
            get_lex()
            if LexTablet1[lex] != 'NEXT':
                error()
    get_lex()
    s()
def COND():
    global lex
    get_lex()
    if LexTablet1[lex] == 'open_mark':

        get_lex()

        EXMPL()
        
        if LexTablet1[lex] == 'close_mark':
            get_lex()
            if LexTablet1[lex] != 'OP_START':
                error()
            else:
                s()
            
            if LexTablet1[lex] == 'ELSE':
                get_lex()
                s()
            else:

                error()
        else:

            error()
        get_lex()
        s()
def variable():
    global lex
    get_lex()
    if LexTablet1[lex] == 'assignment':
        get_lex()
        if LexTablet1[lex] in ['variable', 'numbers', 'TRUE'] and LexTablet1[lex+1] is 'variable':
            get_lex()
            s()
        
    else: 
        error()
    get_lex()
    s()
def EXIT():
    exit(0)
start()