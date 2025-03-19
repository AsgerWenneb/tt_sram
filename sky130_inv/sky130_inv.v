module sky130_inv(
    `ifdef USE_POWER_PINS
    inout VPWR,
    inout VGND,
    `endif

    input logic A,
    output logic Y
);
endmodule
