module inverte(
    `ifdef USE_POWER_PINS
    inout vccd1,
    inout vssd1,
    `endif

    input logic A,
    output logic Y
);
endmodule
