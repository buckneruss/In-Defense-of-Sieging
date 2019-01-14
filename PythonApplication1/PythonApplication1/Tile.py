import json


class Tile(object):
    """Tile Object containing all relevant information for a tile"""

    #used to create instance of a tile at X, Y
    def __init__(self, X, Y, terraintype):
        self.X = X #X coordinate
        self.Y = Y #Y coordinate
        self.terrain = ReadTerrainList(terraintype) #function for setting the Terrain Type
        self.tileEffects = []
        self.unit = None


    #Getter functnions for the X and Y coordinates
    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y


    #Terrain Info and Effects
    def get_terrain_type(self):
        return self.terrain['ID']

    def get_terrain_movement_cost(self):
        return self.terrain['Movement_Cost']
    #def get_whatever(self):


    #Tile Effects
    #may need to change 'effect' variable
    def add_effect(self, effect):
        self.tileEffects.append(effect)

    def remove_effect(self, effect):
        self.tileEffects.remove(effect)

    #method to return specific info
    def has_effect(self, effect):
        for i in tileEffects:
            if tileEffects[i]==effect:
                return true
        return false


    #Unit: Getter and Setter
    def get_unit(self):
        return self.unit

    def set_unit(self, unit):
        self.unit = unit #ONLY EVER 1 UNIT, 2 units cannot occupy the same tile


    #No need for Setter functions (yet)
        #coordinates should only be created when instantiated