'''
define file's class
'''

try:
    from data_define import Record
    import chardet
except Exception as error:
    print(f"{error}! " + "Error in file_define.py")
    quit()
else:
    pass

class FileReader:
    
    def read_data(self) -> list[Record]:
        #讀取文件檔案的數據，讀到的每一條數據都轉換為Record對象，通過list封裝返回即可
        pass

class FileWriter:
    def data_to_dict(self) -> str:
        pass
    def write_data(self):
        pass

class TextFileReader(FileReader):

    def __init__(self, path:str):
        self.path = path                #定義成員path



    def read_data(self) -> list[Record]:
        file = open(self.path, "r", encoding = "UTF-8")
        list_record:list[Record] = []
        for line in file.readlines():
            line = line.strip()
            list_data = line.split(",")
            data_record = Record(list_data[0], list_data[1], list_data[2], list_data[3])
            list_record.append(data_record)

        file.close()
        return list_record

class HtmlFileReader(FileReader):

    def __init__(self, path:str):
        self.path = path                #定義成員path



    def read_data(self) -> str:
        with open(self.path, 'rb') as file:             #detect the encoding type
            result = chardet.detect(file.read())
            encoding = result['encoding']
        file = open(self.path, 'r', encoding=encoding)
        html_in_str = str(file.read())
        file.close()
        return html_in_str

class JsonFileReader(FileReader):
    def __init__(self, path:str):
        self.path = path                #定義成員path



    def read_data(self) -> list[Record]:
        file = open(self.path, "r", encoding = "UTF-8")
        list_record:list[Record] = []
        import json
        for line in file.readlines():
            dict_data = json.loads(line)
            
            data_record = Record(dict_data['date'], dict_data['order_id'], dict_data['money'], dict_data['province'])
            list_record.append(data_record)

        file.close()
        return list_record


class MySQLFileReader(FileReader):
    '''
    connetion info request
    '''
    def __init__(self, host:str, port:int, user:str, password:str, autocommit:bool):
        '''
        connetion info request
        '''
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.autocommit = autocommit
    

    def read_data(self, db_name:str, table_name:str) -> list[Record]:
        '''
        which databese and table
        '''
        from pymysql import Connection
        self.db_name = db_name
        self.table_name = table_name
        connt = Connection(
            host=self.host,    
            port=self.port,
            user=self.user,
            password=self.password,
            autocommit=self.autocommit
        )
        cursor = connt.cursor()
        connt.select_db(self.db_name)
        cursor.execute(f"select * from {table_name}")
        results = cursor.fetchall()
        list_record:list[Record] = []
        for rs in results:
            data_record = Record(rs[0], rs[1], rs[2], rs[3])
            list_record.append(data_record)
        connt.close()
        return list_record


class JsonFileWriter(FileWriter):
    def data_to_json(self, record:Record, is_enter:bool = True) -> str:
        import json
        self.record = record
        self.is_enter = is_enter
        dict_line_data = {}
        dict_line_data["date"] = str(record.date)
        dict_line_data["order_id"] = record.order_id
        dict_line_data["money"] = record.money
        dict_line_data["province"] = record.province
        dict_line_data_j = str(json.dumps(dict_line_data, ensure_ascii=False))
        if is_enter:
            return dict_line_data_j + "\n"
        else:
            return dict_line_data_j

    def write_data(self, file_path:str, content:str, close_file:bool = True, a_mode:bool = False):
        '''
        content: str #需要寫入的內容
        a_mode: bool #是否開啟追加模式
        '''

        self.file_path = file_path
        self.content = content
        self.close_file = close_file
        self.a_mode = a_mode
        if self.a_mode:
            myfile = open(f"{self.file_path}", "a")
        else:
             myfile = open(f"{self.file_path}", "w")
        myfile.write(self.content)
        if self.close_file :
            myfile.close()
            print("file has been closed")
            return True
        

if __name__ == "__main__":
    #text_file_reader_1 = TextFileReader("E:/Downloads/2011年1月销售数据.txt")
    #json_file_reader_1 = JsonFileReader("E:/Downloads/2011年2月销售数据JSON.txt")
    #list_1 = text_file_reader_1.read_data()
    #list_2 = json_file_reader_1.read_data()
    #for order_data in list_1:
    #    print(order_data.date)
    #for order_data in list_2:
    #    print(order_data.province)
    sql_file_reader_1 = MySQLFileReader('localhost', 3306, 'root', 'xjszzx123', True)
    list_3 = sql_file_reader_1.read_data('py_sql', 'orders')
    
    for order_data in list_3:
        dict_line_data = {}
        dict_line_data["date"] = str(order_data.date)
        dict_line_data["order_id"] = order_data.order_id
        dict_line_data["money"] = order_data.money
        dict_line_data["province"] = order_data.province
        print(type(dict_line_data))
        break
