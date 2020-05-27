import description_objects
import parse_objects
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
    
    def __init__(self,objects):
        self.objects=objects
        
    def determiningNodes(self):
        if(type(self.objects)==description_objects.Bodies):
            print("Input Body")
            
            
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


obj=parse_objects.ParseBodies(dize)
obj=obj.getBody()

a=CreateNetwork(obj).determiningNodes()