#This code should be implemented in an ArcGIS ToolBox as a script

import arcpy
import os
import time

# --- Tool Inputs (Must match the 0-5 order in your Parameters tab) ---
output_folder    = arcpy.GetParameterAsText(0) 
layout_name      = arcpy.GetParameterAsText(1) 
day_inter_name   = arcpy.GetParameterAsText(2) 
day_seg_name     = arcpy.GetParameterAsText(3) 
night_inter_name = arcpy.GetParameterAsText(4) 
night_seg_name   = arcpy.GetParameterAsText(5) 

# --- Logic ---
aprx = arcpy.mp.ArcGISProject("CURRENT")

# 1. Find the layout
layouts = aprx.listLayouts(layout_name)
if not layouts:
    arcpy.AddError(f"Could not find a layout named '{layout_name}'. Check the spelling!")
else:
    lyt = layouts[0]
    
    # Force 4x4 sizing
    lyt.pageHeight = 4
    lyt.pageWidth = 4
    
    # 2. Find the Map Frame
    mf = lyt.listElements("MAPFRAME_ELEMENT")[0]
    map_obj = mf.map
    
    # 3. Reference all 4 layers
    day_inter_lyr   = map_obj.listLayers(day_inter_name)[0]
    day_seg_lyr     = map_obj.listLayers(day_seg_name)[0]
    night_inter_lyr = map_obj.listLayers(night_inter_name)[0]
    night_seg_lyr   = map_obj.listLayers(night_seg_name)[0]
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # 4. Process Bookmarks
    bookmarks = map_obj.listBookmarks()
    arcpy.AddMessage(f"Found {len(bookmarks)} bookmarks. Starting export...")
    
    for bkmk in bookmarks:
        arcpy.AddMessage(f"Processing: {bkmk.name}")
        mf.zoomToBookmark(bkmk)
        
        # --- Daytime Export ---
        day_inter_lyr.visible   = True
        day_seg_lyr.visible     = True
        night_inter_lyr.visible = False
        night_seg_lyr.visible   = False
        
        time.sleep(0.7) 
        lyt.exportToPNG(os.path.join(output_folder, f"{bkmk.name}_Daytime.png"), 300)
        
        # --- Nighttime Export ---
        day_inter_lyr.visible   = False
        day_seg_lyr.visible     = False
        night_inter_lyr.visible = True
        night_seg_lyr.visible   = True
        
        time.sleep(0.7)
        lyt.exportToPNG(os.path.join(output_folder, f"{bkmk.name}_Overnight.png"), 300)
        
    arcpy.AddMessage("Process Complete! 4x4 PNGs generated.")
