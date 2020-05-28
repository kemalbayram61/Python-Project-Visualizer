import description_objects
import parse_objects
import description_objects
"""
summary
- relationships are standardized as follows
relation = {source: "source_id", destination: "destination_id", relationship_type: "relationship_type"}

- nodes are standardized as follows
node = {id:"id","Name: "name" type "type", "value" value "}

created: 27.05.2020 by kemalbayramag@gmail.com
"""

class CreateNetwork:
    nodes=[]
    relationships=[]
    objects=[]
    
    def __init__(self,project):
        self.project=project
        
    def determiningNodes(self):
        package_name=self.project.getName()


            

dize="""
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
"""

project=parse_objects.ParseProject("proje1")
project.addModul("modul1",dize)
prj_obj=project.getProjec()

network=CreateNetwork(prj_obj)
network.determiningNodes()