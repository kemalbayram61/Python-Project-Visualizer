import description_objects
import parse_objects
import description_objects
"""
summary
- relationships are standardized as follows
relation = {source: "source_id", destination: "destination_id", relationship_type: "relationship_type"}

- nodes are standardized as follows
node = {id:"id","Name: "name" type: "type", references: "imported modules names" "}

created: 27.05.2020 by kemalbayramag@gmail.com
"""

class CreateNetwork:
    nodes = []
    edges = []
    objects = []
    project_name = ""
    
    def __init__(self,project):
        self.project = project
        self.project_name = project.getName()
        
    def determiningNodesByModules(self):
        self.nodes = []
        modules = self.project.getModules()
        node ={"id": 1,"name": "module_name", "type": "module_type","references": "imported modules names"}
        idCounter = 0
        for mdl in modules:
            module = mdl.getModule()
            node["id"] = idCounter
            node["name"] = module.getName()
            node["type"] = "module"
            node["references"] = module.getImportedModules()
            self.nodes.append(node)
            idCounter = idCounter + 1

    def determiningNodesByClass(self):
        self.nodes =[]
        modules = self.project.getModules()
        node = {"id": 1, "name": "module_name", "type": "module_type", "references": "imported modules names"}
        idCounter = 0
        modulClasses = []
        modulReferences = []
        referenceNames = []

        for mdl in modules:
            module = mdl.getModule()
            modulClasses = module.getClasses()

            for cls in modulClasses:
                node["id"] = idCounter
                node["name"] = cls.getName()
                node["type"] = "class"
                node["references"] = cls.getImportedModules()
                self.nodes.append(node)
                idCounter = idCounter + 1

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges

dize ="""
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
            jsonDefinition+=self.name+"{"
        else:
            jsonDefinition+="main{"
        
        jsonDefinition+="functions{"
        if(len(self.functions)>0):
            for i in range(len(self.functions)-1):
                jsonDefinition+=self.functions[i].getJson()+","
            jsonDefinition+=str(self.functions[len(self.functions)-1])+"}"
        else:
            jsonDefinition+="},"
        jsonDefinition+="body{"+self.body.getJson()+"}"
        
        return jsonDefinition

    def getImportedModules(self):
        return self.importedModules
        
class Classes2:
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
            jsonDefinition+=self.name+"{"
        else:
            jsonDefinition+="main{"
        
        jsonDefinition+="functions{"
        if(len(self.functions)>0):
            for i in range(len(self.functions)-1):
                jsonDefinition+=self.functions[i].getJson()+","
            jsonDefinition+=str(self.functions[len(self.functions)-1])+"}"
        else:
            jsonDefinition+="},"
        jsonDefinition+="body{"+self.body.getJson()+""
        
        return jsonDefinition

    def getImportedModules(self):
        return self.importedModules
"""

project = parse_objects.ParseProject("proje1")
project.addModul("modules1",dize)
project = project.getProject()

network = CreateNetwork(project)
network.determiningNodesByClass()
nodes = network.getNodes()
for node in nodes:
    print(node)


        

