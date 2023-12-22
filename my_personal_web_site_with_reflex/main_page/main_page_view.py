import reflex as rx

class ChatPair:
    def __init__(self):
        print("ChatPair instance")
        self._question_pair = [
            (
                "What is Reflex?",
                "A way to build web apps in pure Python!",
            ),
            (
                "What can I make with it?",
                "Anything from a simple website to a complex web app!",
            ),
        ]

    def get_question_pair_box(self, question_pair) -> rx.Component:
        print("get questin pair box")
        return rx.box(
            *[
                self._qa(question, answer)
                for question, answer in question_pair
            ]
        )

    def _qa(self, question: str, answer: str) -> rx.Component:
        print("Calling _qa")
        print(f"question: {question}")
        print(f"answer: {answer}")
        return rx.box(
            rx.box(question, text_align="right"),
            rx.box(answer, text_align="left"),
            margin_y="1em",
        )

class MainPageView:
    def __init__(self):
        print("MainPageView instance")
        self._chat_pair = ChatPair()
        init_question_pair = [
            (
                "What is Reflex?",
                "A way to build web apps in pure Python!",
            ),
            (
                "What can I make with it?",
                "Anything from a simple website to a complex web app!",
            ),
        ]
        self.init_pair_box = self._chat_pair.get_question_pair_box(question_pair = init_question_pair)

    def get_content():
        return rx.container(rx.heading("My chat", text_align="center")) #, self.init_pair_box)




