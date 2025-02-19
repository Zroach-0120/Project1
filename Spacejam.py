from direct.showbase.ShowBase import ShowBase
import math, sys, random
import os



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

    def SetupScene(self):
        # Load and set up the universe
        self.Universe = self.loader.loadModel('./Assets/Universe/Universe.obj')
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        universe_tex = self.loader.loadTexture("Assets/Universe/Universe2.jpg")
        self.Universe.setTexture(universe_tex, 1)

        # Load and set up the planets
        self.Planet1 = self.loader.loadModel('Assets/Planets/protoPlanet.x')
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(33150, 5000, 31)
        self.Planet1.setScale(350)
        planet1_tex = self.loader.loadTexture("Assets/Planets/WaterPlanet2.png")
        self.Planet1.setTexture(planet1_tex, 1)

        #2
        self.Planet2 = self.loader.loadModel('Assets/Planets/protoPlanet.x')
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(2550, 8100, 2167)
        self.Planet2.setScale(350)
        planet2_tex = self.loader.loadTexture("Assets/Planets/c-1.png")
        self.Planet2.setTexture(planet2_tex, 1)

        #3
        self.Planet3 = self.loader.loadModel('Assets/Planets/protoPlanet.x')
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(8350, 5200, 1)
        self.Planet3.setScale(350)
        planet3_tex = self.loader.loadTexture("Assets/Planets/planet3.jpg")
        self.Planet3.setTexture(planet3_tex, 1)

        #4
        self.Planet4 = self.loader.loadModel('Assets/Planets/protoPlanet.x')
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(1450, 5300, 167)
        self.Planet4.setScale(350)
        planet4_tex = self.loader.loadTexture("Assets/Planets/c-2.png")
        self.Planet4.setTexture(planet4_tex, 1)

        #5
        self.Planet5 = self.loader.loadModel('Assets/Planets/protoPlanet.x')
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(2550, 5400, 1100)
        self.Planet5.setScale(350)
        planet5_tex = self.loader.loadTexture("Assets/Planets/planet2.jpg")
        self.Planet5.setTexture(planet5_tex, 1)

        #6
        self.Planet6 = self.loader.loadModel('Assets/Planets/protoPlanet.x')
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(5650, 5500, 2500)
        self.Planet6.setScale(350)
        planet6_tex = self.loader.loadTexture("Assets/Planets/c-3.png")
        self.Planet6.setTexture(planet6_tex, 1)


        #player
        self.Player = self.loader.loadModel('Assets/Spaceships/spacejet.3ds')  # Placeholder path
        self.Player.reparentTo(self.render)
        self.Player.setPos(100, 100, 0)  # Starting at origin
        self.Player.setScale(100)  # Adjust scale as needed

        player_tex = self.loader.loadTexture("Assets/Spaceships/spacejet_C.png")  # Placeholder texture
        self.Player.setTexture(player_tex, 1)


        #Space Station
        self.SpaceStation = self.loader.loadModel('Assets/SpaceStation/spaceStation.x')  # Placeholder path
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(500, 4000, 100)  # Adjust position as needed
        self.SpaceStation.setScale(100)

        station_tex = self.loader.loadTexture('Assets/SpaceStation/SpaceStation1_Dif2.png')  # Placeholder texture
        self.SpaceStation.setTexture(station_tex, 1)
        
        def texture_exists(texPath):
    
                return os.path.isfile(texPath)

app = MyApp()
app.run()