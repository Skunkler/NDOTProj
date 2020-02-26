#Script was written by Warren Kunkler to create a new NDOT roads feature class with fields and domains. This script takes one database sde connection file as
#it's input and outputs the LVVWDGIS_INT.NDOT_Roads feature class

import arcpy, sys, traceback, datetime
from arcpy import env


#enter a location to an sde file
dbaseConnection = """C:\Users\matthysj\AppData\Roaming\ESRI\Desktop10.6\ArcCatalog\lvvwdgis_int_dev.sde"""


outpath = dbaseConnection


##create feature class and necessary fields
print "creating roads feature class now"
try:    
    arcpy.CreateFeatureclass_management(out_path=outpath,out_name="LVVWDGIS_INT.NDOT_Roads",geometry_type="POLYLINE",template="",has_m="DISABLED",has_z="DISABLED",spatial_reference="PROJCS['NAD_1983_StatePlane_Nevada_East_FIPS_2701_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',656166.6666666665],PARAMETER['False_Northing',26246666.66666666],PARAMETER['Central_Meridian',-115.5833333333333],PARAMETER['Scale_Factor',0.9999],PARAMETER['Latitude_Of_Origin',34.75],UNIT['Foot_US',0.3048006096012192]];-17790500 -19184900 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision",config_keyword="SDO_DEFAULTS",spatial_grid_1="0",spatial_grid_2="0",spatial_grid_3="0")
    arcpy.MakeFeatureLayer_management(outpath + "\\LVVWDGIS_INT.NDOT_Roads", "Roads_lyr")
    arcpy.AddField_management("Roads_lyr", "FromDate", "DATE", "", "", "", "FromDate", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management("Roads_lyr", "RouteID", "TEXT", "", "", 255, "RouteID", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management("Roads_lyr", "SystemType", "TEXT", "", "", 2, "SystemType", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management("Roads_lyr", "RMID", "LONG")
    arcpy.AddField_management("Roads_lyr", "CountyCode", "TEXT", "", "", 2, "CountyCode", "NULLABLE", "NON_REQUIRED")
    arcpy.AddField_management("Roads_lyr", "RouteNameFull", "TEXT", "", "", 255, "RouteNameFull", "NULLABLE", "NON_REQUIRED")
except:
    print arcpy.GetMessages(2)

#define domains for NDOT Roads feature class
CountyCode_domainDictionary = {'CC': 'CC-Carson City', 'CH': 'CH-Churchill County',\
                               'CL':'CL-Clark County', 'DO':'DO-Douglas County',\
                               'EL':'EL-Elko County', 'ES':'ES-Esmeralda County',\
                               'EU':'Eureka County', 'HU':'Humboldt County', 'LA':'LA-Lander County',\
                               'LN':'LN-Lincoln County', 'LY':'Lyon County', \
                               'MI':'MI-Mineral County', 'NY':'Nye County', 'PE':'Pershing County',\
                               'ST':'ST-Storey County', 'WA':'WA-Washoe County', 'WP':'WP-White Pine County'}


SystemType_domainDictionary = {'01':'01-Interstate', '02':'02-US Highway', '03':'03-State Highway', '04':'04-Collector Distributor', '05':'05-Frontage Road', '06':'06-Access Road',\
                               '07':'07-Ramp', '08':'08-Roadside Park', '09':'09-Truck Inspection', '10':'10-State-Owned', '11':'11-State Park', '12':'12-Functionally Classified'}

#Create the domains
arcpy.CreateDomain_management(outpath, "NDOTCountyCode", "County Code", "TEXT", "CODED")
arcpy.CreateDomain_management(outpath, "NDOTSystemType", "System Type Code", "TEXT", "CODED")



env.workspace = outpath


#add domain values to each of the domains
print "adding CountyCode values"
for key in CountyCode_domainDictionary.keys():
    arcpy.AddCodedValueToDomain_management(outpath, "NDOTCountyCode", key, CountyCode_domainDictionary[key])


print "adding SystemType values"
for key in SystemType_domainDictionary.keys():
    arcpy.AddCodedValueToDomain_management(outpath, "NDOTSystemType", key, SystemType_domainDictionary[key])    

#assign the domains to the fields
try:

    arcpy.AssignDomainToField_management(outpath + '\\LVVWDGIS_INT.NDOT_Roads', 'SystemType', 'NDOTSystemType')
    arcpy.AssignDomainToField_management(outpath + '\\LVVWDGIS_INT.NDOT_Roads', 'CountyCode', 'NDOTCountyCode')

except:
    print arcpy.GetMessages(2)
