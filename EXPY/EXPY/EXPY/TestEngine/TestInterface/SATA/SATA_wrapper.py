from ctypes import cdll
from FromJsonFiles import *

libb = cdll.LoadLibrary(JsonFile.read_json('location_path',0,'api_path' ))


class Storage(object):
    def __init__(self,device_node):
        self.obj = libb.SataStorage_new()
        libb.SataStorage_Init(self.obj,device_node)

    def IDD(self):
        r = libb.SataStorage_Identify(self.obj)
        return r
    def ReadSector(self,val):
	r = libb.ReadSector(self.obj,100)
        return r
    def WriteSector(self,val):
        r = libb.WriteSector(self.obj,val)
        return r
    def WriteCache(self,val):
        r = libb.WriteCache(self.obj,val)
        return r
