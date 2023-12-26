import tkinter as tk
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")
        self.root.geometry("300x200")

        self.tempo = tk.StringVar()
        self.tempo.set("00:00:00")

        self.label_tempo = tk.Label(self.root, textvariable=self.tempo, font=("Arial", 30))
        self.label_tempo.pack(pady=10)

        self.entry_tempo = tk.Entry(self.root, font=("Arial", 12), width=10)
        self.entry_tempo.pack(pady=10)

        self.iniciado = False
        self.tempo_inicial = None

        #janela sempre ativa
        self.root.winfo_toplevel().attributes("-topmost", True)

        self.criar_botoes()

    def criar_botoes(self):
        btn_iniciar = tk.Button(self.root, text="Iniciar", command=self.iniciar_cronometro)
        btn_iniciar.pack()

        btn_parar = tk.Button(self.root, text="Parar", command=self.parar_cronometro)
        btn_parar.pack()

        btn_resetar = tk.Button(self.root, text="Resetar", command=self.resetar_cronometro)
        btn_resetar.pack()

        btn_sair = tk.Button(self.root, text="Sair", command=self.root.quit)
        btn_sair.pack()

    def iniciar_cronometro(self):
        if not self.iniciado:
            self.iniciado = True
            tempo_digitado = self.entry_tempo.get()
            tempo_segundos = self.converter_tempo_para_segundos(tempo_digitado)
            self.tempo_inicial = time.time() + tempo_segundos
            self.atualizar_cronometro()


    def parar_cronometro(self):
        if self.iniciado:
            self.iniciado = False

    def resetar_cronometro(self):
        self.iniciado = False
        self.tempo_inicial = None
        self.tempo.set("00:00:00")
        self.entry_tempo.delete(0, tk.END)

    def atualizar_cronometro(self):
        if self.iniciado:
            tempo_restante = self.tempo_inicial - time.time()
            if tempo_restante <= 0:
                self.tempo.set("00:00:00")
                self.iniciado = False
            else:
                horas = int(tempo_restante // 3600)
                minutos = int((tempo_restante % 3600) // 60)
                segundos = int(tempo_restante % 60)
                tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
                self.tempo.set(tempo_formatado)
                self.root.after(1000, self.atualizar_cronometro)

    def converter_tempo_para_segundos(self, tempo):
        try:
            horas, minutos, segundos = map(int, tempo.split(':'))
            return horas * 3600 + minutos * 60 + segundos
        except ValueError:
            return 0
    
def main():
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()

if __name__ == "__main__":
    main()
