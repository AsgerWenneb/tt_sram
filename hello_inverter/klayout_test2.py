import pya
import os

pdk_root = os.environ['PDK_ROOT']

# lyp location;
lyp_loc = os.path.join(pdk_root, "sky130B", "libs.tech", "klayout", "tech", "sky130B.lyp")

# lyc location
lyt_loc = os.path.join(pdk_root, "sky130B", "libs.tech", "klayout", "tech", "sky130B.lyt")

layout = pya.Layout()
top = layout.create_cell("TOP")
layermap = layout.read(lyp_loc)
print(layermap)
