module sram16_top(
    `ifdef USE_POWER_PINS
    inout vccd1,
    inout vssd1,
    `endif

    input wire clk,
    input wire  [11:0]  addr,
    input wire  [31:0]  wdata,
    input wire          cs,
    input wire  [3:0]   wen,

    output wire [31:0]  rdata
);
    SRAM16K buf_inst(
    `ifdef USE_POWER_PINS
        .VPWR(vccd1),
        .VGND(vssd1),
    `endif
        .clk(clk),
        .addr(addr),
        .wdata(wdata),
        .cs(cs),
        .wen(wen),

        .rdata(rdata)
    );

endmodule
