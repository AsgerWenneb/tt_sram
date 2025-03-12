module my_inverter (
`ifdef USE_POWER_PINS
    inout VPWR,
    inout VGND,
`endif
    input logic A,
    input logic X
);

endmodule
