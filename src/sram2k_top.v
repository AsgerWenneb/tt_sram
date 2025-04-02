module sram2k_top(
    `ifdef USE_POWER_PINS
    inout vccd1,
    inout vssd1,
    `endif

  input logic clk0, // clock
  input logic csb0, // active low chip select
  input logic web0, // active low write control
  input logic [3:0]   wmask0, // write mask
  input logic [8:0]  addr0,
  input logic [31:0]  din0,
  output logic [31:0] dout0,
  input logic clk1, // clock
  input logic csb1, // active low chip select
  input logic [8:0]  addr1,
  output logic [31:0] dout1
);
    sky130_sram_2kbyte_1rw1r_32x512_8 buf_inst(
    `ifdef USE_POWER_PINS
        .vccd1(vccd1),
        .vssd1(vssd1),
    `endif
        .clk0(clk0),
        .csb0(csb0),
        .web0(web0),
        .wmask0(wmask0),
        .addr0(addr0),
        .din0(din0),
        .clk1(clk1),
        .csb1(csb1),
        .addr1(addr1),
        .dout1(dout1)
    );

endmodule
