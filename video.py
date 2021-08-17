from random import randint
from manim import *
import numpy as np

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
        #self.play(FadeInFrom(sequence, DOWN))   ###
        self.play(FadeIn(sequence, shift=UP))
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
            #FadeInFrom(left, DOWN*2),
            #FadeInFrom(right, DOWN*2)
            FadeIn(left, shift=UP),
            FadeIn(right, shift=UP)
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

        self.play(
            Flash(
                qs, line_length=1,
                num_lines=30, color=RED,
                flash_radius=2+SMALL_BUFF,
                time_width=0.3, run_time=2,
                rate_func = rush_from
                )
            )
        self.wait()

        ran = Text("Random", gradient=(PURPLE, BLUE, GREEN)).scale(3).next_to(qs, UP)
        self.play(
            qs.animate().shift(DOWN),
            #FadeInFrom(ran, DOWN)
            FadeIn(ran, shift=UP)
            )
        self.wait( DEFAULT_PAUSE )

        self.play(Unwrite(qs), Unwrite(ran))
        self.wait( DEFAULT_PAUSE )

        v = Matrix([[2, 9, 8, 1, 7, 5, 6, 4, 2, 3, 0, 0, 0, 5, 7, 8, 4]], h_buff=.7)
        self.play( GrowFromCenter(v) )
        self.wait( DEFAULT_PAUSE )

        pivot = v[0][7]
        left, right = v[0][:7], v[0][8:]

        left.save_state()   # salvo lo stato per fare il RESTORE dopo
        right.save_state()  # salvo lo stato per fare il RESTORE dopo

        self.play(
            left.animate().scale(.9).set_opacity(.5),
            right.animate().scale(.9).set_opacity(.5),
            pivot.animate().scale(2)
        )
        self.wait( DEFAULT_PAUSE )

        piv = Text("Pivot", color=ORANGE ).next_to(pivot, UP)
        self.play(
            #FadeInFrom(piv, DOWN),
            FadeIn(piv, shift=UP),
            pivot.animate().set_color(ORANGE)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(piv, shift=UP),
            Restore(left),
            Restore(right),
            pivot.animate().scale(.5)
        )
        self.wait( DEFAULT_PAUSE )

        a, b = v[0][6], v[0][8]
        arrow_b2a = Arrow(
            max_tip_length_to_length_ratio=.2,
            start=b.get_center()+UP*.5,
            end=a.get_center()+UP*.5
            )
        arrow_a2b = Arrow(
            max_tip_length_to_length_ratio=.2,
            start=a.get_center()+DOWN*.5,
            end=b.get_center()+DOWN*.5
            )        


        self.play( Indicate( b ), run_time=1 )
        #self.play( VFadeInThenOut( arrow_b2a ), run_time=3 )
        self.play( GrowArrow(arrow_b2a) )
        self.play( FadeOut(arrow_b2a, shift=LEFT*4) )
        self.wait()

        self.play( Indicate( a ), run_time=1 )
        #self.play( VFadeInThenOut( arrow_b2a ), run_time=3 )
        self.play( GrowArrow(arrow_a2b) )
        self.play( FadeOut(arrow_a2b, shift=RIGHT*4) )
        self.wait( DEFAULT_PAUSE )

        self.play( Swap(a, b), run_time=2 )
        self.wait( DEFAULT_PAUSE )

        a, b = v[0][5], v[0][9]
        self.play(
            Indicate(a),
            Indicate(b),
            run_time=2
            )
        self.wait()
        self.play( Swap(a, b), run_time=2 )
        self.wait()
        a, b = v[0][4], v[0][10]
        self.play(
            Indicate(a),
            Indicate(b),
            run_time=1
            )
        self.wait()
        self.play( Swap(a, b), run_time=1 )
        self.wait( DEFAULT_PAUSE )

        new_v = Matrix([[2, 9, 8, 1, 0, 3, 2, 4, 6, 5, 7, 0, 0, 5, 7, 8, 4]], h_buff=.7)
        new_v[0][7].set_color(ORANGE)
        self.play( Uncreate(v), run_time=0 )
        self.add( new_v )
        v = new_v
        left, right = v[0][:7], v[0][8:]

        brace_left = BraceLabel(left, "\\leq 4", UP).shift(UP*.5)
        brace_right = BraceLabel(right, "> 4", UP).shift(UP*.5)

        self.play(
            Group(left, right).animate().shift( UP*.5 ),
            #FadeInFrom(brace_left, DOWN),
            #FadeInFrom(brace_right, DOWN)
            FadeIn(brace_left, shift=UP),
            FadeIn(brace_right, shift=UP)
        )
        self.wait( DEFAULT_PAUSE )

        new_v = Matrix([[2, 0, 0, 4, 1, 0, 3, 2, 4, 6, 5, 7, 5, 7, 8, 8, 9]], h_buff=.7)
        new_v[0][8].save_state()
        new_v[0][8].set_color(ORANGE)

        new_brace_left = BraceLabel(new_v[0][:8], "\\leq 4", UP)
        new_brace_right = BraceLabel(new_v[0][9:], "> 4", UP)

        self.play( 
            TransformMatchingShapes(v, new_v),
            Transform(brace_left, new_brace_left),
            Transform(brace_right, new_brace_right),
            run_time=2
            )
        v = new_v
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(Group(brace_left, brace_right), shift=UP),
            Restore(new_v[0][8])
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Circumscribe(v[0][:8], fade_out=True, time_width=1, run_time=2)
        )
        self.wait()
        new_v = Matrix([[2, 0, 0, 4, 1, 0, 3, 2]], h_buff=1.5)
        self.play(
            TransformMatchingShapes(v, new_v)
        )
        v = new_v
        self.wait( DEFAULT_PAUSE )

        self.play(
            v[0][4].animate().scale(1.5).set_color(ORANGE)
        )
        self.wait()
        self.play(
            Swap(v[0][0], v[0][5]),
            Swap(v[0][4], v[0][3], run_time=.75)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Circumscribe(Group(v[0][3], v[0][-1]), fade_out=True, time_width=1, run_time=2)
        )
        self.wait()
        new_v = Matrix([[4, 2, 3, 2]], h_buff=2)
        self.play(
            TransformMatchingShapes(v, new_v)
        )
        v = new_v
        self.wait( DEFAULT_PAUSE )

        v[0][1].save_state()
        self.play( v[0][1].animate().scale(1.5).set_color(ORANGE) )
        self.wait()
        self.play( Swap(v[0][0], v[0][-1]) )
        self.wait()
        sor = Tex("Stop! It's sorted.").next_to(v, UP*1.5)
        self.play(
            Restore(v[0][1]),
            #FadeInFrom(sor, DOWN)
            FadeIn(sor, shift=UP)
        )
        self.wait( 1 )
        self.play( FadeOut(sor, shift=UP*1.5) )
        self.wait( DEFAULT_PAUSE )

        came_back = Text("Came back").to_edge(DOWN)
        new_v = Matrix([[0, 0, 0, 1, 2, 2, 3, 4]], h_buff=1.5)
        self.play(
            TransformMatchingShapes(v, new_v),
            #FadeInFrom(came_back, DOWN)
            FadeIn(came_back, shift=UP)
        )
        self.play( FadeOut(came_back, shift=DOWN) )
        v = new_v
        self.wait( DEFAULT_PAUSE )

        sor = BraceText(v[0][:3], "Already sorted")
        self.play(
            Circumscribe(v[0][:3],fade_out=True, time_width=1, run_time=2),
            #FadeInFrom(sor, UP*.5)
            FadeIn(sor, shift=DOWN*.5)
        )
        self.play( FadeOut(sor, shift=UP*.5) )
        self.wait()

        sor = BraceText(v[0][:], "Sorted")
        self.play(
            Circumscribe(v[0][:],fade_out=True, time_width=1, run_time=2),
            #FadeInFrom(sor, UP*.5)
            FadeIn(sor, shift=DOWN*.5)
        )
        self.play( FadeOut(sor, shift=UP*.5) )
        self.wait( DEFAULT_PAUSE )

        new_v = Matrix([[0, 0, 0, 1, 2, 2, 3, 4, 4, 6, 5, 7, 5, 7, 8, 8, 9]], h_buff=.7)
        self.play(
            TransformMatchingShapes(v, new_v),
            #FadeInFrom(came_back, DOWN)
            FadeIn(came_back, shift=UP)
        )
        self.play( FadeOut(came_back, shift=DOWN) )
        v = new_v
        self.wait( DEFAULT_PAUSE )

        repeat = Tex("Let's repeat on the right side").set_color(YELLOW).shift(UP*.5).scale(1.5)
        v.save_state()
        self.play(
            GrowFromCenter(repeat),
            v.animate().set_opacity(.3).scale(.75)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(repeat),
            Restore(v)
        )
        self.wait()

        self.play(
            Circumscribe(v[0][9:], fade_out=True, time_width=1, run_time=2)
        )
        self.wait()

        new_v = Matrix([[6, 5, 7, 5, 7, 8, 8, 9]], h_buff=1.5)
        self.play(
            TransformMatchingShapes(v, new_v)
        )
        v = new_v
        self.wait()

        self.play(
            v[0][2].animate().scale(1.5).set_color(ORANGE)
        )
        self.wait()
        self.play( Swap(v[0][2], v[0][3]) )
        self.wait()

        self.play( Circumscribe(Group(v[0][0], v[0][3]), fade_out=True, time_width=1, run_time=2) )
        new_v = Matrix([[6, 5, 5]], h_buff=2)
        self.play(
            TransformMatchingShapes(v, new_v)
        )
        v = new_v
        self.wait()
        self.play(
            v[0][1].animate().scale(1.5).set_color(ORANGE)
        )
        self.wait()
        self.play( Swap(v[0][0], v[0][2]) )
        self.wait()

        sor = BraceText(v[0][:], "Sorted")
        #self.play( FadeInFrom(sor, UP) )
        self.play( FadeIn(sor, shift=DOWN) )
        self.wait()

        new_v = Matrix([[5, 5, 6, 7, 7, 8, 8, 9]], h_buff=1.5)
        self.play(
            TransformMatchingShapes(v, new_v),
            FadeOut(sor, shift=UP)
        )
        v = new_v
        self.wait()

        sor = BraceText(v[0][4:], "Already sorted")
        #self.play( FadeInFrom(sor, UP) )
        self.play( FadeIn(sor, shift=DOWN) )
        self.wait()

        sor2 = BraceText(v[0][:], "Sorted", brace_direction=UP)
        self.play(
            #FadeInFrom(sor2, DOWN),
            FadeIn(sor2, shift=UP),
            FadeOut(sor, shift=UP)
        )
        self.wait()
        
        new_v = Matrix([[0, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9]], h_buff=.7)
        self.play(
            TransformMatchingShapes(v, new_v),
            FadeOut(sor2, shift=DOWN)
        )
        v = new_v
        self.wait()

        sor = Tex("Sorted :)").scale(1.3).next_to(v, UP*1.5)
        self.play(
            #FadeInFrom(sor, DOWN),
            FadeIn(sor, shift=UP),
            Flash(
                sor, line_length=1, num_lines=20,
                flash_radius=sor.width+SMALL_BUFF,
                run_time=2
                )
        )
        self.play(
            Flash(
                sor, line_length=1, num_lines=20,
                flash_radius=sor.width+SMALL_BUFF,
                run_time=2
                )
        )
        self.wait( DEFAULT_PAUSE )

        self.play( Unwrite(v), FadeOut(sor) )
        self.wait( DEFAULT_PAUSE )


