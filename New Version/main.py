from networkDefinition import ProjectNetwork
import parseOperations
import objectDefinition

module = """
class kkkkkkkkk:
    #definitions
    _name = ""
    _classes = []               #_classes_names = [{'name':'c1_name','functions':[c1_functions_names]},...]
    _functions_names = []       #_function_objects = ['f1_name','f2_name',...]
    _imported_objects_names = []#_function_objects = [{'name':'obj_name','alias':'obj_alias'},...]

    #objects
    _functions_objects = []     #_functions_objects = [<Functions>,<Functions>,...]
    _classes_objects = []       #_functions_objects = [<Classes>,<Classes>,...]
    _imported_objects_objects = []#_functions_objects = [<ImportedObjects>,<ImportedObjects>,...]

    #functions
    #Constructive function of Modules class
    def __init__(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

    def setmethod(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

def __init__(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

class sssssss:
    #definitions
    _name = ""
    _classes = []               #_classes_names = [{'name':'c1_name','functions':[c1_functions_names]},...]
    _functions_names = []       #_function_objects = ['f1_name','f2_name',...]
    _imported_objects_names = []#_function_objects = [{'name':'obj_name','alias':'obj_alias'},...]

    #objects
    _functions_objects = []     #_functions_objects = [<Functions>,<Functions>,...]
    _classes_objects = []       #_functions_objects = [<Classes>,<Classes>,...]
    _imported_objects_objects = []#_functions_objects = [<ImportedObjects>,<ImportedObjects>,...]

    #functions
    #Constructive function of Modules class
    def a(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

    def b(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

def kemal(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

"""

module2 = """
class Modules:
    #definitions
    _name = ""
    _classes = []               #_classes_names = [{'name':'c1_name','functions':[c1_functions_names]},...]
    _functions_names = []       #_function_objects = ['f1_name','f2_name',...]
    _imported_objects_names = []#_function_objects = [{'name':'obj_name','alias':'obj_alias'},...]

    #objects
    _functions_objects = []     #_functions_objects = [<Functions>,<Functions>,...]
    _classes_objects = []       #_functions_objects = [<Classes>,<Classes>,...]
    _imported_objects_objects = []#_functions_objects = [<ImportedObjects>,<ImportedObjects>,...]

    #functions
    #Constructive function of Modules class
    def __init__(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

    def setmethod(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

def __init__(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

class Modules2:
    #definitions
    _name = ""
    _classes = []               #_classes_names = [{'name':'c1_name','functions':[c1_functions_names]},...]
    _functions_names = []       #_function_objects = ['f1_name','f2_name',...]
    _imported_objects_names = []#_function_objects = [{'name':'obj_name','alias':'obj_alias'},...]

    #objects
    _functions_objects = []     #_functions_objects = [<Functions>,<Functions>,...]
    _classes_objects = []       #_functions_objects = [<Classes>,<Classes>,...]
    _imported_objects_objects = []#_functions_objects = [<ImportedObjects>,<ImportedObjects>,...]

    #functions
    #Constructive function of Modules class
    def a(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

    def b(self,name,classes,functions_names,imported_objects_names):
        self._name = name
        self._classes = classes
        self._functions_names = functions_names
        self._imported_objects_names = imported_objects_names

        # run setter functions
        self.__setClasses()
        self.__setFunctions()
        self.__setImportedObjects()

    def kemal(self,name,classes,functions_names,imported_objects_names):
            self._name = name
            self._classes = classes
            self._functions_names = functions_names
            self._imported_objects_names = imported_objects_names

            # run setter functions
            self.__setClasses()
            self.__setFunctions()
            self.__setImportedObjects()

"""


module3 ="""
class ProjectNetwork:
    _name = ""
    _nodes = []
    _edges = []
    _project = ""
    _net = Network("800px","1600px")

    def __init__(self,name,project):
        self._name = name
        self._project =project
        self.__setNetwork()
        self.__createNetwork()

    def __writeNodes(self):
        for node in self._nodes:
            print(node.name,end=" | ")

    #setter functions
    def __setNetwork(self):
        node = Nodes(self._project.getName(),len(self._nodes),"project","#EA5900",25,"icons\\project.png")
        self._nodes.append(node)                            #self._nodes = ["project_name-0-project"]
        self.__writeNodes()

        modules = self._project.getModuleObject()
        for module in modules:
            node = Nodes(module.getName(),len(self._nodes),"module","#79EA00",20,"icons\\module.png")
            self._nodes.append(node)                        #self._nodes = ["project_name-0-project","module_name1-1-module","module_name2-2-module"...]
            self.__writeNodes()
            edge = Edges(self._nodes[0].getString(),self._nodes[len(self._nodes)-1].getString())
            self._edges.append(edge)
        
        items_counter = 0
        last_items_counter = 0

        for i,module in enumerate(modules):
            last_items_counter = items_counter
            classes = module.getClassesObject()
            for clss in classes:
                node = Nodes(clss.getName(),len(self._nodes),"class","#00EACE",15,"icons\\class.png") 
                self._nodes.append(node)                    #self._nodes = ["project_name-0-project","module_name1-1-module","class_name1-2-class","class_name2-3-class",...]
                self.__writeNodes()
                edge = Edges(self._nodes[i+1].getString(),self._nodes[len(self._nodes)-1].getString())
                self._edges.append(edge)

            for j,clss in enumerate(classes):
                functions = clss.getFunctionsObjects()
                items_counter = items_counter + 1
                for func in functions:
                    node = Nodes(func.getName(),len(self._nodes),"class-function","#004AEA",10,"icons\\function.png")
                    self._nodes.append(node)                #self._nodes = ["project_name-0-project","module_name1-1-module","class_name1-2-class","func_name1-3-class-function","func_name2-4-class-function",...]
                    self.__writeNodes()
                    edge = Edges(self._nodes[len(modules) + 1 + j + last_items_counter].getString(),self._nodes[len(self._nodes)-1].getString())
                    self._edges.append(edge)
                    items_counter = items_counter + 1

            module_functions = module.getFunctionsObject()
            for func in module_functions:
                node = Nodes(func.getName(),len(self._nodes),"module-function","#EA00DF",10,"icons\\module_function.png")
                self._nodes.append(node)                    #self._nodes = ["project_name-0-project","module_name1-1-module","class_name1-2-class","func_name1-3-class-function","func_name1-4-module-function","func_name2-5-module-function",...]
                self.__writeNodes()
                edge = Edges(self._nodes[i+1].getString(),self._nodes[len(self._nodes)-1].getString())
                self._edges.append(edge)
                items_counter = items_counter + 1

    def __createNetwork(self):
        for node in self._nodes:
            self._net.add_node(node.getString(),label=node.name,color=node.node_color,size=node.node_size,shape='image',image = node.node_icon)

        for edge in self._edges:
            self._net.add_edge(edge.source_object,edge.definition_object)
        self._net.show("nx.html")
        

    def getNodes(self):
        return self._nodes

    def getEdges(self):
        return self._edges
"""

k= parseOperations.ParseModules('m1',module).getModuleObject()
a= parseOperations.ParseModules('m2',module2).getModuleObject()
f= parseOperations.ParseModules('m3',module3).getModuleObject()
b= objectDefinition.Project('p1')
b.addModule(a)
b.addModule(k)
b.addModule(f)
c= ProjectNetwork('n1',b)
