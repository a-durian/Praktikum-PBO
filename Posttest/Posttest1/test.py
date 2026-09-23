# class Creep:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, target):
#         print(f"menyerang {target}")
#         target.terima_damage(self.damage)
    
#     def terima_damage(self, jumlah_damage):
#             self.hp -= jumlah_damage
#             if self.hp < 0:
#                 self.hp = 0


# # class test:
#     char1 = Character("drian", 100, 167, 20)
#     creep1 = Creep("shibal", 50, 7)
#     print("Sebelum diserang")
#     print("Nama: ", creep1.name, "HP: ", creep1.hp, "\n")

#     char1.attack(creep1)

#     print(f"{char1.name} Menyerang creep dengan {char1.damage} damage!")
#     print("Nama: ", creep1.name, "HP:", creep1.hp)

#     char1.attack(creep1)
#     print(f"{char1.name} nyerang lagi dengan {char1.damage} damage!")
#     print("Nama: ", creep1.name, "HP:", creep1.hp)

#     char1.attack(creep1)
#     print(f"{char1.name} nyerang lagi dengan {char1.damage} damage!")
#     print("Nama: ", creep1.name, "HP:", creep1.hp, "\n")

#     if creep1.hp == 0:
#         print(f"{creep1.name} dikalahkan, mendapatkan ... buff")
   
  
# def attack(self, target):
    #     print(f"{self.name} menyerang {target.name} sebesar {self.damage} damage!")
    #     target.hp -= self.damage
    