import re 


if __name__ == '__main__':
    txt = [['los pinos (lopresti)', 'acacia'], ['arabia', 'acacia dealbata']]

    lista = ['vivero arabia', 'acacia dealbata']
    print(re.findall(str(txt), str(lista)))
