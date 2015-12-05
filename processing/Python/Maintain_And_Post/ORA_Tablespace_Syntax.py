
tbs = "PROCESS,SDE,SDEALLEDITS_DT,SDEALLEDITS_IX,SDEBUS_DT,SDEBUS_DT_M,SDEBUS_IX,SDEBUS_LOB_SEG,SDEBUS_LOB_SEG_IX,SDEDELTA_DT,SDEDELTA_DT_M,SDEDELTA_IX,SDEDELTA_LOB_SEG,SDEDELTA_LOB_SEG_IX,SDEFEA_DT_M,SDEFEA_IX,SDEFEA_LOB_SEG,SDEFEA_LOB_SEG_IX,SDENET_BLOB,SDESPA_DT_M,SDESPA_IX,SDEUSER_DT,SDE_DT_M,SDE_IX,TOOLS,UNDOTBS1"

for tb in tbs.split(","):
    string = """CREATE TABLESPACE {0} DATAFILE 'D:/app/chri6962/oradata/pnmgdgp/{0}.dbf'
    SIZE 100M AUTOEXTEND ON NEXT 51200K MAXSIZE UNLIMITED EXTENT MANAGEMENT
    LOCAL UNIFORM SIZE 320K LOGGING ONLINE SEGMENT SPACE MANAGEMENT MANUAL;"""
    print string.format(tb)