class CodeRandomQuickSort(Scene):
    def construct(self):
        randomqs_code = Code(
            "RandomQuickSort.py",
            tab_width=4,
            background_stroke_color=WHITE,
            insert_line_no=False,
            style=Code.styles_list[1],  # emacs
            background="window",
            language="python",
            font="Monospace",
            generate_html_file=True
            ).scale(.85)
        self.add(randomqs_code)
        self.wait( 10 )

class Analisi(Scene):
    def construct(self):

        warning = Text(
            "Warning: Danger zone, math's area!",
            t2c={"Warning:":RED},
            font="Monospace",
            weight=BOLD
            ).scale(.9)
        
        self.play( Write( warning ) )
        self.play(
            Wiggle(warning[:7], scale_value=1.25,),
            Wiggle(warning[19:23], scale_value=1.5, run_time=1.75, n_wiggles=5)
            )
        self.wait( DEFAULT_PAUSE )

        self.play( FadeOut(warning, shift=RIGHT*10) )
        self.wait( DEFAULT_PAUSE )

        questions = BulletedList("Why Random?", "How fast is Random Quick Sort?")\
                    .set_opacity(0.5).scale(1.3).to_edge(LEFT)
        self.play( Write(questions) )
        self.wait( DEFAULT_PAUSE )

        self.play( questions[0].animate().set_opacity(1) )
        self.wait( DEFAULT_PAUSE )

        ans1 = Tex("$\\rightarrow$ choose uniformly at random the \\textit{pivot}").next_to(questions[0])
        # self.play( FadeInFrom(ans1, LEFT) )
        self.play( FadeIn(ans1, shift=RIGHT) )
        self.wait( DEFAULT_PAUSE )

        self.play( questions[1].animate().set_opacity(1) )
        self.wait( DEFAULT_PAUSE )

        ans2 = VGroup(
            Tex("$\\downarrow$"),
            Tex("Time ", "$\\rightarrow$", " n° of switch sides ", "$\\rightarrow$", " n° comparisons with \\textit{pivot}")
            ).arrange(DOWN).next_to(questions[1], DOWN).shift(RIGHT*2)
        self.play(
            # FadeInFrom(ans2, UP)
            FadeIn(ans2, shift=DOWN)
        )
        self.wait( DEFAULT_PAUSE )

        rect = SurroundingRectangle(ans2[1][0])
        self.play( Create( rect ) )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                rect,
                SurroundingRectangle(ans2[1][2])
            )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                rect,
                SurroundingRectangle(ans2[1][4])
            )
        )
        self.wait( DEFAULT_PAUSE )


        self.play( Unwrite(questions), Unwrite(ans1), Unwrite(ans2), Uncreate(rect) )
        self.wait( DEFAULT_PAUSE )

        """
            [0, 1, 4, 6, 7, 9, 12, 13, 21]
             0  1  2  3  4  5   6   7   8 
        """
        v = Matrix([[0, 1, 4, 6, 7, 9, 12, 13, 21]], h_buff=1.5)
        self.play( Write( v ) )
        self.wait()

        y = Matrix(
            [["y_0", "y_1", "y_2", "y_3", "y_4", "y_5", "y_6", "y_7", "y_8"]],
            h_buff=1.5
        ).next_to(v, DOWN*2)
        arrows = VGroup(*[Arrow(start=config.top-UP, end=ORIGIN+UP) for _ in range(9)]).arrange(buff=1.15)
        self.play(
            v.animate().shift(UP*2),
            # FadeInFrom(y, UP),
            FadeIn(y, shift=DOWN),
            *[GrowArrow(a) for a in arrows]
        )
        self.play(
            FadeOut(arrows, shift=DOWN)
        )
        self.wait()

        new_v = Matrix([[6, 0, 13, 9, 7, 12, 21, 1, 4]], h_buff=1.5)
        new_y = Matrix(
            [["y_3", "y_0", "y_7", "y_5", "y_4", "y_6", "y_8", "y_1", "y_2"]],
            h_buff=1.5
        ).next_to(new_v, DOWN*2)
        new_v.shift(UP*2)
        
        self.play(
            TransformMatchingShapes(v, new_v),
            TransformMatchingShapes(y, new_y)
            )
        v = new_v
        y = new_y
        self.wait( DEFAULT_PAUSE )

        brace_y = Brace(y[0][:], UP)
        brace_v = Brace(v[0][:], DOWN)
        t = Text("Same order").shift(UP*.5)

        self.play(
            # FadeInFrom(brace_v, UP),
            # FadeInFrom(brace_y, DOWN),
            FadeIn(brace_v, shift=DOWN),
            FadeIn(brace_y, shift=UP),
            GrowFromCenter(t)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(brace_v, shift=UP),
            FadeOut(brace_y, shift=DOWN),
            ShrinkToCenter(t)
        )
        self.wait( DEFAULT_PAUSE )

        a_v, a_y = v[0][0], y[0][0]
        b_v, b_y = v[0][4], y[0][4]

        self.play(
            Indicate(a_v, scale_factor=2, color=ORANGE),
            Indicate(a_y, scale_factor=2, color=ORANGE),
            run_time=2
        )
        self.wait()
        self.play(
            Indicate(b_v, scale_factor=2, color=BLUE),
            Indicate(b_y, scale_factor=2, color=BLUE),
            run_time=2
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Swap(a_v, b_v, run_time=2),
            Swap(a_y, b_y, run_time=2)
        )
        self.wait( DEFAULT_PAUSE )

        v.save_state()
        y.save_state()
        statement1 = MathTex("i < j").scale(2)
        statement2 = MathTex("\\Longrightarrow y_i \\leq y_j").scale(2).shift(RIGHT*2)
        self.play(
            FadeOut(v),
            FadeOut(y),
            Write(statement1)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            statement1.animate().shift(LEFT*2),
            FadeIn(statement2, shift=RIGHT)    ###
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(statement1),
            FadeOut(statement2),
            Restore(v),
            Restore(y)
        )
        self.wait( DEFAULT_PAUSE )

        g = VGroup(y[0][5].copy(), y[0][6].copy())
        self.play(
            g.animate().shift(UP*1.5)
        )
        self.wait()
        leq_1 = MathTex("\\leq").set_x(g.get_center()[0]).set_y(g.get_center()[1])
        leq_2 = MathTex("\\leq").set_x(v[0][5:7].get_center()[0]).set_y(v[0][5:7].get_center()[1])
        self.play( Write(leq_1) )
        self.wait()
        self.play( Write(leq_2) )
        self.wait( DEFAULT_PAUSE )

        self.play( Indicate(VGroup(g, leq_1)) )
        self.play( Indicate(VGroup(v[0][5:7], leq_2)) )
        self.wait( DEFAULT_PAUSE )

        self.play( Unwrite(g), Unwrite(leq_1), Unwrite(leq_2) )
        self.wait( DEFAULT_PAUSE )

        Y = Matrix([["y_1", "y_2", "y_3", "\\cdots", "y_i", "\\cdots", "y_j", "\\cdots", "y_n",]])
        self.play(
            #Transform(y, Y),
            TransformMatchingShapes(y, Y),
            FadeOut(v)
        )
        self.wait( DEFAULT_PAUSE )
        
        yi, yj = Y[0][4].copy(), Y[0][6].copy()
        Y.save_state()
        self.play(
            Y[0][4].animate().scale(1.2).set_color( ORANGE ),
            Y[0][6].animate().scale(1.2).set_color( ORANGE )
        )
        self.wait()
        self.play(
            Restore(Y),
            yi.animate().set_color( WHITE ).shift( UP + RIGHT*.5 ),
            yj.animate().set_color( WHITE ).shift( UP + LEFT*.5 ),
        )
        self.wait( DEFAULT_PAUSE )

        g = VGroup(yi, yj)
        leq = MathTex("\\stackrel{\\text{?}}{\\leq}").set_x(g.get_center()[0]).set_y(g.get_center()[1]+UP[1]*.1).scale(.75)
        brace = BraceText(g, "Will they ever be compared?", brace_direction=UP).shift(UP*.2)
        self.play(
            FadeIn(brace, shift=UP),
            Write( leq )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(brace, shift=UP),
            Unwrite( leq ),
            Unwrite(Y, run_time=.75),
            Transform(g, MathTex("y_i, y_j"), run_time=1.5)
        )
        self.wait( DEFAULT_PAUSE )

