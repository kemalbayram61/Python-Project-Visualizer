import description

class ParseVariable:
    variable=None
    variable_name=None
    variable_value=None
    variable_type=None
    
    def __init__(self,variable):
        self.variable=variable
        
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
        
        for i in range(len(self.variable)):# a = 5 
            if(self.variable[i]=="="):
                case=True
                continue
            
            if(case==False):
                name=name+self.variable[i]
                
            else:
                value=value+self.variable[i]

        name=name.strip() #deletes spaces if entry with spaces      
        value=value.strip()
                
        self.variable_name=name

        self.variable_value=value
        
        self.variable_type=self.getType(value)

    def getVariables(self):
        self.parse()
        variables=description.Variables(self.variable_name,self.variable_type,self.variable_value)
        return variables
    
class ParseBodies:
    body=None
    variables=[]
    
    def __init__(self,body):
        self.body=body
        
    def isCase(self,location):#a==1 or a!=2
        caseCharacters=["=","!",">","<"]
        if(self.body[location-1] in caseCharacters or self.body[location+1] in caseCharacters):
            return True
        elif(self.body[location-1]=="\""):
            return True
        else:
            return False
    
    def isIncorDec(self,location):#a+=5 or a-=5 increment or decrement
        characters=["+","-","*","/","%"]
        if(self.body[location-1] in characters):
            return True
        else:
            return False
        
    def badCharacters(self,character):
        characters=["=",","," ",")","(","{","}","\n"]
        if(character in characters):
            return True
        else:
            return False
    
    def parse(self):
        
        for i in range(len(self.body)):
            
            if(self.body[i]=="=" and  not(self.isCase(i)) and not(self.isIncorDec(i))):
                counter=1
                temp=""
                temp+=self.body[i]
                while((i-counter)>=0  and not(self.badCharacters(self.body[i-counter]))):#spool backwards
                    temp=self.body[i-counter]+temp
                    counter=counter+1
                    
                counter=1
                while((i+counter)<len(self.body) and not(self.badCharacters(self.body[i+counter]))):#forward spooling
                    temp=temp+self.body[i+counter]
                    counter=counter+1
                    
                variable=ParseVariable(temp).getVariables()
                if(len(self.variables)!=0):
                    case=False
                    for var in self.variables:
                        if(var.getName()==variable.getName()):
                            case=True
                    if(not(case)):
                        self.variables.append(variable)
                else:
                    self.variables.append(variable)
                
                
    def getBody(self):
        self.parse()
        bodies=description.Bodies(self.variables,self.body)
        return bodies
    

class ParseFunctions:
    name=None
    return_parameters=None
    parameters=None
    body=None
    functions=""
    bodyStartIndex=0
    
    def __init__(self,functions):
        self.functions=functions
        
    def setParameters(self):
        temp=""
        for i in range(len(self.functions)):
            if(self.functions[i]==" "):
                counter=1
                while(self.functions[i+counter]!="("):#equal def getName(self):
                    temp+=self.functions[i+counter]
                    counter=counter+1
                self.name=temp
                temp=""
                if(self.functions[i+counter+1]!=")"):#not equal def getName():
                    counter=counter+1
                    while(self.functions[i+counter]!=")"):
                        temp=temp+self.functions[i+counter]
                        counter=counter+1
                    self.bodyStartIndex=i+counter+1
                else:
                    self.bodyStartIndex=i+counter+2
                self.parameters=temp
                break
            
    def setReturns(self):
        if("return" in self.functions):
            temp_array=self.functions.split(" ")
            for i in range(len(temp_array)):
                if(temp_array[i]=="return"):
                    self.return_parameters=temp_array[i+1]
                    break
                    
        else:
            self.return_parameters="void_function"
    
    def parse(self):
        self.setParameters()
        self.setReturns()
        bodyString=self.functions[self.bodyStartIndex:len(self.functions)]
        self.body=ParseBodies(bodyString).getBody()
        
    def getFunction(self):
        self.parse()
        function=description.Functions(self.name,self.parameters,self.return_parameters,self.body)
        return function

class ParseClasses:
    name=None
    functions=[]
    body=None
    classString=""
    def __init__(self,classString):
        self.classString=classString
        
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
            split_lines=lines[i].split(" ")
            if("class" in split_lines):
                self.name=split_lines[-1][0:len(split_lines[-1])-1]
                i=i+1
                
            elif("def" in split_lines):
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
                body_temp=body_temp+lines[i]
                i=i+1
        #set body with body string      
        b=ParseBodies(body_temp).getBody()  
        self.body=b
            
        #set functions on temp_functtions array
        for function in temp_functions:
            f=ParseFunctions(function).getFunction()
            self.functions.append(f)
        
    def getClass(self):
        self.setParameters()
        classes=description.Classes(self.name,self.functions,self.body)
        return classes
        
                    
        

class ParseModules:
    classes=[]
    body=None
    functions=[]
    modul_string=""
    name=""
    
    def __init__(self,name,modul_string):
        self.modul_string=modul_string
        self.name=name

    def indent(self,string):
        indent=0

        while(indent<len(string) and not(string[indent].isalpha())):
            indent=indent+1

        return indent
    
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
                        counter=counter+1
                        new_indent=self.indent(lines[counter])
                    i=counter
                    temp_classes.append(temp_class.strip())
                else:
                    temp_body+=lines[i]+"\n"
                    i=i+1
                    
            body_class=ParseClasses(temp_body).getClass()
            self.body=body_class#the bodies of the modules are class type data
            
            for clsa in temp_classes:
                c=ParseClasses(clsa).getClass()
                self.classes.append(c)
            print(self.body.getJson())
                
    def getModule(self):
        self.setParameters()
        module=description.Modules(self.name,self.classes,self.body)
        return module



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
            
    def getProjec(self):
        project=description.Projects(self.project_name,self.modules)
        return project
     
        
        
        
        
        
        
        
        