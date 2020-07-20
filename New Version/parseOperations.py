import  objectDefinition
class ParseModules:
    #definition
    _name = ""
    _classes = []               #_classes_names = [{'name':'c1_name','functions':[c1_functions_names]},...]
    _functions_names = []       #_function_objects = ['f1_name','f2_name',...]
    _imported_objects_names = []#_function_objects = [{'module_name':'module_name','name':'obj_name','alias':'obj_alias'},...]
    _module_lines = []

    # Constructive function of ParseModules class
    def __init__(self,name,module_string):
        self._module_lines =module_string.splitlines()
        self._name =name
        self._classes = []
        self._functions_names = []
        self._imported_objects_names = []

        #run start functions
        self.__removeLineSpacing()
        self.__setImportedObjectName()
        self.__setClasses()

    #getter functions
    def getClasses(self):
        return self._classes

    def getImportedObjects(self):
        return self._imported_objects_names

    def getFunctions(self):
        return self._functions_names

    def getModuleObject(self):
        return objectDefinition.Modules(self._name,self._classes,self._functions_names,self._imported_objects_names)

    def __isSpaceLine(self,line):
        for alpha in line:
            if(alpha != " "):
                return False
        return True

    def __removeLineSpacing(self):
        temp =[]
        for line in self._module_lines:
            if(not(self.__isSpaceLine(line))):
                temp.append(line)
        self._module_lines = temp

    def __setImportedObjectName(self):
        obj = {'name': 'object_name', 'alias': 'object_alias', 'module_name': 'object_module_name'}
        for line in self._module_lines:
            temp = line.split()
            if("from"+" " in line):
                if("as"+" " in line):
                    obj['name'] = temp[3]
                    obj['alias'] = temp[5]
                    obj['module_name'] = temp[1]
                else:
                    obj['name'] = temp[3]
                    obj['module_name'] = temp[1]
                self._imported_objects_names.append(obj)

            elif("import"+" " in line):
                if("as"+" " in line):
                    obj['name'] = temp[1]
                    obj['alias'] = temp[3]
                else:
                    obj['name'] = temp[1]
                self._imported_objects_names.append(obj)

    def __getIndent(self,line):
        counter=0
        for alpha in line:
            if(alpha!=" "):
                return counter
            counter = counter + 1
        return counter

    def __setClasses(self):
        obj = {'name':'class_name','functions':['f1_name','f2_name']}
        module_body = []
        i = 0 
        while(i<len(self._module_lines)):
            if("class"+" " in self._module_lines[i]):
                class_body = []
                indent = self.__getIndent(self._module_lines[i])
                obj['name'] = self._module_lines[i].split(':')[0].split()[-1]       #class_class_name: #description -->class_name
                i=i+1
                new_indent =self.__getIndent(self._module_lines[i])
                while(new_indent>indent and i<len(self._module_lines)-1):
                    class_body.append(self._module_lines[i])
                    i = i + 1
                    new_indent = self.__getIndent(self._module_lines[i])

                obj['functions'] = self.__getFunctions(class_body)
                self._classes.append(obj)
                obj = {}

            if(i<len(self._module_lines)):
                module_body.append(self._module_lines[i])
            i = i+1
        self._functions_names = self.__getFunctions(module_body)

    def __getFunctions(self,lines):
        functions_names = []
        for line in lines:
            if("def"+" " in line):
                functions_names.append(line.split(':')[0].split('(')[0].split()[-1])    #def_f_name(...): #description -->f_name
        return functions_names