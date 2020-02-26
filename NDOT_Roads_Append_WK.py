#This script was written by Warren Kunkler to update LVVWDGIS_INT.NDOT_Maintained_Rds feature class
#it takes the newly released NDOT roads layer
#deletes the old NDOT data found in LVVWDGIS_INT.NDOT_Maintained_Rds and appends the new data


import arcpy, sys, traceback, datetime, os
from arcpy import env

#Get user input for the feature class, obtain workspace from the feature class path
fc = raw_input("Please enter NDOT Roads FC: ")
ws = '\\'.join(fc.split('\\')[:-1])

#set database sde connection
dbaseConnection = r"C:\Users\kunklerw\AppData\Roaming\ESRI\Desktop10.7\ArcCatalog\kunklerw_ops.sde\\"
outpath = dbaseConnection + "LVVWDGIS_INT.NDOT_Maintained_Rds"


outLocation = r"\\storage\snwa\etsexch\GIS\Data_ETL\NDOT\scripts\NDOT_Road_Shapefile"
outName = """NDOT_ROADS_DECODED.shp"""

env.workspace = ws
env.transferDomains = True
arcpy.MakeFeatureLayer_management(fc, 'fc_lyr', "MAINTAINED_BY = 1")
arcpy.FeatureClassToFeatureClass_conversion('fc_lyr', outLocation, outName)

#delete features of old LVVWD_INT.NDOT_Roads and append new features


try:
    print "deleting previous features"
    arcpy.DeleteFeatures_management(outpath)

    print "attempting to append to output feature class"
    inFeature = outLocation + '\\'+ outName
    
    arcpy.Append_management(inputs=inFeature, target=outpath, schema_type="NO_TEST", field_mapping="""'RMID "RMID" true true false 4 Long 0 0 ,First,#,"""+inFeature +""",RMID,-1,-1;
    FIPS_CODE "FIPS Code" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_FIPS_COD,-1,-1;
    SYSTEM "SYSTEM" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_SYSTEM,-1,-1;
    PREFIX "Road Prefix" true true false 5 Text 0 0 ,First,#,"""+inFeature+""",PREFIX,-1,-1;
    ROAD_NAME "Road Name" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",ROAD_NAME,-1,-1;
    ROAD_TYPE "Road Type" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_ROAD_TYP,-1,-1;
    SUFFIX "SUFFIX" true true false 5 Text 0 0 ,First,#,"""+inFeature+""",SUFFIX,-1,-1;
    FULL_NAME "Full Name" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",FULL_NAME,-1,-1;
    DIRECTION "DIRECTION" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_DIRECTIO,-1,-1;
    OWNED_BY "Owned By" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_OWNED_BY,-1,-1;
    MAINTAINED_BY "Maintained By" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_MAINTAIN,-1,-1;
    SURFACE_TYPE "Surface Type" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_SURFACE_,-1,-1;
    FUNC_CODE "Function Code" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_FUNC_COD,-1,-1;
    PROPOSED_FUNC_CODE "Proposed Function Code" true true false 254 Text 0 0 ,First,#;
    FUNC_CODE_ACCEPT_DATE "Function Code Accept Date" true true false 8 Date 0 0 ,First,#;
    DATA_SOURCE "Data Source" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_DATA_SOU,-1,-1;
    DATA_METHOD "Data Method" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_DATA_MET,-1,-1;
    DATA_DATE "Data Date" true true false 8 Date 0 0 ,First,#,"""+inFeature+""",DATA_DATE,-1,-1;
    RECORD_STATUS "Record Status" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_RECORD_S,-1,-1;
    ENTITY_STATUS "Entity Status" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_ENTITY_S,-1,-1;
    FROM_DATE "From Date" true true false 8 Date 0 0 ,First,#,"""+inFeature+""",FROM_DATE,-1,-1;
    TO_DATE "To Date" true true false 8 Date 0 0 ,First,#,"""+inFeature+""",TO_DATE,-1,-1;
    SHAREABLE "SHAREABLE" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",SHAREABLE,-1,-1;
    ALIAS1 "Name Alias 1" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",ALIAS1,-1,-1;
    ALIAS2 "Name Alias 2" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",ALIAS2,-1,-1;
    ALIAS3 "Name Alias 3" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",ALIAS3,-1,-1;
    ALIAS4 "Name Alias 4" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",ALIAS4,-1,-1;
    ALIAS5 "Name Alias 5" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",ALIAS5,-1,-1;
    ALIAS6 "Name Alias 6" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",ALIAS6,-1,-1;
    RAMP_TYPE "Ramp Type" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_RAMP_TYP,-1,-1;
    NATIONAL_HIGHWAY_SYSTEM "National Highway System" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_NATIONAL,-1,-1;
    ONE_WAY "One Way" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_ONE_WAY,-1,-1;
    ONE_WAY_DIRECTION "One Way Direction" true true false 1 Text 0 0 ,First,#;
    DATE_CREATED "Created Date" true true false 8 Date 0 0 ,First,#;
    DATE_MODIFIED "Date Modified" true true false 8 Date 0 0 ,First,#;
    LOCAL_SOURCE_ID "Local Source ID" true true false 4 Long 0 0 ,First,#;
    QC_FLAG "QC Flag" true true false 2 Short 0 0 ,First,#,"""+inFeature+""",QC_FLAG,-1,-1;
    ZIP_CODE_LEFT "Zip Code Left" true true false 5 Text 0 0 ,First,#;
    ZIP_CODE_RIGHT "Zip Code Right" true true false 5 Text 0 0 ,First,#;
    NUMBER_OF_LANES "Number of Lanes" true true false 2 Short 0 0 ,First,#;
    FUEL_TAX_ROAD "Fuel Tax Road" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_FUEL_TAX,-1,-1;
    PUBLIC_ROAD "Public Road" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_PUBLIC_R,-1,-1;
    RS2477 "Revised Statute 2477" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",d_RS2477,-1,-1;
    NOTES "NOTES" true true false 254 Text 0 0 ,First,#,"""+inFeature+""",NOTES,-1,-1;
    ROUTE_NUMBER "Route Number" true true false 2 Short 0 0 ,First,#;
    FROM_ADDRESS_LEFT "From Address Left" true true false 4 Long 0 0 ,First,#;
    FROM_ADDRESS_RIGHT "From Address Right" true true false 4 Long 0 0 ,First,#;
    TO_ADDRESS_LEFT "To Address Left" true true false 4 Long 0 0 ,First,#;
    TO_ADDRESS_RIGHT "To Address Right" true true false 4 Long 0 0 ,First,#;
    COMMUNITY_LEFT "Community Left" true true false 100 Text 0 0 ,First,#;
    COMMUNITY_RIGHT "Community Right" true true false 100 Text 0 0 ,First,#;
    PREFIX_TYPE "Prefix Type" true true false 50 Text 0 0 ,First,#;SHAPE_Length "SHAPE_Length" false true true 8 Double 0 0 ,First,#'""", subtype="")

except:
    print arcpy.GetMessages(2)
