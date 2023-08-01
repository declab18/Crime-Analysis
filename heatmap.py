crime_layer=QgsVectorLayer("D:/MSc-Assignment/Answers/Task-3/output/crimes.shp","crimes","ogr")
heatmap = QgsHeatmapRenderer()
crime_layer.setRenderer(heatmap)
crime_layer.triggerRepaint()

#Color Ramp
col_ramp = QgsStyle().defaultStyle().colorRamp('Magma')
heatmap.setColorRamp(col_ramp)

#Inverting Color Ramp
col_ramp.invert()

#Change Minimum Color
col_ramp.setColor1(QColor(43,131,186,0))