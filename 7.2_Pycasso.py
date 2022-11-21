'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''


import arcade ; arcade.open_window(500,500, "Amongaso") ,arcade.set_background_color(arcade.color.EERIE_BLACK), arcade.start_render()


x=-75
a=255
b=0
c=0
while x<=200:
    arcade.draw_circle_filled(x+250,250,50,(a,b,c),)
    arcade.draw_ellipse_filled(x+204,203,15,130,(a,b,c),)
    arcade.draw_ellipse_filled(x+288,200,20,80,(a,b,c),)
    arcade.draw_ellipse_filled(x+245,175,25,90,(a,b,c),100,)
    arcade.draw_ellipse_filled(x+270,250,40,80,arcade.color.COOL_GREY,90,)
    arcade.draw_ellipse_filled(x+270,255,40,80,arcade.color.COOL_GREY,90,)
    arcade.draw_ellipse_filled(x+270,260,40,80,arcade.color.COOL_GREY,90,)
    arcade.draw_rectangle_filled(x+245,200,95,60,(a,b,c),)
    arcade.draw_ellipse_outline(x+270,255,53,83,arcade.color.BLACK,3,90,)
    arcade.draw_rectangle_filled(x+195,212,15,54,(a,b,c),)
    arcade.draw_circle_filled(x+203,242,15,(a,b,c),)
    arcade.draw_circle_filled(x+202,192,15,(a,b,c),)

    arcade.draw_rectangle_filled(x+225,160,32.5,40,(a,b,c),)
    arcade.draw_ellipse_filled(x+221.5,145,30,37.5,(a,b,c),90,)

    arcade.draw_rectangle_filled(x+275,160,37.5,40,(a,b,c),355)
    arcade.draw_ellipse_filled(x+276.5,145,30,37.5,(a,b,c),85,)
    arcade.draw_text("AMONGASO",100,375,arcade.color.GREEN,30)
    arcade.draw_text("Oded's",100,425,arcade.color.PINK_SHERBET,15)
    arcade.draw_text("WHO IS THE IMPOSTER???",120,65,arcade.color.YELLOW,15)

    x+=200
    a=0
    c=255

arcade.finish_render(),arcade.run()



# arcade.draw_parabola_outline(227,225,263,30,arcade.color.BLACK,10,90,)
# arcade.draw_parabola_outline(277,225,313,30,arcade.color.BLACK,10,270,)
# arcade.draw_parabola_outline(232,230,310,32.5,arcade.color.BLACK,10,)
# arcade.draw_parabola_outline(232,217,310,30,arcade.color.BLACK,10,180)

# arcade.draw_line(200,250,200,125,arcade.color.RED,3)
