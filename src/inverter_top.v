module inverter_top(
    `ifdef USE_POWER_PINS
    inout vccd2,
    inout vssd2,
    `endif

    input logic clk,
    input logic A,
    output logic Y
);

    logic buf_out;
    logic tmp;

    inv_test buf_inst(
    `ifdef USE_POWER_PINS
        .VPWR(vccd2),
        .VGND(vssd2),
    `endif
        .A(A),
        .Y(buf_out)
    );


    assign Y = buf_out;
    // always @(posedge clk)
    // begin
    //     tmp <= buf_out;
    //     Y <= tmp;
    // end

endmodule
