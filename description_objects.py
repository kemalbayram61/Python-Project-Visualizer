import json
"""
summary
is the module that contains all the objects that can be found in a project 
and these objects are converted to json format

created: 23.05.2020 by kemalbayramag@gmail.com
"""

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
        #jsonDefinition=str(self.name)+"{\n\t value:"+str(self.variable_value)+",\n\t type:"+str(self.variable_type)+"}\n"
        jsonDefinition=json.dumps(self.__dict__)
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
        jsonDefinition+=" variables{\n\t"
        if(len(self.variables)>0):
            for i in range(len(self.variables)-1):
                jsonDefinition+=self.variables[i].getJson()+",\n\t"
            jsonDefinition+=self.variables[len(self.variables)-1].getJson()+"}\n"
        else:
            jsonDefinition+="}\n"
        
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
        jsonDefinition+="name:"+self.name+",\n\t parameters:"+self.parameters+",\n\t"+" return_parameters:"+self.return_parameters+",\n\t"+"\n body{"+self.body.getJson()+"}\n"
        return jsonDefinition

class Classes:
    functions=[]
    body=None
    name=None
    importedModules = []

    def __init__(self,name,functions,body,importedModules):
        self.name = name
        self.functions=functions
        self.body=body
        self.importedModules = importedModules
        
    def getFunctions(self):
        return self.functions
    
    def getBody(self):
        return self.body
    
    def getJson(self):
        jsonDefinition=""
        if(self.name!=None):
            jsonDefinition+=self.name+"{\n\t"
        else:
            jsonDefinition+="main{\n\t"
        
        jsonDefinition+="functions{\n\t"
        if(len(self.functions)>0):
            for i in range(len(self.functions)-1):
                jsonDefinition+=self.functions[i].getJson()+",\n\t"
            jsonDefinition+=str(self.functions[len(self.functions)-1])+"}\n\t"
        else:
            jsonDefinition+="},\n\t"
        jsonDefinition+="body{\n\t"+self.body.getJson()+"}\n\t"
        
        return jsonDefinition

    def getImportedModules(self):
        return self.importedModules

    def getName(self):
        return self.name
    
class Modules:#the bodies of the modules are class type data
    classes=[]
    body=None
    name=None
    impoted_modules=[]
    
    def __init__(self,name,classes,body,imported_Modules):
        self.classes=classes
        self.body=body
        self.name=name
        self.impoted_modules = imported_Modules
        
    def getClasses(self):
        return self.classes
    
    def getBody(self):#class type body
        return self.body
    
    def getName(self):
        return self.name
    
    def getJson(self):
        jsonDefinition=""
        for clas in self.classes:
            jsonDefinition+=clas.getJson()+","
        jsonDefinition+=self.body.getJson()

        return jsonDefinition

    def getImportedModules(self):
        return self.impoted_modules
    
class Project:
    modules=[]
    name=""
    def __init__(self,name,modules):
        self.modules=modules
        self.name=name
        
    def getModules(self):
        return self.modules
    
    def getName(self):
        return self.name