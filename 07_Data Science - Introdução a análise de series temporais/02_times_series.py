import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

alucar = pd.read_csv('data\\alucar.csv',sep=',')

# Convertendo a coluna mês para datetime
alucar['mes'] = pd.to_datetime(alucar['mes'])
print(alucar.dtypes)

# Utilizamos o metodo diff para subtrair o dados do mes seguinte pelo mes anterior, assim teremos a diferença
alucar['aumento'] = alucar['vendas'].diff()
print(alucar.head())

# Utilizamos o metodo diff para subtrair o dados do mes seguinte pelo mes anterior, assim teremos a diferença
alucar['aceleracao'] = alucar['aumento'].diff()
print(alucar.head())

# Criando uma função para realizar o plot do gráfico
def plotar(titulo,labelx, labely,x,y,dataset):
    sns.set_palette('Accent')                   
    sns.set_style('darkgrid')           
    ax = sns.lineplot(x=x,y=y,data=dataset)
    ax.figure.set_size_inches(12,6)             
    ax.set_title(titulo, loc='left', fontsize=18)
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_ylabel(labely, fontsize=14)   
    plt.show()

# Criando uma função para realizar o plot dos 3 gráficos
def plot_comparacao(x,y1,y2,y3,dataset,titulo):
    plt.figure(figsize=(16,12))
    ax = plt.subplot(3,1,1)
    ax.set_title(titulo, fontsize=18, loc='left')
    sns.lineplot(x=x,y=y1,data=dataset)
    plt.subplot(3,1,2)
    sns.lineplot(x=x,y=y2,data=dataset)
    plt.subplot(3,1,3)
    sns.lineplot(x=x,y=y3,data=dataset)
    plt.show()


''' Autocorrelação '''
# Autocorrelação é uma medida de correlação entre observações de uma serie temporal
# Nível de correlação: máx 1 / min -1
from pandas.plotting import autocorrelation_plot

# Criando uma analise de correlação das vendas
''' Podemos verificar que os 7 primeiros dias tem uma correlação muito forte com a semana passada, tendo uma correlação alta nesse periodo
Com o passar do tempo essa correlação cai '''
# Correlação das vendas
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação das Vendas', fontsize=18, x=0.25, y=0.95)
autocorrelation_plot(alucar['vendas'])
plt.show()

# Correlação do aumento
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação do Aumento', fontsize=18, x=0.25, y=0.95)
autocorrelation_plot(alucar['aumento'][1:])
plt.show()

# Correlação da aceleração
ax = plt.figure(figsize=(12,6))
ax.suptitle('Correlação da Aceleração', fontsize=18, x=0.25, y=0.95)
autocorrelation_plot(alucar['aceleracao'][2:])
plt.show()