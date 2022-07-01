# def minPartitions(n):
#     n = [int(c) for c in n]
#     max = 0
#     for dig in n:
#         if dig > max:
#             max = dig
#     return max
# print(minPartitions(input()))

# class Vehicle(object):
#     """docstring"""
 
#     def __init__(self, color, doors, tires):
#         """Constructor"""
#         self.color = color
#         self.doors = doors
#         self.tires = tires
    
#     def brake(self):
#         """
#         Stop the car
#         """
#         return "Braking"
    
#     def drive(self):
#         """
#         Drive the car
#         """
#         return "I'm driving!"
 
# if __name__ == "__main__":
#     car = Vehicle("blue", 5, 4)
#     print(car.color)
    
#     truck = Vehicle("red", 3, 6)
#     print(truck.color) 









# from collections import Counter
# import os

# os.chdir(r'C:\Users\Администратор\Desktop')

# answ = ''
# with open ('123.txt','r') as text:
#     text = str(text)
#     c = Counter(text)
#     rares = c.most_common()
#     i = -1
#     while rares[i][1] == 1:
#         answ += rares[i][0]
#         i -= 1
#     print(answ[::-1])
