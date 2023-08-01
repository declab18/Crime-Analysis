
# Import arcpy module
import arcpy


# Local variables:
crimes = "crimes"
crimes__3_ = crimes

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(crimes, "NEW_SELECTION", "\"Type\" = 'Drugs'")

