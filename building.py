""" import datetime

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


print(f'Designed by {eight_hundred_eighth.designer}, {eight_hundred_eighth.address} was purchased by {eight_hundred_eighth.owner} on {eight_hundred_eighth.date_constructed} and has {eight_hundred_eighth.stories} stories.')

print(f'{building1.address} was purchased by {building1.owner} on {building1.date_constructed} and has {building1.stories} stories.')

print(f'{feathered_friends_hq.address} was purchased by {feathered_friends_hq.owner} on {feathered_friends_hq.date_constructed} and has {feathered_friends_hq.stories} stories.')

print(f'{sole_sync_hq.address} was purchased by {sole_sync_hq.owner} on {sole_sync_hq.date_constructed} and has {sole_sync_hq.stories} stories.')
print(f'{lapis_hq.address} was purchased by {lapis_hq.owner} on {lapis_hq.date_constructed} and has {lapis_hq.stories} stories.')
 """
