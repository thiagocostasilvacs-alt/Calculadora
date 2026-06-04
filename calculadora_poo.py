import tkinter as tk

OPERADORES = ["+", "-", "*", "/"]

class Calculadora:
    
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")

        self.visor = tk.Entry(
            self.janela, 
            width=35, 
            state="readonly", 
            justify="right"
            )
        
        self.visor.grid(
            row=0, 
            column=0, 
            columnspan=4
            )
        
        self.criar_botoes()
        
        self.janela.mainloop()
        
    def inserir(self, numero):
        texto = self.visor.get()

        if numero in OPERADORES:
            if texto == "":
                return
            if texto[-1] in OPERADORES:
                return
        
        self.visor.config(state="normal")
        self.visor.insert(tk.END, numero)
        self.visor.config(state="readonly")

    def limpar(self):
        self.atualizar_visor("")

    def calcular(self):
        try:
            expressao = self.visor.get()
            resultado = eval(expressao)
            self.atualizar_visor(resultado)

        except Exception as erro:
            print(erro)
            self.atualizar_visor("Erro")

    def atualizar_visor(self, texto):
        self.visor.config(state="normal")
        self.visor.delete(0,tk.END)
        self.visor.insert(0, texto)
        self.visor.config(state="readonly")

    def criar_botoes(self):
        numeros = [7, 8, 9, 4, 5, 6, 1, 2, 3]

        linha = 1
        coluna = 0

        for numero in numeros:
            botao = tk.Button(self.janela, text=str(numero), width=5, height=2, command=lambda n=numero: self.inserir(str(n)))

            botao.grid(row=linha, column=coluna)

            if coluna < 2:
                coluna +=1
            else:
                coluna = 0
                linha +=1

        linha = 1
        coluna = 3

        for operador in OPERADORES:
            botao = tk.Button(self.janela, text=str(operador), width=5, height=2, command=lambda o=operador: self.inserir(str(o)))

            botao.grid(row=linha, column=coluna, padx=1, pady=1)

            linha +=1

        botao_0 = tk.Button(self.janela, text="0", width=5, height=2, command= lambda:self.inserir("0"))
        botao_0.grid(row=4, column=1)

        botao_C = tk.Button(self.janela, text="C", width=5, height=2, command=self.limpar)
        botao_C.grid(row=4, column=0)

        botao_igual = tk.Button(self.janela, text="=", width=5, height=2, command=self.calcular)
        botao_igual.grid(row=4, column=2)
        

if __name__ == "__main__":
    Calculadora()