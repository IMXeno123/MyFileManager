"""
class of data definition
"""

class Record:
    
    def __init__(self, date:str, order_id:str, money:int, province:str):
        self.date = date                                                
        self.order_id = order_id                                        
        self.money = int(money)                                         
        self.province = province                                        

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"


#class Html:
#    def __init__(self, websource:str):
#        self.websource = str(websource)


#    def __str__(self):
#        return f"{self.websource}"




#class MyFile:
#    def __init__(self, content:str):
#        self.content = str(content)
#    def __str__(self):
#        return f"{self.content}"



if __name__ == '__main__':
    qqq = Record('aaa', 'ccc', '555', 'bbb')
    print(qqq.date)
    print(qqq.money)
    print(type(qqq.money))

