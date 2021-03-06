from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
#from direct.task.Task import Tasks
from direct.actor.Actor import Actor


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.camera.setPos(0,45,52)
        self.disableMouse()
        self.camera.setHpr(0,-40,0)
        self.wall=self.loader.loadModel("line2.egg")
        self.wall.reparentTo(self.render)
        self.wall.setPos(-0.2,100,-21)


        self.L=self.Lway(1)
        self.L.changePozVar(1,100,14)
        self.z=self.fillUp()
        self.tabus=self.coll()
        self.info=self.objInfo(0,0,0,1,1)
        self.ster(self.L)
        self.taskMgr.add(self.fall, 'fall', extraArgs=[self.L])
        self.taskMgr.add(self.betterlogic, "logic", extraArgs=[self.L, self.tabus, self.z])


    class pudlo():
        def __init__(self):
            self.pudlo=loader.loadModel("PS2.egg")
            self.pudlo.reparentTo(render)
            self.x = 1
            self.y = 1
            self.z = 1
            self.showStatus=1
        def notShow(self):
           # self.pudlo.detachNode()
            self.pudlo.hide()
            self.showStatus=0
        def Show(self):
            self.pudlo.show()
            self.showStatus=1
        def setPozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z
        def setPoz(self):
            self.pudlo.setPos(self.x,self.y,self.z)



    def ster(self,ob):
        self.accept("a",ob.moveL)
        self.accept("d",ob.moveR)
        self.accept("w", ob.moveUp)
        self.accept("s", ob.moveDown)
        self.accept("g",ob.changeStatusUp)
        self.accept("h", ob.changeStatusDown)

    class Lway():
        def __init__(self,stat):
            self.x=0
            self.y=0
            self.z=0
            self.swapS=0
            self.logX=0
            self.logY=0
            self.logZ=0

            self.state=stat
            if(self.state==1):
                self.p0=MyApp.pudlo()
                self.p0.setPozVar(self.x,self.y,self.z)
                self.p0.setPoz()

                self.p1=MyApp.pudlo()
                self. p1.setPozVar(self.x,self.y,self.z+2)
                self. p1.setPoz()
                self. p2=MyApp.pudlo()
                self. p2.setPozVar(self.x+2,self.y,self.z+2)
                self. p2.setPoz()

                self.p3=MyApp.pudlo()
                self.p3.setPozVar(self.x+4,self.y,self.z+2)
                self.p3.setPoz()
            if(self.state==2):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x, self.y, self.z + 4)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x+2, self.y, self.z)
                self.p3.setPoz()
            if(self.state==3):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x+2, self.y, self.z )
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x + 4, self.y, self.z)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x + 4, self.y, self.z + 2)
                self.p3.setPoz()
            if(self.state==4):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x , self.y, self.z + 4)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x -2, self.y, self.z + 4)
                self.p3.setPoz()
        def setLogs(self):
            self.logX=int((self.x+9)//2)
            self.logZ=int((self.z-21)//(-2))

        def updatePoz(self):
            if(self.state==1):
                self.p0.setPozVar(self.x,self.y,self.z)
                self.p0.setPoz()
                self. p1.setPozVar(self.x,self.y,self.z+2)
                self. p1.setPoz()
                self. p2.setPozVar(self.x+2,self.y,self.z+2)
                self. p2.setPoz()
                self.p3.setPozVar(self.x+4,self.y,self.z+2)
                self.p3.setPoz()

            if(self.state==2):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2.setPozVar(self.x, self.y, self.z + 4)
                self.p2.setPoz()
                self.p3.setPozVar(self.x + 2, self.y, self.z)
                self.p3.setPoz()
            if(self.state==3):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x+2, self.y, self.z )
                self.p1.setPoz()
                self.p2.setPozVar(self.x + 4, self.y, self.z)
                self.p2.setPoz()
                self.p3.setPozVar(self.x + 4, self.y, self.z + 2)
                self.p3.setPoz()


            if(self.state==4):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2.setPozVar(self.x , self.y, self.z + 4)
                self.p2.setPoz()
                self.p3.setPozVar(self.x -2, self.y, self.z + 4)
                self.p3.setPoz()
            self.setLogs()
        def changePozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z
            self.setLogs()
        def IncPoz(self,X,Y,Z):
            self.x=self.x+X
            self.y=self.y+Y
            self.z=self.z+Z
        def moveL(self):
            if(self.logX>0):
                self.IncPoz(-2,0,0)
                self.updatePoz()
                self.setLogs()
        def moveR(self):
            if(self.logX<10):
                self.IncPoz(2,0,0)
                self.updatePoz()
                self.setLogs()
        def moveUp(self):
            self.IncPoz(0,0,2)
            self.updatePoz()
            self.setLogs()
        def moveDown(self):
            self.IncPoz(0,0,-2)
            self.updatePoz()
            self.setLogs()
        def changeStatusUp(self):
            if( self.swapS==0):
                if(self.state==4):
                    self.state=0
                self.state=self.state+1
                self.updatePoz()
        def changeStatusDown(self):
            if(self.swapS==0):
                if(self.state==1):
                    self.state=5
                self.state=self.state-1
                self.updatePoz()

    class cube():
        def __init__(self, stat):
            self.x = 0
            self.y = 0
            self.z = 0
            self.swapS = 0
            self.logX = 0
            self.logY = 0
            self.logZ = 0

            self.state = stat
            if (self.state == 1):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x + 2, self.y, self.z + 2)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x +2, self.y, self.z)
                self.p3.setPoz()


        def setLogs(self):
            self.logX = int((self.x + 9) // 2)
            self.logZ = int((self.z - 21) // (-2))

        def updatePoz(self):
            if (self.state == 1):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2.setPozVar(self.x + 2, self.y, self.z + 2)
                self.p2.setPoz()
                self.p3.setPozVar(self.x +2, self.y, self.z)
                self.p3.setPoz()


            self.setLogs()

        def changePozVar(self, X, Y, Z):
            self.x = X
            self.y = Y
            self.z = Z
            self.setLogs()

        def IncPoz(self, X, Y, Z):
            self.x = self.x + X
            self.y = self.y + Y
            self.z = self.z + Z

        def moveL(self):
            if (self.logX > 0):
                self.IncPoz(-2, 0, 0)
                self.updatePoz()
                self.setLogs()

        def moveR(self):
            if (self.logX < 10):
                self.IncPoz(2, 0, 0)
                self.updatePoz()
                self.setLogs()

        def moveUp(self):
            self.IncPoz(0, 0, 2)
            self.updatePoz()
            self.setLogs()

        def moveDown(self):
            self.IncPoz(0, 0, -2)
            self.updatePoz()
            self.setLogs()

        def changeStatusUp(self):
            return

        def changeStatusDown(self):
            return

    class strline():
        def __init__(self,stat):
            self.x=0
            self.y=0
            self.z=0
            self.swapS=0
            self.logX=0
            self.logY=0
            self.logZ=0

            self.state=stat
            if(self.state==1):
                self.p0=MyApp.pudlo()
                self.p0.setPozVar(self.x,self.y,self.z)
                self.p0.setPoz()

                self.p1=MyApp.pudlo()
                self. p1.setPozVar(self.x+2,self.y,self.z)
                self. p1.setPoz()
                self. p2=MyApp.pudlo()
                self. p2.setPozVar(self.x+4,self.y,self.z)
                self. p2.setPoz()

                self.p3=MyApp.pudlo()
                self.p3.setPozVar(self.x+6,self.y,self.z)
                self.p3.setPoz()
            if(self.state==2):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x, self.y, self.z + 4)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x, self.y, self.z+6)
                self.p3.setPoz()

        def setLogs(self):
            self.logX=int((self.x+9)//2)
            self.logZ=int((self.z-21)//(-2))

        def updatePoz(self):
            if(self.state==1):
                self.p0.setPozVar(self.x,self.y,self.z)
                self.p0.setPoz()
                self. p1.setPozVar(self.x+2,self.y,self.z)
                self. p1.setPoz()
                self. p2.setPozVar(self.x+4,self.y,self.z)
                self. p2.setPoz()
                self.p3.setPozVar(self.x+6,self.y,self.z)
                self.p3.setPoz()

            if(self.state==2):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2.setPozVar(self.x, self.y, self.z + 4)
                self.p2.setPoz()
                self.p3.setPozVar(self.x , self.y, self.z+6)
                self.p3.setPoz()
            self.setLogs()
        def changePozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z
            self.setLogs()
        def IncPoz(self,X,Y,Z):
            self.x=self.x+X
            self.y=self.y+Y
            self.z=self.z+Z
        def moveL(self):
            if(self.logX>0):
                self.IncPoz(-2,0,0)
                self.updatePoz()
                self.setLogs()
        def moveR(self):
            if(self.logX<10):
                self.IncPoz(2,0,0)
                self.updatePoz()
                self.setLogs()
        def moveUp(self):
            self.IncPoz(0,0,2)
            self.updatePoz()
            self.setLogs()
        def moveDown(self):
            self.IncPoz(0,0,-2)
            self.updatePoz()
            self.setLogs()
        def changeStatusUp(self):
            if( self.swapS==0):
                if(self.state==2):
                    self.state=0
                self.state=self.state+1
                self.updatePoz()
        def changeStatusDown(self):
            if(self.swapS==0):
                if(self.state==1):
                    self.state=3
                self.state=self.state-1
                self.updatePoz()

    class objInfo():
        def __init__(self,X,Y,Z,typ,typRot):
            self.logX=X
            self.logY=Y
            self.logZ=Z
            self.type=typ
            self.typeRot=typRot
        def setLogs(self,x,y,z):
            self.logX=(x+9)//2
            self.logZ=(z-21)//(-2)


    def printlogs(self,obj,obj2):
        obj.setLogs(obj2.x,obj2.y,obj2.z)
        print(obj.logX)
        print(obj.logY)
        print(obj.logZ)
        print("-----------------------")
        return Task.cont

    def fall(self,obj):
        obj.IncPoz(0,0,-0.01)
        obj.updatePoz()
        return Task.cont

    class fillUp(pudlo):
        class cell():
            def __init__(self):
                self.boxHold=MyApp.pudlo()
                self.exsist=0
        def __init__(self):
            self.boxTab=[]

            for i in range(21):
                self.littleTab = []
                for j in range(10):
                    self.pom=self.cell()
                    self.pom.boxHold.setPozVar(-(9-2*j),100,-(2*i-19))
                    self.pom.boxHold.setPoz()
                    self.pom.boxHold.notShow()
                    self.littleTab.append(self.pom)


                    #self.boxTab[i][j].append(self.pom)

                    #self.boxTab[i][j].boxHold.notShow
                    #self.pom=MyApp.pudlo()
                    #self.pom.setPozVar(9-2*j,100,2*i-21)
                    #self.pom.setPoz()
                    #self.boxTab.append(self.pom)
                self.boxTab.append(self.littleTab)
        def showBox(self):
            for i in range(20):
                for j in range(10):
                    if(self.boxTab[i][j].boxHold.showStatus==0 and  self.boxTab[i][j].exsist==1):
                        self.boxTab[i][j].boxHold.Show()
                    if(self.boxTab[i][j].boxHold.showStatus == 1 and self.boxTab[i][j].exsist==0):
                        self.boxTab[i][j].boxHold.notShow()

    class coll():
        def __init__(self):
            self.tab=[]
            for i in range(21):
                self.litTab = []
                for j in range(10):
                    self.litTab.append(0)
                self.tab.append(self.litTab)
        def update(self,obj):
            for i in range(21):
                for j in range(10):
                    self.tab[i][j]=0
            if (isinstance(obj,MyApp.Lway)):
                if(obj.state==1):
                    self.tab[obj.logZ][obj.logX]=1
                    self.tab[obj.logZ-1][obj.logX]=1
                    self.tab[obj.logZ-1][obj.logX+1]=1
                    self.tab[obj.logZ-1][obj.logX+2]=1
                if (obj.state == 2):
                    self.tab[obj.logZ][obj.logX]=1
                    self.tab[obj.logZ ][obj.logX+1]=1
                    self.tab[obj.logZ - 1][obj.logX]=1
                    self.tab[obj.logZ - 2][obj.logX]=1
                if (obj.state == 3):
                    self.tab[obj.logZ][obj.logX] = 1
                    self.tab[obj.logZ][obj.logX + 1] = 1
                    self.tab[obj.logZ][obj.logX + 2] = 1
                    self.tab[obj.logZ-1][obj.logX + 2] = 1
                if (obj.state == 4):
                    #print obj.logZ
                    self.tab[obj.logZ][obj.logX] = 1
                    self.tab[obj.logZ-1][obj.logX ] = 1
                    self.tab[obj.logZ - 2][obj.logX] = 1
                    self.tab[obj.logZ - 2][obj.logX -1] = 1
            if (isinstance(obj, MyApp.strline)):
                if (obj.state == 2):
                    self.tab[obj.logZ][obj.logX] = 1
                    self.tab[obj.logZ -1][obj.logX] = 1
                    self.tab[obj.logZ -2][obj.logX] = 1
                    self.tab[obj.logZ -3][obj.logX] = 1
                if (obj.state == 1):
                    self.tab[obj.logZ][obj.logX] = 1
                    self.tab[obj.logZ][obj.logX + 1] = 1
                    self.tab[obj.logZ][obj.logX+2] = 1
                    self.tab[obj.logZ][obj.logX+3] = 1
            if (isinstance(obj, MyApp.cube)):
                if (obj.state == 1):
                    self.tab[obj.logZ][obj.logX] = 1
                    self.tab[obj.logZ - 1][obj.logX] = 1
                    self.tab[obj.logZ - 1][obj.logX + 1] = 1
                    self.tab[obj.logZ][obj.logX + 1] = 1
    def colide(self,obj,coll,groud):
        def fallColide(self,obj,coll,groud):
            '''
            1-floor thouch down
            2-box hit


            '''

            self.flag = 0
            if (obj.logZ > 18):
                self.flag=1
                return self.flag

            for i in range(20):
                for j in range(10):
                    if (coll.tab[i][j] == 1 and groud.boxTab[i][j].exsist == 1):
                        self.flag =2
                        return  self.flag
            return self.flag
        def swapCollide(self,obj,coll,groud):
            self.flag=0
            obj.swapS =0
            obj.changeStatusUp()
            coll.update(obj)
            for i in range(20):
                for j in range(10):
                    if (coll.tab[i][j] == 1 and groud.boxTab[i][j].exsist == 1):
                        self.flag=3
                        break
                        break

            obj.changeStatusDown()
            obj.changeStatusDown()
            coll.update(obj)
            for i in range(20):
                for j in range(10):
                    if (coll.tab[i][j] == 1 and groud.boxTab[i][j].exsist == 1):
                        if(self.flag==3):
                            self.flag=5
                        else:
                            self.flag=4
                        break
                        break

            obj.changeStatusUp()

            coll.update(obj)
            obj.swapS = self.flag
            return self.flag


        return [fallColide(self,obj,coll,groud),swapCollide(self,obj,coll,groud)]
    def setBack(self,obj):
        obj.changePozVar(obj.x,obj.y,17)
        obj.updatePoz()

    def betterlogic(self,obj,coll,groud):

        self.pom=MyApp.colide(self,obj,coll,groud)

        self.fallhit=self.pom[0]
        if(self.fallhit==1):
            for k in range(20):
                for p in range(10):
                    if (coll.tab[k][p] == 1):
                        groud.boxTab[k][p].exsist = 1
                        MyApp.setBack(self,obj)
        if(self.fallhit==2):
            for k in range(20):
                for p in range(10):
                    if (coll.tab[k][p] == 1):
                        self.flag = 1
                        groud.boxTab[k - 1][p].exsist = 1
                        MyApp.setBack(self, obj)
        self.swapHit0=self.pom[1]



        groud.showBox()
        coll.update(obj)
       # MyApp.ster(self,obj)
        return Task.cont

    def log(self,obj,coll,groud):
        self.a = []
        self.a=MyApp.colide(self,obj,coll,groud)
        coll.update(obj)
        self.flag=0
        if(obj.logZ>19):
            for k in range(20):
                for p in range(10):
                    if (coll.tab[k][p] == 1):
                        groud.boxTab[k][p].exsist = 1
            obj.moveUp()
            obj.moveUp()
            obj.moveUp()
            obj.moveUp()

        else:
            for i in range(20):
                for j in range(10):
                    if(coll.tab[i][j]==1 and groud.boxTab[i][j].exsist==1):

                        for k in range(20):
                            for p in range(10):
                                if (coll.tab[k][p] == 1):
                                    self.flag=1
                                    groud.boxTab[k-1][p].exsist = 1
                        break
        '''
        for i in range(20):
            self.counter = 0
            for j in range(10):
                if(groud.boxTab[i][j]==1):
                    self.counter=self.counter+1
            if(self.counter>9):
                for j in range(10):
                    groud.boxTab[i][j] =0
            '''
        if(self.flag==1):
            obj.moveUp()
            obj.moveUp()
            obj.moveUp()
            obj.moveUp()
            obj.moveUp()
            obj.moveUp()
        groud.showBox()
        coll.update(obj)


       # print a

        return Task.cont



app = MyApp()
app.run()