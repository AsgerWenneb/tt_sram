
default:
	python klayout_test.py
	magic -rcfile ${PDK_ROOT}/sky130A/libs.tech/magic/sky130A.magicmagicrc -dnull -noconsole << EOF \
	gds read t.gds \
	lef write t.lef \
	EOF