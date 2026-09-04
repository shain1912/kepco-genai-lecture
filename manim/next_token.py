"""
언어모델이 하는 일 — "사실을 찾는 게 아니라, 다음에 올 법한 말을 고른다"
슬라이드 07(왜 끝났는가)에 삽입. 덱과 같은 다크 팔레트.

렌더 (저장소 루트에서):
    manim -qh manim/next_token.py NextToken
결과:
    media/videos/next_token/1080p60/NextToken.mp4  →  assets/manim_next_token.mp4
"""

from manim import *
from palette import KO, BG, INK, SUB, ACC, EXEC, LINE, WARN


class NextToken(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("언어모델이 하는 일", font=KO, weight=BOLD, color=INK).scale(0.85)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title, shift=DOWN * 0.3))
        self.wait(0.6)

        # 지금까지 나온 말
        given = Text("제3조", font=KO, weight=BOLD, color=INK).scale(1.25)
        given.move_to(LEFT * 4.2 + UP * 0.9)
        label = Text("지금까지 나온 말", font=KO, color=SUB).scale(0.45)
        label.next_to(given, UP, buff=0.35)
        self.play(FadeIn(label), Write(given))
        self.wait(0.5)

        arrow = Arrow(given.get_right() + RIGHT * 0.15,
                      given.get_right() + RIGHT * 1.35,
                      buff=0, color=SUB, stroke_width=5)
        qmark = Text("다음에 올 말은?", font=KO, color=SUB).scale(0.45)
        qmark.next_to(arrow, DOWN, buff=0.3)
        self.play(GrowArrow(arrow), FadeIn(qmark))
        self.wait(0.4)

        # 후보와 확률 (개념 도식 — 실제 측정치 아님)
        cands = [("제2항", 0.62), ("제1항", 0.21), ("에", 0.11), ("의", 0.06)]
        bars, texts, pcts = VGroup(), VGroup(), VGroup()
        top = UP * 1.7
        for i, (w, p) in enumerate(cands):
            y = top + DOWN * (i * 0.95)
            t = Text(w, font=KO, weight=BOLD, color=INK).scale(0.6)
            t.move_to(RIGHT * 0.1 + y).align_to(RIGHT * 0.1, LEFT)
            bar = Rectangle(width=p * 7.0, height=0.42,
                            fill_color=ACC if i == 0 else EXEC,
                            fill_opacity=1, stroke_width=0)
            bar.next_to(t, RIGHT, buff=0.5).align_to(t, DOWN).shift(UP * 0.03)
            pc = Text(f"{int(p*100)}%", font=KO, color=SUB).scale(0.42)
            pc.next_to(bar, RIGHT, buff=0.3)
            bars.add(bar); texts.add(t); pcts.add(pc)

        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.2) for t in texts], lag_ratio=0.15))
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.15),
                  LaggedStart(*[FadeIn(p) for p in pcts], lag_ratio=0.15))
        self.wait(0.8)

        # 가장 높은 걸 고른다
        pick = SurroundingRectangle(VGroup(texts[0], bars[0], pcts[0]),
                                    color=ACC, buff=0.18, corner_radius=0.08)
        picked = Text("가장 그럴듯한 걸 고른다", font=KO, weight=BOLD, color=ACC).scale(0.5)
        picked.next_to(pick, DOWN, buff=0.3).align_to(pick, LEFT)
        self.play(Create(pick), FadeIn(picked, shift=UP * 0.2))
        self.wait(1.0)

        # 이어붙이기
        self.play(FadeOut(VGroup(bars, texts, pcts, pick, picked, arrow, qmark)))
        grown = Text("제3조 제2항에 따라 보고한다", font=KO, weight=BOLD, color=INK).scale(1.0)
        grown.move_to(UP * 0.9)
        self.play(ReplacementTransform(given, grown), FadeOut(label))
        self.wait(0.8)

        # 결론
        line = Line(LEFT * 5.6, RIGHT * 5.6, color=LINE, stroke_width=3)
        line.move_to(DOWN * 0.5)
        self.play(Create(line))

        c1 = Text("이 과정 어디에도", font=KO, color=INK).scale(0.62)
        c2 = Text("사실을 확인하는 단계가 없다", font=KO, weight=BOLD, color=WARN).scale(0.78)
        c1.move_to(DOWN * 1.3)
        c2.next_to(c1, DOWN, buff=0.35)
        self.play(FadeIn(c1, shift=UP * 0.2))
        self.wait(0.3)
        self.play(FadeIn(c2, shift=UP * 0.2))
        self.wait(1.6)

        note = Text("개념 도식 — 실제 측정치가 아님", font=KO, color=SUB).scale(0.36)
        note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note))
        self.wait(1.4)
