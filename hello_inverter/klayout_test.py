# Python version:

import pya
import os

pdk_root = os.environ['PDK_ROOT']

# lyp location;
lyp_loc = os.path.join(pdk_root, "sky130B", "libs.tech", "klayout", "tech", "sky130B.lyp")

# lyc location
lyt_loc = os.path.join(pdk_root, "sky130B", "libs.tech", "klayout", "tech", "sky130B.lyt")

print(lyp_loc)
# klayout -e -nn $PDK_ROOT/sky130A/libs.tech/klayout/tech/sky130A.lyt
# $PDK_ROOT/sky130A/libs.tech/klayout/tech/sky130A.lyp

## $PDK_ROOT/sky130A/libs.tech/klayout/tech/sky130A.ly

lw = pya.LayoutView()
lw.load_layer_props(lyp_loc)
i = 0
for layer in lw.each_layer():
    print(f"Layer number {i}: {layer.name} ID: {layer.source_layer_(True)} {layer.source_datatype_(True)}")
    i += 1
    #print("Layer handle " + str(layer) + " refers to " ) # + str(lw.get_info(layer))

# Load the technology file
#tech = pya.Technology()
#tech.load(lyt_loc)

#print(tech.component_names())
# Load the technology into KLayout

layout = pya.Layout()
top = layout.create_cell("t")
m1 = layout.layer(68, 20) # metal1
m1label = layout.layer(68, 5) # metal1 label

m2 = layout.layer(69, 20) # metal2
m2pin = layout.layer(69, 16) # metal2 pin
m2label = layout.layer(69, 5) # metal2 label

via2 = layout.layer(69, 44) # via2

m3 = layout.layer(70, 20) # metal3
via3 = layout.layer(70, 44) # via3

m4 = layout.layer(71, 20) # metal4
m4pin = layout.layer(71, 16) # metal4 pin
m4label = layout.layer(71, 5) # metal4 label

via1 = layout.layer(68, 44) # via1


m1pin = layout.layer(68,16)

bd = layout.layer(235, 4) # boundary

mc = layout.layer(81, 2) # memcore

li1 = layout.layer(67, 20)
li1pin = layout.layer(67, 16)

mcon1 = layout.layer(67, 44)


# Loading can probably be done better with 	merge_meta_info (Layout class) or similar.

# Bounding box
top.shapes(bd).insert(pya.Box(0, 0, 10000, 5000))
top.shapes(mc).insert(pya.Box(0, 0, 10000, 5000))

# Metal1 layer with interconnect
top.shapes(m1).insert(pya.Box(0, 0, 1000, 2000))
top.shapes(m1pin).insert(pya.Box(0, 0, 1000, 2000))
top.shapes(m2).insert(pya.Box(0, 0, 1000, 2000))
top.shapes(m2pin).insert(pya.Box(0, 0, 1000, 2000))
top.shapes(via1).insert(pya.Box(100, 100, 900, 1900))


top.shapes(m1).insert(pya.Box(8000, 0, 10000, 2000))
top.shapes(m1pin).insert(pya.Box(8000, 0, 10000, 2000))
top.shapes(m2).insert(pya.Box(8000, 0, 10000, 2000))
top.shapes(m2pin).insert(pya.Box(8000, 0, 10000, 2000))
top.shapes(via1).insert(pya.Box(8100, 100, 9900, 1900))

top.shapes(m1).insert(pya.Box(8000, 3000, 10000, 5000))
top.shapes(m1pin).insert(pya.Box(8000, 3000, 10000, 5000))
top.shapes(m2).insert(pya.Box(8000, 3000, 10000, 5000))
#top.shapes(m2pin).insert(pya.Box(8000, 3000, 10000, 5000))
top.shapes(via1).insert(pya.Box(8100, 3100, 9900, 4900))
top.shapes(via2).insert(pya.Box(8100, 3100, 9900, 4900))
top.shapes(m3).insert(pya.Box(8000, 3000, 10000, 5000))
top.shapes(via3).insert(pya.Box(8100, 3100, 9900, 4900))
top.shapes(m4).insert(pya.Box(8000, 3000, 10000, 5000))
top.shapes(m4pin).insert(pya.Box(8000, 3000, 10000, 5000))
#top.shapes(m4label).insert(pya.Box(8000, 3000, 10000, 5000))


top.shapes(m1).insert(pya.Box(0, 3000, 1000, 5000))
top.shapes(m1pin).insert(pya.Box(0, 3000, 1000, 5000))
top.shapes(m2).insert(pya.Box(0, 3000, 1000, 5000))
#top.shapes(m2pin).insert(pya.Box(0, 3000, 1000, 5000))
top.shapes(via1).insert(pya.Box(100, 3100, 900, 4900))
top.shapes(via2).insert(pya.Box(100, 3100, 900, 4900))
top.shapes(m3).insert(pya.Box(0, 3000, 1000, 5000))
top.shapes(via3).insert(pya.Box(100, 3100, 900, 4900))
top.shapes(m4).insert(pya.Box(0, 3000, 1000, 5000))
top.shapes(m4pin).insert(pya.Box(0, 3000, 1000, 5000))



top.shapes(li1).insert(pya.Box(8000, 3000, 10000, 5000))
top.shapes(mcon1).insert(pya.Box(8100, 3100, 9900, 4900))
#top.shapes(li1pin).insert(pya.Box(8000, 3000, 10000, 5000))

top.shapes(li1).insert(pya.Box(0, 3000, 1000, 5000))
top.shapes(mcon1).insert(pya.Box(100, 3100, 900, 4900))
#top.shapes(li1pin).insert(pya.Box(0, 3000, 1000, 5000))



pin_pos = pya.Point(500, 500)  # in database units (e.g., nm)
pin_box = pya.Box(pin_pos - pya.Point(50, 50), pin_pos + pya.Point(50, 50))  # 100x100 box

pin_pos2 = pya.Point(8500, 500)  # in database units (e.g., nm)
pin_box2 = pya.Box(pin_pos2 - pya.Point(50, 50), pin_pos2 + pya.Point(50, 50))  # 100x100 box

# Add metal shape
top.shapes(m1).insert(pin_box)
top.shapes(m1).insert(pin_box2)

# Add text label at the center of the box
text = pya.Text("A", pya.Trans(pin_pos))
top.shapes(m2label).insert(text)

text = pya.Text("Y", pya.Trans(pin_pos2))
top.shapes(m2label).insert(text)

pin_pos3 = pya.Point(500, 3500)
text = pya.Text("VPWR", pya.Trans(pin_pos3))
top.shapes(m4label).insert(text)

pin_pos4 = pya.Point(8500, 3500)
text = pya.Text("VGND", pya.Trans(pin_pos4))
top.shapes(m4label).insert(text)
#top.shapes(li1).insert(text)

# Add pin label

layout.write("t.gds")
print("Completed layout creation.")
