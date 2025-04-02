class Paciente :
    def __init__ (self, nome, idade, temperatura , sintomas) :
        self.nome = nome
        self.idade = idade
        self.temperatura = temperatura
        self.sintomas = sintomas if isinstance(sintomas, list) else []

        if temperatura == 39 or (temperatura > 39):
            self.sintomas.append("febre alta")
        elif 37.5 <= temperatura < 38:
            self.sintomas.append("Estado febril.")
        elif 38 <= temperatura < 39:
            self.sintomas.append("febre.")
        else: 
            self.sintomas.append("Temperatura normal")

        self.regras = {
        "Gripe": ["febre", "tosse", "dor de garganta", "fadiga", "calafrios"],
        "Resfriado": ["espirros", "coriza", "dor de garganta", "tosse leve"],
        "Dengue": ["febre alta", "dor muscular", "dor atrás dos olhos", "manchas vermelhas"],
        "Covid-19": ["febre", "tosse seca", "falta de ar", "perda de olfato", "fadiga"],
        "Sinusite": ["dor facial", "congestão nasal", "dor de cabeça", "secreção nasal amarelada"],
        "Infecção de Garganta": ["dor de garganta", "vermelhidão na garganta", "tosse leve", "febre baixa", "rouquidão", "linfonodos inchados", "coriza"],
        "Amigdalite": ["dor intensa na garganta", "dificuldade para engolir", "amígdalas inchadas", "placas brancas ou pus nas amígdalas", "mau hálito", "febre alta", "dor de cabeça", "rouquidão"]
        }
    
    def exibirProntuario (self) :
        sintomas_str = ", ".join(self.sintomas) if self.sintomas else "Nenhum"
        print(f"Paciente: {self.nome} de {self.idade} de idade, apresenta: {sintomas_str}")

    def diagnosticar (self) :
        if not self.sintomas :
            print("\nNenhum sintoma informado. Diagnóstico não pode ser realizado.")
            return
        
        pontuacao = {
            diagnostico: len(set(self.sintomas) & set(sintomas_doenca))
            for diagnostico, sintomas_doenca in self.regras.items()
        }
        
        diagnostico_provavel = max(pontuacao, key=pontuacao.get)

        print("\nCom base nos sintomas informados, o diagnóstico mais provável é:", diagnostico_provavel)

paciente = Paciente("Manuela", 22, 39, ["dor muscular", "dor atrás dos olhos", "manchas vermelhas"])
paciente.exibirProntuario()
paciente.diagnosticar()
paciente = Paciente("Carlos", 33, 38, ["tosse leve", "dor de garganta"])
paciente.exibirProntuario()
paciente.diagnosticar()
    

