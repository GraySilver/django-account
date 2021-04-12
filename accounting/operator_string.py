import re
import operator

opt_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


class OperatorString:

    def calu(self, _list, opt_list=['*', '/']):
        if len(set(_list) & set(opt_list)) == 0:
            return _list
        new_list = []
        for i, item in enumerate(_list):
            if item in opt_list:
                value = opt_dict[item](_list[i - 1], _list[i + 1])
                first = True
                for index, j in enumerate(_list):
                    if index in [i - 1, i + 1, i]:
                        if first:
                            new_list.append(value)
                            first = False
                    else:
                        new_list.append(j)
                return self.calu(new_list, opt_list=opt_list)

    def run(self, _string):
        string_list = re.split('(\+|-|\*|/)', _string)
        if len(string_list) == 1:
            result = float(string_list[-1])
            if result.is_integer():
                return int(result)
            else:
                return result
        else:
            string_list = [float(i) if i not in ['+', '-', '*', '/'] else i for i in string_list]
            if string_list[-1] == '':
                raise ValueError('最后末尾不能以符号结尾')
            string_list = self.calu(string_list, opt_list=['*', '/'])
            result = self.calu(string_list, opt_list=['+', '-'])[-1]
            if result.is_integer():
                return int(result)
            else:
                return result
