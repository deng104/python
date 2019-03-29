import re
def cal_atom(exp):  # '2/5'
    if '*' in exp:
        a,b = exp.split('*')
        return str(float(a)*float(b))
    if '/' in exp:
        a,b = exp.split('/')
        return str(float(a)/float(b))

def exp_format(exp):
    exp = exp.replace('--','+')
    exp = exp.replace('+-','-')
    exp = exp.replace('++','+')
    exp = exp.replace('-+','-')
    return exp

# 加减乘除
def inner_bracket(s):
    while True:
        parttern = r'\d+(\.\d+)?[*/]-?\d+(\.\d+)?'
        ret = re.search(parttern, s)
        if ret:
            exp = ret.group()
            res = cal_atom(exp)
            s = s.replace(exp, res)
        else:break
    s = exp_format(s)
    ret = re.findall('[-+]?\d+(?:\.\d+)?', s)
    count = 0
    for i in ret:
        count += float(i)
    return count

# 去除括号
def remove_bracket(s):
    while True:
        ret = re.search('\([^()]+\)',s)
        if ret:
            no_bracket = ret.group()
            res = inner_bracket(no_bracket)
            s = s.replace(no_bracket,str(res))
            s = exp_format(s)
        else:return s

def main(s):
    s = s.replace(' ', '')
    s = remove_bracket(s)
    return inner_bracket(s)

s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret = main(s)
print(ret)