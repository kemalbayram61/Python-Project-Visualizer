class ImportedObjects:
    #definitions
    name = ""           #module name, class name or function name -->import module_name
    alias =""           #object alias name --> import modul_name as mdl
    module_name = ""    #object module name --> import modul_name
    #functions
    # Constructive function of Classes class
    def __init__(self,name,alias,module_name):
        self.name = name
        self.alias = alias

class Functions:
    #definitions
    _name = ""

    #functions
    # Constructive function of Functions class
    def __init__(self,name):
        self.name = name

    #getter functions
    def getName(self):
        return self.name

class Classes:
    #definitions
    _name = ""
    _function_names = []    #_function_names = ['f1_name','f2_name',...]

    #objects
    _function_objects = []  #_functions_objects = [<Functions>,<Functions>,...]

    #functions
    # Constructive function of Classes class
    def __init__(self,name,functions_names):
        self._name =name
        self._function_names = functions_names

        #run setter functions
        self.__setFunctions()

    def __setFunctions(self):
        for func in self._function_names:
            self._function_objects.append(Functions(func))

    def getFunctionsObjects(self):
        return self._function_objects

    def getName(self):
        return self._name

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

    #setter functions
    def __setClasses(self):
        for cls in self._classes:
            self._classes_objects.append(Classes(cls['name'],cls['functions']))

    def __setFunctions(self):
        for func in self._functions_names:
            self._functions_objects.append(Functions(func))

    def __setImportedObjects(self):
        for imp in self._imported_objects_names:
            self._imported_objects_objects.append(ImportedObjects(imp['name'],imp["alias"],imp["module_name"]))

    #getter functions
    def getName(self):
        return self._name

    def getFunctionsObject(self):
        return self._functions_objects

    def getClassesObject(self):
        return self._classes_objects

    def getImportedObjects(self):
        return self._imported_objects_objects

class Project:
    #definitions
    _name = ""
    _modules_object =[]

    # Constructive function of Project class
    def __init__(self,name):
        self._name = name

    #Create Read Update and Delete operations
    def addModule(self,module_object):
        self._modules_object.append(module_object)

    def getModule(self,module_name):
        for mdl in self._modules_object:
            if(mdl.getname()==module_name):
                return mdl

    def updateModule(self,module_name,new_version):
        temp =[]
        for mdl in self._modules_object:
            if(mdl.getname()==module_name):
                temp.append(new_version)
            else:
                temp.append(mdl)

        self._modules_object =temp

    def deleteModule(self,module_name):
        temp =[]
        for mdl in self._modules_object:
            if(mdl.getname()!=module_name):
                temp.append(mdl)

        self._modules_object = temp

    #getter functions
    def getModuleObject(self):
        return self._modules_object

class Nodes:
    #definitions
    name = ""
    type = ""

    # Constructive function of Nodes class
    def __init__(self,name,type):
        self.name = name
        self.type = type

class Edges:
    #definitions
    source_object = ""
    definition_object =""

    # Constructive function of Edges class
    def __init__(self,source_object,definition_object):
        self.source_object =source_object
        self.definition_object =definition_object