from random import randint
from manim import *

DEFAULT_PAUSE = 1

class Banner(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))

class Intro(Scene):
    """
        Scena introduttiva, utile a spiegare il problema dell'ordinamento
    """
    def construct(self):
        """
        logo = SVGMobject("./logo_TV.svg", stroke_width=0, fill_color=GREEN).scale(.4)
        firma = Tex("Alessandro Straziota").next_to(logo, LEFT)
        self.add( VGroup(logo, firma).scale(.75).to_corner(RIGHT+DOWN) )
        
        self.wait( DEFAULT_PAUSE )
        """

        circle = Circle(radius=1, color=RED_E, fill_opacity=1)
        star = Star(outer_radius=1, color=BLUE_C, fill_opacity=1)
        #array = Rectangle(width=4.0, height=2.0, grid_xstep=1.0)
        rect = Rectangle(width=1.0, height=4.0, color=ORANGE, fill_opacity=1)
        poly = RegularPolygon(n=6, start_angle=30*DEGREES, color=DARK_BLUE, fill_opacity=1)
        square = Square(side_length=2.0, color=GREEN, fill_opacity=1)
        triangle = Triangle(color=PURPLE, fill_opacity=1)

        shapes = VGroup(circle, star, rect, poly, square, triangle).arrange(buff=1).scale(.5)
        self.play( Create(shapes) )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Swap(star, triangle, run_time=.75),
            Swap(poly, square)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Swap(rect, triangle, run_time=.5),
            Swap(star, square, run_time=.75)
        )
        self.play(
            Swap(square, triangle)
        )
        self.wait( DEFAULT_PAUSE )

        sequence = Matrix(
            [[1, 2, 3, 4, 5, 6]],
            h_buff=1.35
            ).next_to(shapes, DOWN)
        self.play(FadeInFrom(sequence, DOWN))
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(shapes, shift=UP),
            sequence.animate.shift(UP*2)
            )
        self.wait( DEFAULT_PAUSE )

        sequence_medium = Matrix(
            [[randint(10,99) for _ in range(50)]],
            h_buff=.75
            ).scale(.33)
        self.play(
            ReplacementTransform(sequence, sequence_medium)
            )
        self.wait( DEFAULT_PAUSE )

        #self.play( ApplyWave(sequence_medium, amplitude=.75, run_time=2) ) 
        #self.wait( DEFAULT_PAUSE )

        sequence_long = Tex(
            "[ 68 35 44 85 55 81 84 10 65 70 60 56 93 48 94 18 89 97 14 17 88 68 24 69 48 24 59 13 62 93 44 38 54 99 44 32 76 10 94 14 81 64 41 49 75 19 25 25 35 83 ",                       
            "80 87 28 37 50 12 13 60 69 59 75 91 93 48 17 16 89 93 86 37 99 77 94 64 98 69 23 84 42 40 51 26 95 40 85 62 62 17 51 30 55 10 90 71 36 25 36 17 35 33 ",
            "49 14 35 56 31 74 89 26 87 40 59 70 69 60 25 13 11 92 94 66 27 36 96 92 11 22 46 99 97 23 51 56 12 49 77 10 32 20 38 55 61 34 58 67 66 47 29 12 29 72 ",
            "91 38 46 89 43 28 50 79 82 59 25 61 80 38 43 24 14 71 13 22 11 49 80 40 15 11 85 66 22 20 91 77 15 92 51 29 33 53 67 63 69 20 31 48 64 12 15 91 80 12 ",
            "79 47 41 71 56 15 49 76 73 71 94 21 71 23 12 14 52 65 90 87 56 34 64 49 54 63 22 12 52 15 69 54 52 75 38 59 24 94 55 74 92 17 48 28 12 31 56 36 59 19 ",
            "65 51 97 66 84 34 32 86 18 28 65 98 75 23 65 68 67 68 14 27 48 50 51 29 81 10 84 11 26 77 96 40 84 66 10 77 57 56 43 29 38 23 17 84 18 36 71 83 42 73 ",
            "98 88 35 49 51 84 97 54 58 76 72 84 25 94 87 73 80 50 23 50 93 51 76 20 27 16 11 63 55 51 29 23 17 66 80 53 26 21 28 43 72 98 40 94 29 61 82 25 70 82 ",
            "55 26 33 18 17 32 38 38 13 33 95 71 81 78 59 91 98 68 86 29 27 11 35 91 59 46 48 50 33 92 67 52 36 28 51 60 64 56 75 15 61 53 59 95 11 56 77 53 12 13 ",
            "40 72 22 52 31 71 63 25 49 77 84 44 69 15 85 74 58 57 93 17 45 21 62 29 31 78 39 65 37 77 68 70 72 13 17 18 37 62 34 31 54 64 15 49 63 67 34 35 68 46 ",
            "32 30 26 88 80 66 49 40 46 75 73 93 41 57 35 65 86 45 33 77 66 23 68 42 28 12 75 30 11 13 89 54 70 71 77 66 35 41 58 18 36 51 67 82 95 36 64 63 43 12 ",
            "60 69 53 15 72 84 85 20 57 62 30 74 55 17 11 62 95 98 43 42 85 77 16 75 84 54 33 31 77 30 61 73 13 92 71 24 22 55 50 64 13 80 75 50 16 84 ]"
        ).scale(.6)

        self.play( ReplacementTransform(sequence_medium, sequence_long) )
        self.wait( DEFAULT_PAUSE )

        self.play(ApplyWave(
            sequence_long,
            direction=RIGHT,
            time_width=0.5,
            amplitude=0.3
        ))

        self.play( ShrinkToCenter(sequence_long) )
        self.wait( DEFAULT_PAUSE )

