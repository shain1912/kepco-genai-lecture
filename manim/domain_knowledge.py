"""
도메인 지식 — 모델이 좋아져도 줄지 않는 몫
슬라이드 12(일반해 vs 특수해)에 삽입. 덱과 같은 다크 팔레트.

렌더 (저장소 루트에서):
    manim -qh manim/domain_knowledge.py DomainKnowledge
결과:
    media/videos/domain_knowledge/1080p60/DomainKnowledge.mp4  →  assets/manim_domain.mp4
"""

from manim import *
from palette import KO, BG, INK, SUB, ACC, EXEC, LINE, OK


class DomainKnowledge(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("업무 하나를 둘로 나누면", font=KO, weight=BOLD, color=INK).scale(0.8)
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.wait(0.5)

        W = 2.0
        base_y = -2.2

        def stack(exec_h, judge_h, x):
            ex = Rectangle(width=W, height=exec_h, fill_color=EXEC,
                           fill_opacity=1, stroke_width=0)
            ju = Rectangle(width=W, height=judge_h, fill_color=ACC,
                           fill_opacity=1, stroke_width=0)
            ex.move_to([x, base_y + exec_h / 2, 0])
            ju.move_to([x, base_y + exec_h + judge_h / 2, 0])
            return VGroup(ex, ju)

        JUDGE = 1.5
        s1 = stack(1.1, JUDGE, -2.6)
        s2 = stack(2.6, JUDGE, 0.9)
        s3 = stack(3.6, JUDGE, 4.4)

        axis = Line([-4.6, base_y, 0], [6.0, base_y, 0], color=LINE, stroke_width=4)
        axis_lbl = Text("모델 성능이 좋아진다  →", font=KO, color=SUB).scale(0.45)
        axis_lbl.next_to(axis, DOWN, buff=0.3).align_to(axis, RIGHT)
        self.play(Create(axis), FadeIn(axis_lbl))

        # 범례 — 왼쪽 여백에 두어 잘리지 않게 한다
        sw_j = Square(0.28, fill_color=ACC, fill_opacity=1, stroke_width=0)
        t_j = Text("사람이 정하는 판단", font=KO, weight=BOLD, color=ACC).scale(0.4)
        t_j.next_to(sw_j, RIGHT, buff=0.22)
        sw_e = Square(0.28, fill_color=EXEC, fill_opacity=1, stroke_width=0)
        t_e = Text("AI가 대신하는 실행", font=KO, color=SUB).scale(0.4)
        t_e.next_to(sw_e, RIGHT, buff=0.22)
        ylbl = Text("세로축 = 해낼 수 있는 일의 양", font=KO, color=SUB).scale(0.36)
        leg = VGroup(VGroup(sw_j, t_j), VGroup(sw_e, t_e), ylbl) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        leg.to_corner(UL, buff=0.7).shift(DOWN * 0.9)

        self.play(GrowFromEdge(s1[0], DOWN), GrowFromEdge(s1[1], DOWN))
        self.play(FadeIn(leg))
        self.wait(0.9)

        self.play(GrowFromEdge(s2[0], DOWN), GrowFromEdge(s2[1], DOWN))
        self.wait(0.4)
        self.play(GrowFromEdge(s3[0], DOWN), GrowFromEdge(s3[1], DOWN))
        self.wait(0.8)

        # 판단 층은 그대로라는 걸 선으로 잇는다
        top1 = s1[1].get_top()
        top3 = s3[1].get_top()
        bot1 = s1[1].get_bottom()
        bot3 = s3[1].get_bottom()
        lt = DashedLine([top1[0] - 1.1, top1[1], 0], [top3[0] + 1.1, top3[1], 0],
                        color=ACC, stroke_width=3, dash_length=0.12)
        lb = DashedLine([bot1[0] - 1.1, bot1[1], 0], [bot3[0] + 1.1, bot3[1], 0],
                        color=ACC, stroke_width=3, dash_length=0.12)
        self.play(Create(lt), Create(lb))

        keep = Text("이 층의 두께는 그대로다", font=KO, weight=BOLD, color=ACC).scale(0.72)
        keep.move_to(title.get_center())
        self.play(FadeOut(title, shift=UP * 0.25))
        self.play(FadeIn(keep, shift=DOWN * 0.25))
        self.wait(1.4)

        # 차트는 할 일을 끝냈다 — 결론은 빈 화면에서
        self.play(FadeOut(VGroup(keep, leg, s1, s2, s3, lt, lb, axis, axis_lbl)))

        c1 = Text("무엇이 급한 일인지", font=KO, color=INK).scale(0.6)
        c2 = Text("무엇을 넣으면 안 되는지", font=KO, color=INK).scale(0.6)
        c3 = Text("무엇이 틀렸는지", font=KO, color=INK).scale(0.6)
        col = VGroup(c1, c2, c3).arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        col.move_to(UP * 1.2)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.25) for c in col], lag_ratio=0.3))
        self.wait(0.7)

        fin = Text("이건 현장에 있었던 사람만 안다", font=KO, weight=BOLD, color=OK).scale(0.7)
        fin.next_to(col, DOWN, buff=0.85)
        self.play(FadeIn(fin, shift=UP * 0.2))
        self.wait(1.6)

        note = Text("개념 도식 — 실제 측정치가 아님", font=KO, color=SUB).scale(0.36)
        note.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(note))
        self.wait(1.2)