class Analisi_2(Scene):
    def construct(self):
        
        X = MathTex("y_i, y_j")
        self.add( X )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(X, MathTex("1 \\leq i < j \\leq n"))
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(X, MathTex("X_{i, j}"))
        )
        self.wait( DEFAULT_PAUSE )
        
        brace = BraceText(X, "random variable", brace_direction=RIGHT)
        self.play(
            FadeIn(brace, shift=RIGHT)
        )
        self.wait( DEFAULT_PAUSE )

        eq1 = _eq, _1 = Tex("$=$ ","$1$").next_to(X, RIGHT)
        self.play(
            FadeOut(brace, shift=UP),
            FadeIn(eq1, shift=UP)
        )
        self.wait( DEFAULT_PAUSE )

        _0 = Tex("$0$").move_to(_1)
        self.play(
            FadeOut(_1, shift=UP),
            FadeIn(_0, shift=UP)
        )
        self.wait( DEFAULT_PAUSE )

        brace = BraceText(Group(X, eq1), "if $y_i$ and $y_j$ are compared\\\\at any time", brace_direction=DOWN)
        self.play(
            FadeOut(_0, shift=DOWN),
            FadeIn(_1, shift=DOWN),
            FadeIn(brace, shift=DOWN)
        )
        self.wait( DEFAULT_PAUSE )

        brace2 = BraceText(Group(X, eq1), "otherwise", brace_direction=DOWN)
        self.play(
            FadeOut(_1, shift=UP),
            FadeIn(_0, shift=UP),
            TransformMatchingShapes(
                brace,
                brace2
            )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Unwrite( _eq ),
            Unwrite( _0 ),
            Unwrite( brace2 )
        )
        self.wait( DEFAULT_PAUSE )

        tot = Tex("Total number of comparison =").shift(UP)
        Xs = MathTex("X_{1,2} + X_{1,3} + \\cdots X_{1,n} + X_{2,3} + X_{2,4} + \\cdots + X_{2,n} + \\cdots X_{n-1, n}")
        self.play(
            GrowFromCenter( tot ),
            Transform(X, Xs)
        )
        self.wait( DEFAULT_PAUSE )

        s = Tex("for all $1 \\leq i < j \\leq n$").shift(DOWN*2)
        self.play(
            Write( s )
        )
        self.play(
            Circumscribe(s, fade_in=True, stroke_width=5, run_time=2)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(s, shift=DOWN)
        )
        self.wait( DEFAULT_PAUSE )

        equation = MathTex("\\sum_{i=1}^{n-1} \\sum_{j=i+1}^{n} X_{i,j}")
        self.play(
            Transform(X, equation)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(tot, MathTex("X=").next_to(tot.get_center(), ORIGIN))
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            tot.animate.shift(DOWN + LEFT),
            X.animate.shift( RIGHT )
        )
        self.wait( DEFAULT_PAUSE )
        
        self.play(Flash(
            Group(tot, X),
            line_length=1,
            num_lines=30,
            color=YELLOW,
            flash_radius= Group(tot, X).width*.5 + SMALL_BUFF,
            time_width=0.3,
            run_time=2,
            rate_func = rush_from
        ))
        self.wait( DEFAULT_PAUSE )

        q = Text("but, how can I calculate it?").next_to(Group(tot, X), DOWN).scale(.5)
        self.play(
            FadeIn(q, shift=DOWN)
        )
        self.wait( DEFAULT_PAUSE )

        m = Text("I have to calculate the average").next_to(q, DOWN).scale(.5)
        self.play(
            GrowFromCenter( m )
        )
        self.wait( DEFAULT_PAUSE )

        eq = MathTex("\\mathbf{E}\\left[ X \\right] =", "\\mathbf{E}\\left[ \\sum_{i=1}^{n-1} \\sum_{j=i+1}^{n} X_{i,j} \\right]")
        self.play(
            ReplacementTransform(
                VGroup(tot, X),
                eq,
                run_time=1.75
            ),
            Wiggle(m[-7:], scale_value=1.25, run_time=2, n_wiggles=7)
            #Indicate(m[-7:], run_time=4)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut(
                Group(q, m),
                shift=DOWN
            )
        )
        self.wait( DEFAULT_PAUSE )

        brace = BraceText(eq, "Linearity property", brace_direction=DOWN)
        self.play(
            Transform(
                eq[1],
                MathTex(
                    "\\sum_{i=1}^{n-1} \\sum_{j=i+1}^{n}","\\mathbf{E}\\left[ X_{i,j} \\right]"
                    ).next_to(eq[1], ORIGIN)
            ),
            FadeIn(brace, shift=DOWN)
        )
        self.wait( DEFAULT_PAUSE )

        self.play( FadeOut(brace, shift=UP) )
        self.wait( DEFAULT_PAUSE )
        
        calculemus = Text(
            '"Calculemus!"',
            gradient=(BLUE, GREEN)
            ).to_edge(UP)
        self.play(
            Write( calculemus )
        )        
        self.wait( DEFAULT_PAUSE )

        leibniz = Text(
            "- Leibniz's dream -",
            slant=ITALIC
        ).next_to(calculemus, DOWN).scale(.5).set_opacity(.75)
        self.play(
            FadeIn(leibniz, shift=DOWN)
        )
        self.wait( DEFAULT_PAUSE*2 )

        self.play(
            ShrinkToCenter(Group(calculemus, leibniz))
        )
        self.wait( DEFAULT_PAUSE )

        self.remove( eq[1] )
        x = eq[1][-1].copy().set_opacity(1)
        self.add( x )

        eq.save_state()
        self.play(
            eq.animate().scale(.5).set_opacity(0),
            x.animate.next_to(ORIGIN, ORIGIN)
        )
        self.wait( DEFAULT_PAUSE )

