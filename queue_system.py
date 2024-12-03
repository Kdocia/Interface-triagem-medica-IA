from queue import Queue
import names

class CustomQueue:
    '''
    Classe responsável por gerenciar a fila de pacientes.
    '''

    def __init__(self):
        self.q_vermelho = Queue()
        self.q_laranja = Queue()
        self.q_amarelo = Queue()
        self.q_verde = Queue()
        self.q_azul = Queue()
        self.contador_vermelho = 0
        self.contador_laranja = 0
        self.contador_amarelo = 0
        self.contador_verde = 0
        self.contador_azul = 0

    def insert(self, user_name:str, user_urgency_code:int)->str:
        '''
        Insere um paciente na fila, fornecendo um número da sua posição relativa
        na fila.

        Args:
            user_name:str -> nome do paciente.
            
            user_urgency_code -> número inteiro correspondente ao nível de urgência
                                do paciente de acordo com o Protocolo Manchester.
                                Assume os valores:
                                - 4 -> Azul.
                                - 3 -> Verde.
                                - 2 -> Amarelo.
                                - 1 -> Laranja.
                                - 0 -> Vermelho.

        Returns:
            position_code:str -> string que indica qual o grau de urgeência do paciente
                                e sua posição na fila. Exemplo: AZ_18.

        '''
        match user_urgency_code:
            case 4:
                self.contador_azul += 1
                self.q_azul.put((user_name, f"AZ_{self.contador_azul}"))
                return f"AZ_{self.contador_azul}"
            case 3:

                self.contador_verde += 1
                self.q_verde.put((user_name, f"VD_{self.contador_verde}"))
                return f"VD_{self.contador_verde}"
            case 2:

                self.contador_amarelo += 1
                self.q_amarelo.put((user_name, f"AM_{self.contador_amarelo}"))
                return f"AM_{self.contador_amarelo}"
            case 1:

                self.contador_laranja += 1
                self.q_laranja.put((user_name, f"LA_{self.contador_laranja}"))
                return f"LA_{self.contador_laranja}"
            case 0:

                self.contador_vermelho += 1
                self.q_vermelho.put((user_name, f"VM_{self.contador_vermelho}"))
                return f"VM_{self.contador_vermelho}"
    
    def get_next_user(self) -> tuple[str, int]:
        '''
        Pega o próximo paciente da fila e o remove dela.

        Args:
            None

        Returns:
            tuple[user_name:str, position_code:int] -> tupla contendo o nome
                                                     do paciente e seu código
                                                     de posição na fila.
        '''
        if not self.q_vermelho.empty():
            return self.q_vermelho.get()
        
        elif not self.q_laranja.empty():
            return self.q_laranja.get()
        
        elif not self.q_amarelo.empty():
            return self.q_amarelo.get()
        
        elif not self.q_verde.empty():
            return self.q_verde.get()
        
        elif not self.q_azul.empty():
            return self.q_azul.get()
        
        else:
            raise Exception(
                "Não é possível retirar itens de uma fila vazia."
            )
        
    def is_not_empty(self) -> bool:
        '''
        Verifica se a fila de pacientes está vazia

        Args:
            None

        Returns:
            not_empty:bool -> True se a fila não estiver vazia.
                            False, caso contrário. 
        '''
        if not self.q_vermelho.empty() or\
           not self.q_laranja.empty() or\
           not self.q_amarelo.empty() or\
           not self.q_verde.empty() or\
           not self.q_azul.empty():
            return True
        else:
            return False

