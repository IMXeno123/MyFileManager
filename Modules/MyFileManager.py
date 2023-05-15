import filetype,os,re

class MyFileProcess:
    def __init__(self):
        pass

    def repair_ext(self, dir_:str, is_log=True) -> None:
        self.dir_ = dir_
        self.is_log = is_log
        if is_log:
            log_1 = False
        else:
            log_1 = True
        files = os.listdir(dir_)
        for file in files:
            path = f"{dir_}/{file}"
            if os.path.isfile(path):
                if not re.findall(r"\.",file):
                    kind = filetype.guess(f"{dir_}/{file}")
                    if kind==None:
                            continue
                    g_ext = "." + kind.extension
                    new_name = file + g_ext
                    os.rename(f"{dir_}/{file}", f"{dir_}/{new_name}")
                    if is_log:
                        print(f"{file}  ->  {new_name} repaired seccessfully!")
                        log_1 = True
                else:
                    name = file.split(".")[0]
                    ext = file.split(".")[-1]
                    kind = filetype.guess(f"{dir_}/{file}")
                    if kind==None:
                            continue
                    if not ext==kind.extension:
                        g_ext = "." + kind.extension
                        new_name = name + g_ext
                        os.rename(f"{dir_}/{file}", f"{dir_}/{new_name}")
                        if is_log:
                            print(f"{file}  ->  {new_name} repaired seccessfully!")
                            log_1 = True
        if is_log and log_1:
            print("------------------------------------")
            print("Done.")
        elif not log_1:
            print("No error!!!")
        else:
            pass

    def repair_ext_walk(self, dir_:str, is_log=True) -> None:
        self.dir_ = dir_
        self.is_log = is_log
        if is_log:
            log_1 = False
        else:
            log_1 = True
        for root, dirs, files in os.walk(dir_):
            dir_ = re.sub(r"\\", "/", root)
            if files:
                for file in files:
                    if not re.findall(r"\.",file):
                        kind = filetype.guess(f"{dir_}/{file}")
                        if kind==None:
                            continue
                        g_ext = "." + kind.extension
                        new_name = file + g_ext
                        os.rename(f"{dir_}/{file}", f"{dir_}/{new_name}")
                        if is_log:
                            print(f"{file}  ->  {new_name} repaired seccessfully!")
                            log_1 = True
                    else:
                        name = file.split(".")[0]
                        ext = file.split(".")[-1]
                        kind = filetype.guess(f"{dir_}/{file}")
                        if kind==None:
                            continue
                        if not ext==kind.extension:
                            g_ext = "." + kind.extension
                            new_name = name + g_ext
                            os.rename(f"{dir_}/{file}", f"{dir_}/{new_name}")
                            if is_log:
                                print(f"{file}  ->  {new_name} repaired seccessfully!")
                                log_1 = True
        if is_log and log_1:
            print("------------------------------------")
            print("Done.")
        elif not log_1:
            print("No error!!!")
        else:
            pass



if __name__ == "__main__":
    myflie = MyFileProcess()
    try:
        myflie.repair_ext_walk("test")
    except Exception as error :
        print(error)