class Analisi_3(Scene):
    def construct(self):

        x = MathTex("\\mathbf{E}\\left[ X_{i,j} \\right]")
        self.add( x )
        self.wait( DEFAULT_PAUSE )

        formula = _eq, val = MathTex(
            "=",
            "\\sum_{k} k \\cdot \\mathcal{P}\\left( X_{i,j} = k\\right)"
            ).shift( RIGHT + DOWN*.2 )
        
        self.play(
            x.animate.shift( LEFT*2.25 ),
            FadeIn(formula, shift=RIGHT)
        )
        self.wait( DEFAULT_PAUSE )

        _val = MathTex(
                    "0 \\cdot \\mathcal{P}\\left( X_{i,j} = 0\\right)",
                    "+",
                    "1 \\cdot \\mathcal{P}\\left( X_{i,j} = 1\\right)"
                    ).next_to(_eq, RIGHT)
        self.play(
            ReplacementTransform(
                val,
                _val
            )
        )
        self.wait( DEFAULT_PAUSE )
        val = _val

        rect = SurroundingRectangle(val[0])
        self.play( Create( rect ) )
        self.wait( DEFAULT_PAUSE )

        cross = Cross(val[0])
        self.play( Create( cross ) )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                rect,
                SurroundingRectangle(val[-1])
            )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                val,
                MathTex("\\mathcal{P}\\left( X_{i,j} = 1\\right)").next_to(_eq, RIGHT)
            ),
            Uncreate(cross, run_time=.5),
            Uncreate( rect )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Flash(
                Group(x, val),
                line_length=1,
                num_lines=30,
                color=YELLOW,
                flash_radius= Group(x, val).width*.5 + SMALL_BUFF,
                time_width=0.3,
                run_time=2,
                rate_func = rush_from
            )
        )
        self.wait( DEFAULT_PAUSE )
        
        p = val[-1].copy().set_opacity(1)
        self.play(
            VGroup(x, _eq, val).animate.scale(.5).set_opacity(0),
            p.animate.next_to(ORIGIN, ORIGIN)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                p,
                MathTex("\\mathcal{P}\\left( y_i, y_j \\mbox{ are compared}\\right)")
            )
        )
        self.wait( DEFAULT_PAUSE )

        t = Tex("how ?").next_to(p, UP)
        self.play(
            FadeIn(t, shift=UP)
        )
        self.wait( DEFAULT_PAUSE )
        self.play(
            FadeOut(t, shift=DOWN)
        )
        self.wait( DEFAULT_PAUSE )

        p.save_state()
        Y = Matrix(
            [["y_1", "\\cdots", "y_i", "y_{i+1}", "\\cdots", "y_k", "\\cdots", "y_{j-1}", "y_j", "\\cdots", "y_n"]]
            ).scale(.75)

        self.play(
            p.animate.to_corner( UL ).scale( .75 ),
            GrowFromCenter( Y )
        )
        self.wait( DEFAULT_PAUSE )

        yk = Y[0][5]
        yk.save_state()
        piv = Tex("pivot").scale(.5).next_to(yk, UP).set_color( ORANGE )
        self.play(
            yk.animate.scale( 1.5 ).set_color( ORANGE ),
            FadeIn(piv, shift=UP)
        )
        self.wait( DEFAULT_PAUSE )

        t1 = MathTex("i < k < j").shift( DOWN*1.5 )
        self.play( Write( t1 ) )
        self.wait( DEFAULT_PAUSE )

        t2 = MathTex("\\Rightarrow", "y_i \\leq y_k \\leq y_j").shift( DOWN*1.5 + RIGHT*1.5 )
        self.play(
            t1.animate.shift( LEFT*1.5 ),
            FadeIn(t2, shift=RIGHT)
        )
        self.wait( DEFAULT_PAUSE )

        t3 = Tex("$\\Rightarrow y_i$ will go left, $y_j$ will go right").shift( DOWN*1.5 + RIGHT*1.5 )
        self.play(
            t1.animate.shift( LEFT*3 ).set_opacity( 0 ),
            t2[0].animate.shift( LEFT*3 ).set_opacity( 0 ),
            t2[1].animate.shift( LEFT*5.3 ),
            FadeIn(t3, shift=LEFT)
        )
        self.wait( DEFAULT_PAUSE )

        t4 = Tex("$\\Rightarrow y_i$ and $y_j$ will never be compared!").shift( DOWN*1.5 )
        self.play(
            t2[1].animate.shift( LEFT*2 ).set_opacity( 0 ),
            t3.animate.shift( LEFT*2 ).set_opacity( 0 ),
            FadeIn(t4, shift=LEFT)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Restore( yk ),
            FadeOut( piv ),
            Unwrite( t4 )
        )
        self.wait( DEFAULT_PAUSE )

        self.play( Circumscribe( Y[0][:2] ) )
        self.wait( DEFAULT_PAUSE )
        self.play( Circumscribe( Y[0][9:] ) )
        self.wait( DEFAULT_PAUSE )

        Y.save_state()
        self.play(
            Y[0][:2].animate.scale( .5 ).set_opacity( .5 ),
            Y[0][2:9].animate.scale( 1.25 ),
            Y[0][9:].animate.scale( .5 ).set_opacity( .5 ),
            FocusOn( Y[0][2:9] )
        )
        self.wait( DEFAULT_PAUSE )

        brace = BraceText(Y[0][2:9], "pivot here!", brace_direction=DOWN)
        self.play( FadeIn(brace, shift=DOWN) )
        self.wait( DEFAULT_PAUSE )
        self.play( FadeOut(brace, shift=UP) )

        self.play( Indicate( Y[0][2] ) )
        self.wait( DEFAULT_PAUSE )
        self.play( Indicate( Y[0][8] ) )
        self.wait( DEFAULT_PAUSE )

        self.play( Restore( Y ) )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Y.animate.shift( DOWN*1.5 ),
            Restore( p )
        )
        self.wait( DEFAULT_PAUSE )

        new_p = MathTex(
                    "\\mathcal{P}\\left(",                                  #0
                    "\\mbox{pivot } \\in \\{",                              #1
                    "y_i",                                                  #2
                    ",",                                                    #3
                    "y_j",                                                  #4
                    "\\} | \\mbox{ pivot } \\in \\{",                       #5
                    "y_i, y_{i+1}, \\cdots, y_k, \\cdots, y_{j-1}, y_j",    #6
                    "\\} \\right)"
                )
        self.play( ReplacementTransform(p, new_p) )
        p = new_p
        self.wait( DEFAULT_PAUSE )

        self.play(
            Indicate(p[2], scale_factor=1.5, run_time=2),
            Indicate(Y[0][2], scale_factor=1.5, run_time=2)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Indicate(p[4], scale_factor=1.5, run_time=2),
            Indicate(Y[0][8], scale_factor=1.5, run_time=2)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Indicate(p[6],run_time=2),
            Indicate(Y[0][2:9], run_time=2)
        )
        self.wait( DEFAULT_PAUSE )

        p2 = MathTex(
            "= \\frac{2}{|\\{y_i, y_{i+1}, \\cdots, y_k, \\cdots, y_{j-1}, y_j\\}|}" 
        )
        self.play(
            p.animate.shift( UP*1.5 ),
            FadeIn(p2)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                p2,
                MathTex("= \\frac{2}{j-i+1}")
            )
        )
        self.wait( DEFAULT_PAUSE )

        x = MathTex(
            "\\mathbf{E}\\left[ X_{i,j} \\right]"
            ).next_to(p2, LEFT).shift( RIGHT )
        self.play(
            FadeOut( Y ),
            FadeOut( p ),
            p2.animate.shift( RIGHT ),
            FadeIn(x, shift=LEFT)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                VGroup(x, p2),
                MathTex(
                    "\\mathbf{E}\\left[ X \\right]",
                    "=",
                    "\\sum_{i=1}^{n-1} \\sum_{j=i+1}^{n}",
                    "\\frac{2}{j-i+1}"
                    )
            )
        )
        self.wait( DEFAULT_PAUSE )

