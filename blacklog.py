class Filablacklog:
    def _init_(self):
        sef.dados = []
        
    def enqueue(self,jogo):
        self.dados.append(jogo)
        
    def denqueue(self):
        if self.is_empty():
            return None
        return self.dados.pop(0)
    
    def is_empty(self):
        return len (self.dados) == 0
    
    def mostrar (self):
        if self.is_empty():
            print ('Blacklog vazio')
            return
        print ('----- BLACKLOG-----')
        for index, jogo in enumerate(self.dados, start = 1):
            print(f'(index) - {jogo.exibir()}')
            
    def tamanho(self):
        return len(self.dados)
    
    