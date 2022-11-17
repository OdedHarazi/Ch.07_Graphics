import arcade
#Sign your name:Oded 11.11.2022

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

arcade.open_window(500,400,"Oded Drawing")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

#vertical lines
for x_offset in range (0,501,20):
    arcade.draw_line(x_offset, 0, x_offset, 500, arcade.color.BLACK,2)

#horizontal lines
for y_offset in range (0,401,20):
    arcade.draw_line(0, y_offset, 600, y_offset, arcade.color.BLACK,2)

#pink rectangle
arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)

#purple circle
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)

#Slanted Brick
arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,135)

#Text
arcade.draw_text("I love you. I know.",20,160,arcade.color.BRICK_RED,20)


#Line
arcade.draw_line(80,20,120,60,arcade.color.BLUE,1)

#Oval
arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)

#Small Red Square
arcade.draw_rectangle_filled(460,10,5,5,arcade.color.RED)
#
#Pac-Man
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)

arcade.finish_render()
arcade.run()
