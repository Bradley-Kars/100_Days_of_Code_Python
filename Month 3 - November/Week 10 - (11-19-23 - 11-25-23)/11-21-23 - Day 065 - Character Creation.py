class Character:
  def __init__(self, name):
    self.name = name
    self.hp = 1000
    self.mp = 100

  def set_stats(self, hp, mp):
    self.hp = hp
    self.mp = mp

  def display_stats(self):
    print(f"{self.name}\nHP: {self.hp}\tMP: {self.mp}")


class Player(Character):
  def __init__(self, name, nickname):
    super().__init__(name)
    self.nickname = nickname
    self.lives = 3

  def display_stats(self):
    super().display_stats()
    print(f"Nickname: {self.nickname}\tLives: {self.lives}")

  def is_alive(self):
    if self.lives > 0:
      print(f"{self.nickname} LIVES!")
      return True
    else:
      print(f"{self.nickname} has perished!")
      return False


slayer = Player("Player", "Slayer the forgotten")
slayer.display_stats()
print()

class Enemy(Character):
  def __init__(self, name, enemy_type, strength):
    super().__init__(name)
    self.type = enemy_type
    self.strength = strength

  def display_stats(self):
    super().display_stats()
    print(f"Strength: {self.strength}\nType: {self.type}")


class Orc(Enemy):
  def __init__(self, speed, hp=750, mp=0):
    super().__init__("Orc", "Orc", 50)
    self.speed = speed
    self.hp = hp
    self.mp = mp

  def display_stats(self):
    super().display_stats()
    print(f"Speed: {self.speed}")


bagrak = Orc(25)
muk = Orc(20)

bagrak.display_stats()
print()
muk.display_stats()
print()

class Vampire(Enemy):
  def __init__(self, day, hp=500, mp=500):
    super().__init__("Vampire", "Vampire", 50)
    self.day = day
    self.hp = hp
    self.mp = mp

  def display_stats(self):
    super().display_stats()
    print(f"Day: {self.day}")


amdis = Vampire(False)
amdis.display_stats()