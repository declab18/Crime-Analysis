
# Import arcpy module
import arcpy


# Local variables:
crimes = "crimes"
Schools = "Schools"
School_Buffer_shp = "D:\\MSc-Assignment\\Answers\\Task-3\\output\\School_Buffer.shp"
Crimes_Near_To_Schools_shp = "D:\\MSc-Assignment\\Answers\\Task-3\\output\\Crimes_Near_To_Schools.shp"
Crimes_Near_To_Schools = "Crimes_Near_To_Schools"
Crimes_Near_To_Schools__2_ = Crimes_Near_To_Schools

# Process: Buffer
arcpy.Buffer_analysis(Schools, School_Buffer_shp, "150 Meters", "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Clip
arcpy.Clip_analysis(crimes, School_Buffer_shp, Crimes_Near_To_Schools_shp, "")

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(Crimes_Near_To_Schools, "NEW_SELECTION", "\"Type\" = 'Drugs'")

