import json

class RubricaError (BaseException):...

class Rubrica:
    def __init__ ( self ):
        self._rubrica = None
    
    @staticmethod
    def __Error ( condizione:bool, code:str ):
        if ( not condizione ):
            return
        '''In an error occured this function is called and will throw'''
        print ( '-'*(len(code)+26))
        print ( f"-- the error '{code}' occured --")
        print ( '-'*(len(code)+26))
        raise RubricaError
    
    def APRI ( self, nome_file, is_json = True ):
        with open ( nome_file, 'r' ) as in_file:
            if ( is_json ):
                self._rubrica = json.load ( in_file )
                print ( 'the library is doing the job' )
                return 0
            
            contacts = in_file.read ( ).split ('\n')
            self._rubrica = {}
            for contact in contacts:
                data = contact.split ( ', ' )
                if ( len(data) != 7 ):
                    continue
                ## given that the data is well formed
                print ( 'loading contact: ', data )
                self._rubrica [ data[0] ] = {
                    'giorno': int(data[1]),
                    'mese': data[2],
                    'anno': int(data[3]),
                    'età': int(data[4]),
                    'sesso': data[5],
                    'mail': data[6]
                }
        print ( 'Aperto tutto' )


    @classmethod
    def APRI_JSON ( cls, nome_file ):
        '''Carica il file selezionato in memoria, se is_json == true lo carica come se fosse un file json se no come se fosse un file di testo.
    Se viene richiamata dopo l'inizializzazione proverà ad estendere la rubrica'''

        classe_formata = cls ( )
        classe_formata.APRI ( nome_file )
        return classe_formata


    @classmethod
    def APRI_CSV ( cls, nome_file ):
        classe_formata = cls ( )
        classe_formata.APRI ( nome_file, False )
        return classe_formata

    
    def AGGIUNGI (self, data:list ):
        '''Aggiunge l\'elemento contatto alla lista dei contatti caricati e deve essere della forma contatto = [str,int,str,int,int,char,str]'''

        self.__Error ( self._rubrica == None, "La rubrica non è caricata" )
        self._rubrica [ data[0] ] = {
            'giorno': data[1],
            'mese': data[2],
            'anno': data[3],
            'età': data[4],
            'sesso': data[5],
            'mail': data[6]
        }
        print (f'{data[0]}? Certo che l{'a' if data[5] == 'F' else 'o'} conosco l{'a' if data[5] == 'F' else 'o'} puoi trovare a 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104')


    def RIMUOVI ( self, nome:str ):
        '''Prova a rimuovere l'elemento con il nome nome'''
        self.__Error ( self._rubrica == None, "La rubrica non è caricata" ) 
        self.__Error ( len ( self._rubrica ) == 0, "La rubrica è vuota" )
        self.__Error ( not nome in self._rubrica, f"La rubrica non contine l'elemento {nome}" )
        
        del self._rubrica [ nome ]
        print ( f'Ho eliminato {nome}, non serve che mi ringrazzi')


    def SALVA ( self, file:str, is_json:bool = True ):
        '''scrive la rubrica nel file selezionato, se is_json è true utilizza il formato json se no utiliza il csv'''
        self.__Error ( self._rubrica == None, "La rubrica non è caricata" )
        self.__Error ( len ( self._rubrica ) == 0, "La rubrica è vuota" )

        with open ( file, 'w' ) as out_file:
            if is_json:
                json.dump ( self._rubrica, out_file, indent = 4 )
                return
            for nome in self._rubrica:
                out_file.write ( nome )
                for att in self._rubrica[nome]:
                    out_file.write ( f', {self._rubrica[nome][att]}' )
                out_file.write ( '\n' )
        print ( f"Salvato correttamente '{file}' in formato {'json' if is_json else 'csv'}" )


    def STAMPA ( self, nome:str ):
        '''Prova a stamapre le informazioni della persona nome'''
        self.__Error ( self._rubrica == None, "La rubrica non è caricata" ) 
        self.__Error ( len ( self._rubrica ) == 0, "La rubrica è vuota" )
        self.__Error ( not nome in self._rubrica, f"La rubrica non contine l'elemento {nome}" )
        
        r = self._rubrica[nome]
        print ( f'''Car{'a' if r['sesso'] == 'F' else 'o'} {nome},
sei nat{'a' if r['sesso'] == 'F' else 'o'} il {r['giorno']} di {r['mese']} del {r['anno']} e quindi a breve compirai {r['età']+1} anni.
Ti manderemo gli auguri a {r['mail']}''' )

