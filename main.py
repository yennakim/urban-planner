# from building import Building
# from city import City
import datetime


class City:
  def __init__(self, name):
    self.name = name
    self.mayor = ''
    self.yearEstablished = 2024
    self.buildings = list()

class Building:
  def __init__(self, address, stories):
    self.designer = 'Daun Kim' 
    self.date_constructed = ''
    self.owner = ''
    self.address = address
    self.stories = stories
  
  def construct(self):
    self.date_constructed = datetime.datetime.now()
    
  def purchase(self, name):
    self.owner = name    


megalopolis = City("Megalopolis")

eight_hundred_eighth = Building("800 8th Street", 12)
building1 = Building("Building 1", 2)
feathered_friends_hq = Building("Feathered Friends HQ", 5)
sole_sync_hq = Building("Sole Sync HQ", 7)
lapis_hq = Building("Lapis HQ", 9)

    
eight_hundred_eighth = Building("800 8th Street", 12)
eight_hundred_eighth.purchase("Bob Builder")
eight_hundred_eighth.construct()

building1 = Building("Building 1", 2)
building1.purchase("Owner 1")
building1.construct()

feathered_friends_hq = Building("Feathered Friends HQ", 5)
feathered_friends_hq.purchase("Abby")
feathered_friends_hq.construct()

sole_sync_hq = Building("Sole Sync HQ", 7)
sole_sync_hq.purchase("Bruce")
sole_sync_hq.construct()

lapis_hq = Building("Lapis HQ", 9)
lapis_hq.purchase("Maria")
lapis_hq.construct()

megalopolis.buildings.append(eight_hundred_eighth)
megalopolis.buildings.append(building1)
megalopolis.buildings.append(feathered_friends_hq)
megalopolis.buildings.append(sole_sync_hq)
megalopolis.buildings.append(lapis_hq)

for building in megalopolis.buildings:
  print(f'{building.address}')
