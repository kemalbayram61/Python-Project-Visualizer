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
    edges=[]
    objects=[]
    project_name=""
    
    def __init__(self,project):
        self.project=project
        
    def determiningNodes(self):
        self.project_name=self.project.getName()
        modules=self.project.getModules()
        print(modules[0].getModule().getJson())
        moduleNames=[]
        classesNames=[]


            

dize="""
    name=None
    functions=[]
    body=None
    classString=""
    def __init__(self,classString):
        self.classString=classString
        self.setParameters()
        
    def __init__(self,classString):
        self.classString=classString
        self.setParameters()
class ParseClasses:
    name=None
    functions=[]
    body=None
    classString=""
    def __init__(self,classString):
        self.classString=classString
        self.setParameters()
        
class ParseClasses:
    name=None
    functions=[]
    body=None
    classString=""
    def __init__(self,classString):
        self.classString=classString
        self.setParameters()
"""

a = parse_objects.ParseModules("firstExam",dize).getModule()
b = a.getBody().getFunctions()[0]
print(b.getName())


