class Aircraft(object):

    def __init__(self, aircraft_type):
        self.aircraft_type = aircraft_type
        self.ammo = 0
        if aircraft_type == 'F18':
            self.max_ammo = 8
            self.base_damage = 30
        elif aircraft_type == 'F35':
            self.max_ammo = 12
            self.base_damage = 50

    def fight(self):
        damage = self.ammo * self.base_damage
        self.ammo = 0
        return damage

    def refill(self, loaded_ammo):
        if self.ammo == self.max_ammo:
            return loaded_ammo
        elif self.ammo + loaded_ammo > self.max_ammo:
            self.ammo = self.max_ammo
            if loaded_ammo - self.max_ammo > 0:
                return loaded_ammo - self.max_ammo
            else:
                return (loaded_ammo - self.max_ammo) * -1                
        elif self.ammo + loaded_ammo <= self.max_ammo:
            self.ammo += loaded_ammo
            return 0

    def get_type(self):
        return 'This is an {}'.format(self.aircraft_type)

    def get_status(self):
        return 'Type: {}, Ammo: {}, Base Damage: {}, All Damage: {}'.format(self.aircraft_type, self.ammo, 
    self.base_damage, (self.ammo * self.base_damage))


aircraft1 = Aircraft('F18')
print(aircraft1.ammo)
print(aircraft1.refill(4))
print(aircraft1.ammo)
print(aircraft1.refill(2))
print(aircraft1.ammo)
print(aircraft1.get_status())
aircraft1.fight()
print(aircraft1.get_status())
