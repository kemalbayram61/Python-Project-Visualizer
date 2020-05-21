class variable:
    name=""
    variable_type=""
    variable_value=None
    

class Body:
    variables=[]
    body=""
    def __init__(self,variables,body):
        self.body=body
        self.variables=variables
        
    def getVariables(self):
        return self.variables
    
    def getBody(self):
        return self.body
    
class Functions:
    name=""
    return_parameters=[]
    parameters=[]
    body=None
    def __init__(self,name,parameters,return_parameters,body):
        self.name=name
        self.parameters=parameters
        self.return_parameters=return_parameters
        self.body=body
        
    def getName(self):
        return self.name
    def getReturnParameters(self):
        return self.return_parameters
    def getParameters(self):
        return self.parameters
    def getBody(self):
        return self.body
        
    