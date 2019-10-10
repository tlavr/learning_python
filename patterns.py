import abc
flg_context = "JSON" #"JSON"

#левая сторона моста
class AbstractView(metaclass=abc.ABCMeta):
    __imp = None

    def __init__(self):
        if flg_context == "XML":
            self.__imp = ViewImplXML()
        elif flg_context == "JSON":
            self.__imp = ViewImplJSON()

    def getImplementation(self):
        return self.__imp

    def drawText(self, text=" "):
        return self.getImplementation().drawText(text)

    def drawLine(self, text=" "):
        return self.getImplementation().drawLine()

    def printResult(self, text=" "):
        return print(self.getImplementation().getResult())

class ViewContent(AbstractView):
    def printParagraf(self, text=""):
        self.drawText(text)

class ViewTable(AbstractView):
    def drawCell(self, text=""):
        self.drawLine()
        self.drawText(text)
        self.drawLine()

class ViewNewPlane(AbstractView):
    def view(self):
        print(self.getImplementation().get_new_plane())

#правая сторона моста
class AbstractViewImpl(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drawText(self): pass

    @abc.abstractmethod
    def drawLine(self): pass

    @abc.abstractmethod
    def getResult(self): pass

    @abc.abstractmethod
    def get_new_plane(self): pass

class ViewImplXML(AbstractViewImpl):
    __result = "<xml>"

    def drawLine(self):
        self.__result = self.__result + "\n" + "-----XML-----"

    def drawText(self, text=None):
        self.__result = self.__result + "\n" + text

    def getResult(self):
        return self.__result

    def get_new_plane(self): return self.__result + "\n" + "I'm new plane!!!"

class ViewImplJSON(AbstractViewImpl):
    __result = "<JSON>"

    def drawLine(self):
        self.__result = self.__result + "\n" + "-----JSON-----"

    def drawText(self, text=None):
        self.__result = self.__result + "\n" + text

    def getResult(self):
        return self.__result
    
    def get_new_plane(self): return self.__result + "\n" + "I'm new plane!!!"

content = ViewContent()
table = ViewTable()
plane = ViewNewPlane()
plane.view()

content.printParagraf("I'm Mr.Paragraf!")
content.printResult()
table.drawCell("I'm cell")
table.printResult()
        
    
