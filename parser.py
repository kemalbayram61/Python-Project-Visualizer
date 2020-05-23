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
                while(self.functions[i+counter]!="("):#def getName(self):
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

dize="""def setParameters(self):
        temp=""
        for i in range(len(self.functions)):
            if(self.functions[i]==" "):
                counter=1
                while(self.functions[i+counter]!="("):#def getName(self):
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
                break"""

a=ParseFunctions(dize)
print(a.getFunction().getJson())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        