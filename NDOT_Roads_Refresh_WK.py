import arcpy, sys, traceback, datetime
from arcpy import env

env.workspace = r''
dbaseConnection = raw_input("Please enter a database connection: ")

env.transferDomains = True

try: 
    inFeatures = r"\\storage\\snwa\\etsexch\\GIS\\Data_ETL\\NDOT\\NDOT_Road.gdb\\NV_ROADS"
    outLocation = r"\\storage\\snwa\\etsexch\\GIS\\Data_ETL\\NDOT\\NDOT_Road_Shapefile\\"
    outName = """NDOT_ROADS_DECODED.shp"""

    arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, outName)
    print "Finished creating shapefile " + str(datetime.datetime.now().time())

    arcpy.DeleteFeatures_management(in_features=dbaseConnection+"LVVWDGIS_INT.NDOT_Maintained_Rds")
    print "Finished deleting features from LVVWDGIS_INT.NDOT_Maintained_Rds " + str(datetime.datetime.now().time())

    inFeature = outLocation + outName

    
    print "Finished appending into LVVWDGIS_INT.NDOT_Maintained_Rds " + str(datetime.datetime.now().time())

    
