module hello_inverter_top(
    `ifdef USE_POWER_PINS
    inout vccd1,
    inout vssd1,
    `endif

    input logic clk,
    input logic A,
    output logic Y
);

    hello_inverter buf_inst(
    `ifdef USE_POWER_PINS
        .VPWR(vccd1),
        .VGND(vssd1),
    `endif
        .A(A),
        .Y(Y)
    );

endmodule
