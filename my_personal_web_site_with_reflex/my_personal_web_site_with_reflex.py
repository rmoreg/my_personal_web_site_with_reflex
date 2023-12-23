"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx
import asyncio
import time
from my_personal_web_site_with_reflex import style
from my_personal_web_site_with_reflex.main_page.main_page_view import MainPageView

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        # Our chatbot is not very smart right now...
        now = time.strftime("%H:%M:%S")
        answer = f"Usted ha realizado la siguiente pregunta - {self.question} - a las {now}"
        self.chat_history.append((self.question, ""))
        self.question = ""

        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.1)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value = State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style,
            ),
        rx.button(
        "Ask", 
        on_click=State.answer,
        style = style.button_style
        ),
    )

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right"
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left"
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    # return rx.box(
    #     *[
    #         qa(question, answer)
    #         for question, answer in qa_pairs
    #     ]
    # )
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def index() -> rx.Component:
    return rx.container(rx.heading("My chat", text_align="center"),chat(), action_bar())


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()

# app = rx.App()
# main_window = MainPageView()
# app.add_page(main_window.get_content)
# app.compile()
