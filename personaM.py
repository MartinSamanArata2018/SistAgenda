class PersonaM():

    def __init__(self):
        self.__nomper=""
        self.__apeper=""
        self.__dniper=""
        self.__emailper=""

    def setNomPer(self, nomper):
        self.__nomper = nomper

    def getNomPer(self):
        return self.__nomper

    def setApePer(self, apeper):
        self.__apeper = apeper
    
    def getApePer(self):
        return self.__apeper

    def setDniPer(self, dniper):
        self.__dniper = dniper   
    
    def getDniPer(self):
        return self.__dniper
    
    def setEmailPer(self, email):
        self.__emailper = email
    
    def getEmailPer(self):
        return self.__emailper