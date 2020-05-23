class Variables:
    name=None
    variable_type=None
    variable_value=None
    def __init__(self,name,variable_type,variable_value):
        self.name=name
        self.variable_value=variable_value
        self.variable_type=variable_type
        
    def getName(self):
        return self.name
    
    def getVariableType(self):
        return self.variable_type
    
    def getVariableValue(self):
        return self.variable_value
    def getJson(self):
        jsonDefinition=str(self.name)+"{ value:"+str(self.variable_value)+", type:"+str(self.variable_type)+"}"
        return jsonDefinition

class Bodies:
    variables=None
    body=None
    def __init__(self,variables,body):
        self.body=body
        self.variables=variables
        
    def getVariables(self):
        return self.variables
    
    def getBody(self):
        return self.body
    def getJson(self):
        jsonDefinition=""
        jsonDefinition+=" variables{"
        if(len(self.variables)>0):
            for i in range(len(self.variables)-1):
                jsonDefinition+=self.variables[i].getJson()+","
            jsonDefinition+=self.variables[len(self.variables)-1].getJson()+"}"
        else:
            jsonDefinition+="}"
        return jsonDefinition
    
class Functions:
    name=None
    return_parameters=None
    parameters=None
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
    
    def getJson(self):
        jsonDefinition=""
        jsonDefinition+=self.name+"{ parameters:"+self.parameters+","+" return_parameters:"+self.return_parameters+","+" body{"+self.body.getJson()+"}}"
        return jsonDefinition

class Classes:
    functions=None
    body=None
    def __init__(self,functions,body):
        self.functions=functions
        self.body=body
        
    def getFunctions(self):
        return self.functions
    
    def getBody(self):
        return self.body
    
class Modules:
    classes=None
    functions=None
    body=None
    def __init__(self,classes,functions,body):
        self.classes=classes
        self.functions=functions
        self.body=body
        
    def getClasses(self):
        return self.classes
    
    def getFunctions(self):
        return self.functions
    
    def getBody(self):
        return self.body
    
class Projects:
    modules=None
    def __init__(self,modules):
        self.modules=modules
        
    def getModules(self):
        return self.modules