class Analisi_4(Scene):
    def construct(self):
        X = MathTex(
            "\\mathbf{E}\\left[ X \\right]",
            "=",
            "\\sum_{i=1}^{n-1} \\sum_{j=i+1}^{n}",
            "\\frac{2}{j-i+1}"
            )
        self.add( X )
        self.wait( DEFAULT_PAUSE )
        
        new_X = MathTex(
            "\\mathbf{E}\\left[ X \\right]",    # 0
            "=",                                # 1
            "2",                                # 2
            "\\sum_{i=1}^{n-1}",                # 3
            "\\sum_{j=i+1}^{n}",                # 4 <-
            "\\frac{1}{j-i+1}"                  # 5
            )
        self.play( ReplacementTransform(X, new_X) )
        X = new_X
        self.wait( DEFAULT_PAUSE )

        X.save_state()

        self.play(
            X[:4].animate.scale( .5 ).set_opacity( 0 ),
            X[4:].animate.next_to(ORIGIN, ORIGIN)
        )
        self.wait( DEFAULT_PAUSE )

        self.play( X[4:].animate.to_edge(UP) )
        self.wait( DEFAULT_PAUSE )
        
        _i = 1
        i = Variable(
            _i, MathTex("i"), var_type=Integer
        ).to_corner( UL )
        i.label.set_color( YELLOW )
        
        _j = 2 
        j = Variable(
            _j, MathTex("j"), var_type=Integer
        ).next_to(i, DOWN)
        j.label.set_color( RED )

        
        self.play( 
            Write( i ),
            Write( j ),
            Transform(
                X[5][2:],
                MathTex(
                    "2 - 1 - 1",
                    tex_to_color_map={"2": RED}
                ).next_to(X[5][2:], ORIGIN)
            )
        )
        self.wait( DEFAULT_PAUSE )
        

        a1 = X[5].copy()
        self.play(
            Transform(
                a1,
                MathTex(
                    "\\frac{1}{2}"
                ).to_edge( LEFT ).set_color( GREEN )
            )
        )

        _j += 1
        self.play(
            j.tracker.animate.set_value( _j ),
            Transform(
                X[5][2:],
                MathTex(
                    "3 - 1 - 1",
                    tex_to_color_map={"3": RED}
                ).next_to(X[5][2:], ORIGIN)
            )
            )
        self.wait( DEFAULT_PAUSE )

        a2 = X[5:].copy()
        self.play(
            Transform(
                a2,
                MathTex(
                    "+ \\frac{1}{3}"
                ).next_to(a1, RIGHT).set_color( GREEN )
            )
        )
        self.wait( DEFAULT_PAUSE )

        _j += 1
        self.play(
            j.tracker.animate.set_value( _j ),
            Transform(
                X[5][2:],
                MathTex(
                    "4 - 1 - 1",
                    tex_to_color_map={"4": RED}
                ).next_to(X[5][2:], ORIGIN)
            )
            )
        self.wait( DEFAULT_PAUSE )

        a3 = X[5:].copy()
        self.play(
            Transform(
                a3,
                MathTex(
                    "+ \\frac{1}{4}"
                ).next_to(a2, RIGHT).set_color( GREEN )
            )
        )
        self.wait( DEFAULT_PAUSE )

        _j = 100
        self.play( j.tracker.animate(run_time=2).set_value( _j ) )
        self.wait( DEFAULT_PAUSE )

        a4 = MathTex("+ \\frac{1}{5}").next_to(a3, RIGHT).set_color( GREEN )
        self.play(
            Transform(
                X[5][2:],
                MathTex(
                    "5 - 1 - 1",
                    tex_to_color_map={"5": RED}
                ).next_to(X[5][2:], ORIGIN)
            ),
            FadeIn(a4, shift=RIGHT)
        )

        a5 = MathTex("+ \\frac{1}{6}").next_to(a4, RIGHT).set_color( GREEN )
        self.play(
            Transform(
                X[5][2:],
                MathTex(
                    "6 - 1 - 1",
                    tex_to_color_map={"6": RED}
                ).next_to(X[5][2:], ORIGIN)
            ),
            FadeIn(a5, shift=RIGHT)
        )

        a100 = MathTex("+ \\cdots + \\frac{1}{100}").next_to(a5, RIGHT).set_color( GREEN )
        self.play(
            Transform(
                X[5][2:],
                MathTex(
                    "100 - 1 - 1",
                    tex_to_color_map={"100": RED}
                ).next_to(X[5][2:], ORIGIN)
            ),
            FadeIn(a100, shift=RIGHT)
        )
        self.wait( DEFAULT_PAUSE )

        an = MathTex("+ \\cdots + ","\\frac{1}{n-i+1}").next_to(a100, RIGHT).set_color( GREEN )
        self.play(
            Transform(
                X[5][2:],
                MathTex(
                    "n - 1 - 1",
                    tex_to_color_map={"n": RED}
                ).next_to(X[5][2:], ORIGIN)
            ),
            FadeIn(an, shift=RIGHT)
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Flash(
                an[1],
                line_length=1,
                num_lines=30,
                color=YELLOW,
                flash_radius= an[1].width*.5 + SMALL_BUFF,
                time_width=0.3,
                run_time=2,
                rate_func = rush_from
            )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Unwrite( i ),
            Unwrite( j ),
            FadeOut(a1, a2, a3, a4, a5, a100, an),
            Restore( X )
        )
        self.wait( DEFAULT_PAUSE )

        
        new_X = MathTex(
            "\\mathbf{E}\\left[ X \\right]",    # 0
            "=",                                # 1
            "2",                                # 2
            "\\sum_{i=1}^{n-1}",                # 3
            "\\sum_{k=2}^{n-i+1}",              # 4
            "\\frac{1}{k}"                      # 5
            )
        self.play( ReplacementTransform(X, new_X) )
        X = new_X
        self.wait( DEFAULT_PAUSE )

        X.save_state()

        plane = NumberPlane(
            x_range = (0, 11),
            y_range = (0, 11),
            x_length = 6.5,
            y_length = 6.5,
            axis_config={"include_numbers": False}
        )
        plane.center()

        # ax = Axes(
        #     x_range=[0, 10],
        #     y_range=[0, 10],
        #     x_axis_config={
        #         "numbers_to_include": [1, 2, 3]
        #         },
        #     y_axis_config={
        #         "numbers_to_include": [1, 2, 3]
        #         },
        #     tips=False,
        # )
        
        labels = plane.get_axis_labels(
            x_label='i',
            y_label='k'
            )

        values = [
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (5, "\\cdots"),
            (8, "n-2"),
            (9, "n-1"),
            (10, "n")
        ]

        x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        for x_val, x_tex in values:
            tex = MathTex(x_tex)
            tex.scale( .45 )
            tex.next_to(plane.coords_to_point(x_val, 0), DOWN)
            x_axis_labels.add(tex)  # Add tex in graph
        
        values[3] = (5, "\\vdots")

        y_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        for y_val, y_tex in values:
            tex = MathTex(y_tex)
            tex.scale( .45 )
            tex.next_to(plane.coords_to_point(0, y_val), LEFT)
            x_axis_labels.add(tex)  # Add tex in graph

        self.play(
            X.animate.scale( .5 ).to_edge( RIGHT ),
            Create( plane ),
            Create( labels ),
            Create( x_axis_labels ),
            Create( y_axis_labels )
        )
        self.wait( DEFAULT_PAUSE )

        def get_circle_by_coord(coord):
            return Circle(radius=.1).next_to(coord, ORIGIN).set_fill(YELLOW, opacity=1)
        
        i = MathTex("i=","1").to_corner(UR, buff=1.5)
        k = MathTex("k=","2").next_to(i, DOWN)
        p = get_circle_by_coord(plane.coords_to_point(1, 2))
        points = [ p ]
        self.play(
            Create( i ),
            Create( k ),
            GrowFromCenter( p )
        )
        self.wait( DEFAULT_PAUSE )


        p = get_circle_by_coord(plane.coords_to_point(1, 3))
        self.play(
            Transform(k[1], MathTex("3").next_to(k[0], RIGHT)),
            GrowFromCenter( p )
        )
        points.append( p )
        self.wait( DEFAULT_PAUSE )

        p = get_circle_by_coord(plane.coords_to_point(1, 4))
        self.play(
            Transform(k[1], MathTex("4").next_to(k[0], RIGHT)),
            GrowFromCenter( p )
        )
        points.append( p )
        self.wait( DEFAULT_PAUSE )

        P = VGroup(*[get_circle_by_coord(plane.coords_to_point(1, h)) for h in range(5, 11)])
        ratios = [0, .5, 1, 1.5, 2, 2.5]  
        self.play(
            Transform(k[1], MathTex("n").next_to(k[0], RIGHT)),
            AnimationGroup(*[
                GrowFromCenter(p, lag_ratio=r)
                for p, r in zip(P, ratios)
            ])  
        )
        points.extend( P )
        self.wait( DEFAULT_PAUSE )

        P = VGroup(*[get_circle_by_coord(plane.coords_to_point(2, h)) for h in range(2, 10)])
        ratios = [0, .333, .666, 1, 1.333, 1.666, 2, 2.333]  
        self.play(
            Transform(i[1], MathTex("2").next_to(i[0], RIGHT)),
            k.animate.set_opacity( 0 ),
            AnimationGroup(*[
                GrowFromCenter(p, lag_ratio=r)
                for p, r in zip(P, ratios)
            ])  
        )
        points.extend( P )
        self.wait( DEFAULT_PAUSE )


        P = VGroup(*[get_circle_by_coord(plane.coords_to_point(3, h)) for h in range(2, 9)])
        ratios = [0, .4, .8, 1.2, 1.6, 2, 2.4]  
        self.play(
            Transform(i[1], MathTex("3").next_to(i[0], RIGHT)),
            k.animate.set_opacity( 0 ),
            AnimationGroup(*[
                GrowFromCenter(p, lag_ratio=r)
                for p, r in zip(P, ratios)
            ])  
        )
        points.extend( P )
        self.wait( DEFAULT_PAUSE )

        P = VGroup(*[get_circle_by_coord(plane.coords_to_point(4, h)) for h in range(2, 8)])
        ratios = [0, .5, 1, 1.5, 2, 2.5]  
        self.play(
            Transform(i[1], MathTex("4").next_to(i[0], RIGHT)),
            k.animate.set_opacity( 0 ),
            AnimationGroup(*[
                GrowFromCenter(p, lag_ratio=r)
                for p, r in zip(P, ratios)
            ])  
        )
        points.extend( P )
        self.wait( DEFAULT_PAUSE )

        P = VGroup(*[get_circle_by_coord(plane.coords_to_point(5, h)) for h in range(2, 7)])
        P.add(*[get_circle_by_coord(plane.coords_to_point(6, h)) for h in range(2, 6)])
        P.add(*[get_circle_by_coord(plane.coords_to_point(7, h)) for h in range(2, 5)])
        P.add(*[get_circle_by_coord(plane.coords_to_point(8, h)) for h in range(2, 4)])
        P.add( get_circle_by_coord(plane.coords_to_point(9, 2)) )

        self.play(
            Transform(i[1], MathTex("n-1").next_to(i[0], RIGHT)),
            AnimationGroup(*[
                GrowFromCenter(p)
                for p in P
            ])
        )
        points.extend( P )
        self.wait( DEFAULT_PAUSE )

        arrows = VGroup(*[
            Arrow(
                max_tip_length_to_length_ratio=.2,
                start=DOWN,
                end=UP
            )
            for _ in range(9)
        ]).arrange( LEFT ).to_corner( DOWN )

        self.play(
            AnimationGroup(*[
                GrowArrow(a)
                for a in arrows
            ])
        )
        self.play(
            arrows.animate.move_to( UP*5 ).set_opacity( 0 )
        )
        self.wait( DEFAULT_PAUSE )

        arrows = VGroup(*[
            Arrow(
                max_tip_length_to_length_ratio=.2,
                start=LEFT,
                end=RIGHT
            )
            for _ in range(9)
        ]).arrange( DOWN ).next_to(plane, LEFT)

        self.play(
            AnimationGroup(*[
                GrowArrow(a)
                for a in arrows
            ])
        )
        self.play(
            arrows.animate.move_to( RIGHT*5 ).set_opacity( 0 )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            FadeOut( i ),
            X.animate( run_time=2 ).scale( 2 ).next_to(ORIGIN+RIGHT, ORIGIN),
            VGroup(
                plane,
                labels,
                x_axis_labels,
                y_axis_labels,
                *points
            ).animate( run_time=2 ).scale( .5 ).to_edge( LEFT )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                X[3],
                MathTex("\\sum_{k=2}^{n}").next_to(X[3], ORIGIN)
            ),
            Transform(
                X[4],
                MathTex("\\sum_{i=1}^{n-k+1}").next_to(X[4], ORIGIN)
            )
        )
        self.wait( DEFAULT_PAUSE )

        s = Text("take a minute to convince yourself").scale( .75 ).to_edge( DOWN )
        self.play( FadeIn(s, shift=UP) )
        self.wait( DEFAULT_PAUSE*3 )

        self.play(
            FadeOut(s, shift=DOWN),
            X.animate( run_time=2 ).next_to(ORIGIN, ORIGIN),
            VGroup(
                plane,
                labels,
                x_axis_labels,
                y_axis_labels,
                *points
            ).animate( run_time=2 ).scale( .5 ).set_opacity( 0 )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                X[4:],
                MathTex("\\frac{n-k+1}{k}").next_to(X[3], RIGHT)
                )
        )
        self.wait( DEFAULT_PAUSE )  

        self.play(
            Transform(
                X[4:],
                MathTex("\\left( \\frac{n+1}{k} - \\frac{k}{k} \\right)").next_to(X[3], RIGHT)
                )
        )
        self.wait( DEFAULT_PAUSE )

        self.play(
            Transform(
                X[3:],
                MathTex(
                    "\\left( \\sum_{k=2}^{n}\\frac{n+1}{k} - \\sum_{k=2}^{n}1 \\right)"
                    ).next_to(X[2], RIGHT)
                )
        )
        self.wait( DEFAULT_PAUSE )

        x = MathTex(
            "\\left(",                      # 0
            "(n+1)",                        # 1
            "\\sum_{k=2}^{n}\\frac{1}{k}",  # 2
            "- (n-1) \\right)"              # 3
            ).next_to(X[2], RIGHT)
        self.play(
            ReplacementTransform(
                X[3:],
                x
            )   
        )
        self.wait( DEFAULT_PAUSE )

        brace = Brace(x[2], direction=DOWN)
        s = Tex("$\\approx$ harmonic series").scale( .5 ).next_to(brace, DOWN)
        self.play(
            FadeIn(Group(brace, s), shift=DOWN)
            )
        self.wait( DEFAULT_PAUSE )
        self.play(
            Transform(
                s,
                MathTex("\\approx \\ln{n} + \\Theta(1)").scale( .5 ).next_to(brace, DOWN)
            )
        )
        self.wait( DEFAULT_PAUSE )

        result = MathTex("2n\\ln{n} + \\Theta(n)").next_to(X[1], RIGHT)
        self.play(
            ShrinkToCenter(VGroup(brace, s)),
            ReplacementTransform(
                VGroup(x, X[2:]),
                result
            )
        )
        self.wait( DEFAULT_PAUSE )
        
        formula = Group(X[:2], result)
        flash = Flash(
                formula,
                line_length=1,
                num_lines=30,
                color=YELLOW,
                flash_radius= formula.width*.5 + SMALL_BUFF,
                time_width=0.3,
                run_time=2,
                rate_func = rush_from
            )

        self.play( flash )
        self.play( flash )

        t = Text(
            "RandomQuickSort's running time :)",
            gradient=(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
            ).to_edge( UP )
        self.play(
            FadeIn(t, shift=DOWN),
            flash
        )

        self.play( flash )

        self.play(
            FadeOut(t, shift=UP),
            ShrinkToCenter( formula )
        )
        self.wait( DEFAULT_PAUSE )
