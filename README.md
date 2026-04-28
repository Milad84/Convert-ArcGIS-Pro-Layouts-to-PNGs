# Convert-ArcGIS-Pro-Layouts-to-PNGs
This script implemented in an ArcGIS Pro Toolbox converts a layout to multiple PNGs based on bookmarked views

This repository contains a Python script and documentation for automating map layout exports in ArcGIS Pro. It is specifically designed to handle "Day vs. Night" visibility toggles across multiple bookmarks.

## 🛠️ Implementation Instructions

### 1. Create the Script Tool
* In the **Catalog** pane, right-click your Toolbox (`.atbx`).
* Select **New > Script**.
* **General Tab:** Name it `ExportDayNightPNGs` and point to your `.py` file.

### 2. Configure Parameters
Set these in the **Parameters** tab in this exact order:
1. **Output Folder** (Folder)
2. **Layout Name** (Layout)
3. **Day Intersection Layer** (Layer)
4. **Day Segment Layer** (Layer)
5. **Night Intersection Layer** (Layer)
6. **Night Segment Layer** (Layer)

## 🧠 Code Logic Summary

The script automates the following workflow:
1.  **Validation:** It references the active ArcGIS Pro project and ensures the specified Layout exists.
2.  **Formatting:** It forces the layout page size to **4x4 inches** to ensure consistency across exports.
3.  **Layer Control:** It locates the Map Frame and establishes pointers to the four specific layers (Intersections and Segments for both Day and Night).
4.  **The Loop:** For every bookmark in the map:
    * It zooms the view to that bookmark.
    * It turns "Day" layers ON and "Night" layers OFF, then exports `[BookmarkName]_Daytime.png`.
    * It turns "Day" layers OFF and "Night" layers ON, then exports `[BookmarkName]_Overnight.png`.
5.  **Performance:** It includes a 0.7-second pause (`time.sleep`) between visibility changes and exports to ensure the ArcGIS Pro engine has finished rendering before the file is saved.
<img width="311" height="665" alt="image" src="https://github.com/user-attachments/assets/5e37a08e-a3e8-483a-b6d9-ed872aca362a" />
