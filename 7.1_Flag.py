A=360; D= round(.76*A); B,C,E,F,G,H,K,L,x=(1.9*A),(7/13)*A,(0.054*A),(0.054*A),(0.063*A),(0.063*A),(0.0616*A),round((1/13)*A),D+(A/10)
import arcade ; arcade.open_window(B,A,"STARS AND STRIPES") ,arcade.set_background_color(arcade.color.WHITE), arcade.start_render()
for y_offset in range (10,A,L*2): arcade.draw_line(0, y_offset, 2*A, y_offset, (180,10,45), L)
arcade.draw_rectangle_filled(D/2,A-(C/2),D,C,(0,40,98))
while x >= D-5*(A/20):
    for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,x,(255,255,255),H*1.5)
    x-=(A/20)
    for z_offset in range(round(H*3),D,round(H*2)):arcade.draw_text("*",z_offset-(A/10),x,(255,255,255),H*1.5,)
    x-=(A/20)
    for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,x,(255,255,255),H*1.5)
arcade.finish_render() , arcade.run()
'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''








# x= D+(A/10)
# #
#
# while x >= D-3*(A/15):
    # for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,x,(255,255,255),H*1.5)
    # x-=(A/20)
    # for z_offset in range(round(H),D,round(H*2)):arcade.draw_text("*",z_offset-(A/10),x,(255,255,255),H*1.5)
    # x-=(A/20)











#
# for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,D+(A/10),(255,255,255),H*1.5)
# for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,D,(255,255,255),H*1.5)
# for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,D-(A/10),(255,255,255),H*1.5)
# for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,D-2*(A/10),(255,255,255),H*1.5)
# for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,D-3*(A/10),(255,255,255),H*1.5)
#
#
# for z_offset in range(round(H),D,round(H*2)):arcade.draw_text("*",z_offset-(A/10),D+(A/20),(255,255,255),H*1.5)
# for z_offset in range(round(H),D,round(H*2)):arcade.draw_text("*",z_offset-(A/10),D-(A/20),(255,255,255),H*1.5)
# for z_offset in range(round(H),D,round(H*2)):arcade.draw_text("*",z_offset-(A/10),D-3*(A/20),(255,255,255),H*1.5)
# for z_offset in range(round(H),D,round(H*2,)):arcade.draw_text("*",z_offset-(A/10),D-5*(A/20),(255,255,255),H*1.5)
#




# while x >= D-5*(A/20):
#     for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,x,(255,255,255),H*1.5)
#     x-=(A/20)
#     for z_offset in range(round(H),D,round(H*2)):arcade.draw_text("*",z_offset-(A/10),x,(255,255,255),H*1.5,)
#     x-=(A/20)
#     for z_offset in range(round(H/2),D,round(H*2)):arcade.draw_text("*",z_offset,x,(255,255,255),H*1.5)
# arcade.finish_render() , arcade.run()
