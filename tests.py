from Modules.MyFileManager import MyFileProcess



list_path = ["E:/Pictures/Saved Pictures", ]
myfile = MyFileProcess()
for path in list_path:
    myfile.repair_ext_walk(path)