class Explain(Scene):
    def construct(self):

        src = Matrix([[0, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9]], h_buff=.7)
        dst1 = Matrix([[0, 2, 7, 1, 7, 9, 0, 4, 6, 8, 3, 2, 0, 4, 5, 8, 5]], h_buff=.7)
        dst2 = Matrix([[7, 2, 2, 8, 4, 3, 0, 9, 0, 5, 8, 4, 0, 5, 1, 7, 6]], h_buff=.7)
        dst3 = Matrix([[2, 9, 8, 1, 7, 5, 6, 4, 2, 3, 0, 0, 0, 5, 7, 8, 4]], h_buff=.7)
        self.play( Write(src) )
        self.wait(0.5)
        # in alternatica TransformMatchingTex
        self.play( TransformMatchingShapes(src, dst1, path_arc=PI/2) )
        self.play( TransformMatchingShapes(dst1, dst2, path_arc=PI/2) )
        self.play( TransformMatchingShapes(dst2, dst3, path_arc=PI/2) )
        self.wait( DEFAULT_PAUSE )
        
        # INVERSIONE DEGLI ELEMENTI IN POSIZIONI 7 e 8

        left, right = dst3[0][:7], dst3[0][9:]
        a, b = dst3[0][7], dst3[0][8]
        self.play(
            Group(a, b).animate().scale(2),
            FadeOut(left, shift=DOWN*2),
            FadeOut(right, shift=DOWN*2)
        )
        self.wait( DEFAULT_PAUSE )

        self.play( Swap(a, b) )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Group(a, b).animate().scale(.5),
            FadeInFrom(left, DOWN*2),
            FadeInFrom(right, DOWN*2)
        )
        """
            Vettore a questo punto
            [2, 9, 8, 1, 7, 5, 6, 2, 4, 3, 0, 0, 0, 5, 7, 8, 4]
        """
        self.wait( DEFAULT_PAUSE )

        lista = [2, 9, 8, 1, 7, 5, 6, 2, 4, 3, 0, 0, 0, 5, 7, 8, 4]
        self.play( Uncreate(dst3, run_time=0) )
        self.sort_vector(lista)
        self.wait( DEFAULT_PAUSE )

    """
        Metodo che data una lista genera l'animazione
        degli step del bubble sort
    """
    def sort_vector(self, lista):

        v = Matrix([lista], h_buff=.7)
        self.add( v )
        
        n = len(lista)
        k = 0
        is_sorted = False

        while not is_sorted:
            is_sorted = True
            for i in range(n-1-k):
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    is_sorted = False
                    new_v = Matrix([lista], h_buff=.7)
                    self.play( TransformMatchingShapes(v, new_v, run_time=.4) )
                    v = new_v
            k+=1
        
        self.wait(.5)
        self.play( Indicate(v, scale_factor=1.1) )
        self.wait( DEFAULT_PAUSE )

        self.play( Unwrite( v ) )


class QuickSort(Scene):

    def construct(self):
        
        qs = Text("QuickSort", gradient=(RED, ORANGE, YELLOW)).scale(3)
        self.play(Write(qs))
        self.wait( DEFAULT_PAUSE )

        self.play(Flash(
            qs, line_length=1,
            num_lines=30, color=RED,
            flash_radius=2+SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))
        self.wait()