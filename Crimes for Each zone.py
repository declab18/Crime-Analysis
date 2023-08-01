
# Import arcpy module
import arcpy


# Local variables:
Bambalapitiya = "Bambalapitiya"
crimes__2_ = "crimes"
Bambalapitiya__2_ = "Bambalapitiya"
Bambalapitiya_Crimes_shp = "D:\\MSc-Assignment\\Answers\\Task-3\\output\\Bambalapitiya_Crimes.shp"
Bambalapitiya_Crimes_shp__2_ = Bambalapitiya_Crimes_shp

# Process: Clip
arcpy.Clip_analysis(crimes__2_, Bambalapitiya__2_, Bambalapitiya_Crimes_shp, "")

# Process: Add Field
arcpy.AddField_management(Bambalapitiya_Crimes_shp, "Value", "LONG", "10", "", "", "", "NULLABLE", "NON_REQUIRED", "")

