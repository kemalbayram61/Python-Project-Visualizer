import description_objects
"""
summary
The classes that will convert the input received as a string for all the 
objects in the definition module into that object are included in this module.

created: 24.05.2020 by kemalbayramag@gmail.com

"""

class ParseVariable:
    variable_string=None
    variable_name=None
    variable_value=None
    variable_type=None
    
    def __init__(self,variable_string):
        self.variable_string=variable_string
        self.parse()
        
    def getType(self,character):
        numbers=["1","2","3","4","5","6","7","8","9","0","-","+"]
        listCharacters=["{","[","("]
        if(character[0] in numbers):
            return "Numeric"
        elif(character[0] in listCharacters):
            return "List"
        else:
            return "Text"
    
    def parse(self):
        name=""
        value=""
        case=False
        
        for i in range(len(self.variable_string)):# a = 5
            if(self.variable_string[i]=="="):
                case=True
                continue
            
            if(case==False):
                name=name+self.variable_string[i]
                
            else:
                value=value+self.variable_string[i]

        name=name.strip() #deletes spaces if entry with spaces      
        value=value.strip() #deletes spaces if entry with spaces
                
        self.variable_name=name

        self.variable_value=value
        
        self.variable_type=self.getType(value)

    def getVariables(self):
        return description_objects.Variables(self.variable_name,self.variable_type,self.variable_value)

class ParseBodies:
    body_string = ""
    variables = []
    body = ""

    def  __init__(self,body_string):
        self.body_string = body_string
        self.parse()

    def isBadLine(self,line):
        keywords = ["def ","class ","for ","switch ","as ", "assert ",
                    "break ", "continue ", "del ", " elif", "else:",
                    "except ", "finally ", "from ", "global ",
                    "if(", "import ", " in ", " is ", "lambda ", " not",
                    " or ", "pass ", "return ", "try:", "except ",
                    "while(", " with ", " yield "]
        for word in keywords:
            if(word in line):
                return True
        return False

    def parse(self):
        body_lines = self.body_string.splitlines()
        for line in body_lines:
            if( not(self.isBadLine(line)) and ("=" in line) and line.strip()[0]!="#"):
                self.variables.append(ParseVariable(line).getVariables())
            else:
                self.body = self.body + line +"\n"

    def getBody(self):
        return description_objects.Bodies(self.variables,self.body)


class ParseFunctions:
    function_string = ""
    name = ""
    return_parameter = ""
    parameters = ""
    body = ""

    def __init__(self,function_string):
        self.function_string=function_string
        self.parse()

    def parse(self):
        split_lines = self.function_string.splitlines()
        for line in split_lines:
            if("def"+" " in line):
                temp = line.split()[1].strip()  #def getJson(self): --->  getJson(self):
                temp = temp.split("(")          #getJson(self): ----> getJson , self):
                self.name = temp[0]             #getJson(self): ----> getJson
                self.parameters = temp[1][:-2]  #self): ----> self

            elif("return " in line):
                temp = line.split()[1].strip()  #return jsonDefinition  ----> jsonDefinition
                self.return_parameter = temp

            else:
                self.body = self.body + line +"\n"

        self.body = ParseBodies(self.body).getBody()

    def getFunction(self):
        return  description_objects.Functions(self.name,self.parameters,self.return_parameter,self.body)

class ParseClasses:
    name=None
    functions=[]
    body=None
    classString=""
    importedModules = []
    modulReferences = []

    def __init__(self,classString,moduleReferences):
        self.classString=classString
        self.modulReferences = moduleReferences
        self.setParameters()
        
    def indent(self,string):
        indent=0

        while(indent<len(string) and not(string[indent].isalpha())):
            indent=indent+1
        return indent
                
    def setParameters(self):
        lines=self.classString.splitlines()
        indent=-1
        temp=""
        body_temp=""
        counter=0
        temp_functions=[]
        i=0

        while(i<len(lines)):
            if("class"+" " in lines[i]): #class ParseClasses: ---> ParseClasses
                self.name = lines[i].split()[-1][:-1]
                i=i+1
                
            elif("def"+" " in lines[i]):
                temp=lines[i]
                counter=i+1
                indent=self.indent(lines[i])
                new_indent=self.indent(lines[counter])
                while(new_indent>indent and (counter+1)<len(lines)):
                    temp=temp+lines[counter]+"\n"
                    counter=counter+1
                    new_indent=self.indent(lines[counter])
                temp_functions.append(temp.strip())
                i=counter
            
            else:
                body_temp=body_temp+lines[i] +"\n"
                i=i+1

        #set body with body string      
        b=ParseBodies(body_temp).getBody()
        self.body=b
            
        #set functions on temp_functtions array
        for function in temp_functions:
            f=ParseFunctions(function).getFunction()
            f.getName()
            self.functions.append(f)

    def setImportedModules(self):
        referenceName = ""
        for reference in self.modulReferences:
            referenceElements = reference.split("-")
            if(referenceElements[0] == "standart" and len(referenceElements) == 2):#standart-modulname
                referenceName = referenceElements[1]
            elif(referenceElements[0] == "standart" and len(referenceElements) == 3):#standart-modulname-mdlname
                referenceName = referenceElements[2]
            elif(referenceElements[0] == "advenced" and len(referenceElements) == 3):#advenced-modulname-classname
                referenceName = referenceElements[2]
            elif(referenceElements[0] == "advenced" and len(referenceElements) == 4):#advenced-modulname-classname-clsname
                referenceName = referenceElements[3]
            classLines = self.classString.splitlines()
            for line in classLines:
                if(referenceName in line):
                    self.importedModules.append(reference)#import modulname as alias
                    break


    def getClass(self):
        return description_objects.Classes(self.name,self.functions,self.body,self.importedModules)


