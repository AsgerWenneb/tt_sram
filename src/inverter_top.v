module inverter_top(
    `ifdef USE_POWER_PINS
    inout vccd1,
    inout vssd1,
    `endif

    input logic clk,
    input logic A,
    output logic Y
);

    logic buf_out;
    logic tmp;

    sky130_inv buf_inst(
    `ifdef USE_POWER_PINS
        .VPWR(vccd1),
        .VGND(vssd1),
    `endif
        .A(A),
        .Y(buf_out)
    );


    always @(posedge clk)
    begin
        tmp <= buf_out;
        Y <= tmp;
    end

endmodule
