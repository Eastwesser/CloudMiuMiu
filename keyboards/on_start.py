from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonPollType,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonText:
    HELLO = "Hello!"
    WHATS_NEXT = "What's next?"
    BYE = "Good bye!"


def get_on_start_kb() -> ReplyKeyboardMarkup:
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WHATS_NEXT)
    button_bye = KeyboardButton(text=ButtonText.BYE)
    buttons_row_1 = [button_hello, button_help]
    buttons_row_2 = [button_bye]
    markup_keyboard = ReplyKeyboardMarkup(
        keyboard=[buttons_row_1,
                  buttons_row_2],
        resize_keyboard=True,
    )
    return markup_keyboard


def get_on_help_kb():
    numbers = [
        "/weather",
        "/converter",
        "/calculator",
        "/food",
        "/sticker_kb",
        "/magnetic_storm",
        "/memes",
        "/start_block_me",
        "/rps",
        "/start_blackjack",
    ]

    builder = ReplyKeyboardBuilder()
    for num in numbers:
        builder.add(KeyboardButton(text=num))

    builder.adjust(3)

    return builder.as_markup(resize_keyboard=False)  # возвращаем builder как markup, чтобы у нас была разметка


def get_actions_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="🌍 Send Location",
        request_location=True,
    )
    builder.button(
        text="📱 Send My Phone",
        request_contact=True,
    )
    builder.button(
        text="📊 Send Poll",
        request_poll=KeyboardButtonPollType(),
    )
    builder.button(
        text="❓ Send Quiz",
        request_poll=KeyboardButtonPollType(type="quiz"),
    )
    builder.button(
        text="❔ Regular Quiz",
        request_poll=KeyboardButtonPollType(type="regular"),
    )
    builder.button(
        text=ButtonText.BYE,
    )
    builder.adjust(1)
    return builder.as_markup(
        input_field_placeholder="Actions:",
        resize_keyboard=True,
    )


def build_yes_or_no_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Yes")
    builder.button(text="No")
    # builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