class ParseModules:
    classes=[]
    body=None
    functions=[]
    modul_string=""
    name=""
    imported_modules = []
    
    def __init__(self,name,modul_string):
        self.modul_string=modul_string
        self.name=name
        self.setImportedModules()
        self.clearWhiteLines()
        self.setParameters()

    def setImportedModules(self):
        lines = self.modul_string.splitlines()
        for line in lines:
            if("from " in line):#from modulname import classname
                index = line.strip().split().index("from ")
                temp = "advenced-"
                temp = temp + line.split()[index + 1]#module name
                temp = temp + "-" + line.split()[index + 3]
                if("as" in line):#from modulname import classname as clsname
                    temp = temp + "-" + line.split()[index + 5]
                self.imported_modules.append(temp)

            elif("import " in line):#import modulname
                index = line.strip().split().index("import ")
                temp = "standart-"
                temp = temp + line.split()[index+1]
                if("as" in line):#import modulname as mdl
                    temp = temp + "-" + line.split()[index+3]
                self.imported_modules.append(temp)

    def indent(self,string):
        indent=0

        while(indent<len(string) and not(string[indent].isalpha())):
            indent=indent+1

        return indent

    def isWhiteLine(self,line):
        for i in line:
            if(i!=" "):
                return False
        return True

    def clearWhiteLines(self):
        lines = self.modul_string.splitlines()
        temp_modul_string = ""

        for line in lines:
            if(self.isWhiteLine(line)==False):
                temp_modul_string =temp_modul_string + line +"\n"

        self.modul_string = temp_modul_string
    
    def setParameters(self):

        if(("class" not in self.modul_string) and ("def" not in self.modul_string)):
            self.body=ParseBodies(self.modul_string)
        
        elif("class" not in self.modul_string):
            self.classes=ParseClasses(self.modul_string)
            
        else:
            lines=self.modul_string.splitlines()
            i=0
            counter=0
            indent=0
            new_indent=0
            temp_class=""
            temp_classes=[]
            temp_body=""
            
            while(i<len(lines)):
                line_split=lines[i].split(" ")
                if("class" in line_split):
                    temp_class=""
                    indent=self.indent(lines[i])
                    counter=i
                    new_indent=self.indent(lines[counter+1])
                    while(new_indent>indent and (counter+1)<len(lines)):
                        temp_class+=lines[counter]+" "
                        print(lines[counter]+"\n")
                        counter=counter+1
                        new_indent=self.indent(lines[counter])
                    i=counter
                    temp_classes.append(temp_class.strip())

                else:
                    temp_body+=lines[i]+"\n"
                    i=i+1
                    
            body_class=ParseClasses(temp_body,self.imported_modules).getClass()
            self.body=body_class#the bodies of the modules are class type data
            
            for clsa in temp_classes:
                c=ParseClasses(clsa,self.imported_modules).getClass()
                self.classes.append(c)
                
    def getModule(self):
        return description_objects.Modules(self.name,self.classes,self.body,self.imported_modules)


class ParseProject:
    modules=[]
    project_name=""
    
    def __init__(self,project_name):
        self.project_name=project_name
        
    def addModul(self,name,modul_string):
        modul=ParseModules(name,modul_string)        
        self.modules.append(modul)
        return True
        
    def deleteModul(self,name):
        modules=[]
        
        for modul in self.modules:
            if(modules.getName()!=name):
                modules.append(modul)
        self.modules=modules
        return True
    
    def updateModul(self,name,modul_string):
        for i in range(len(self.modules)):
            if(self.modules[i].getName()==name):
                modul=ParseModules(name,modul_string)
                self.modules[i]=modul
                return True
        return False
            
    def getProject(self):
        project=description_objects.Project(self.project_name,self.modules)
        return project
