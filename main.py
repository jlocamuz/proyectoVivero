import pandas as pd
from regex import D

def read_excel():
    xls = pd.ExcelFile('comparativo.xlsx')
    df1 = pd.read_excel(xls, 'Hoja1')
    df2 = pd.read_excel(xls, 'Hoja2')

    df1_v = df1['Vivero']
    lista_viveros = list(set(df1_v.tolist()))
    df = pd.DataFrame(lista_viveros, columns=["vivero"])
    
    #df_styled = df.style.apply(lambda x: ['background-color:red' if x == 'VIVERO ARABIA' else 'background-color:green' for x in df.vivero])
    #df_styled.to_excel('lista_viveros_style.xlsx', engine='openpyxl', index=False)
    df1_v_e = df1[['Vivero', 'Especie']]
    lista_vivero_especie_1 = df1_v_e.values.tolist()
    df2_v_e = df2[['Vivero', 'Especie']]
    lista_vivero_especie_2 = df2_v_e.values.tolist()

    print(len(lista_vivero_especie_1))
    print(len(lista_vivero_especie_2))

    for x in lista_vivero_especie_1: 
        if x in lista_vivero_especie_2:
            print(x)
        else:
            print("no")


    df_mask=df1_v_e['Vivero']=='VIVERO ARABIA'
    filtered_df = df1_v_e[df_mask]
    #print(filtered_df)





if __name__ == '__main__':
    read_excel()