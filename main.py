

from direct.showbase.ShowBase import ShowBase



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.plant=loader.loadModel("PS.egg")
        self.plant.reparentTo(render)

app = MyApp()
app.run()