module inverter_top(
    `ifdef USE_POWER_PINS
    inout vccd1,
    inout vssd1,
    `endif

    input logic A,
    output logic Y
);

    invering_buffer buf_inst(
    `ifdef USE_POWER_PINS
        .VPWR(vccd1),
        .VGND(vssd1),
    `endif
        .A(A),
        .X(Y)
    );

endmodule
