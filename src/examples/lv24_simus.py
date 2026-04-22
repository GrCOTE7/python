import asyncio
import random
from collections.abc import Callable, Sequence

DEFAULT_USERS = [
    "1Alice",
    "1Bob",
    "1Charlie",
    "1Diana",
    "2Alice",
    "2Bob",
    "2Charlie",
    "2Diana",
    "3Alice",
    "3Bob",
    "3Charlie",
    "3Diana",
    "4Alice",
    "4Bob",
    "4Charlie",
    "4Diana",
    "5Alice",
    "5Bob",
    "5Charlie",
    "5Diana",
]

DEFAULT_MESSAGES = [
    "Hello everyone!",
    "How's it going?",
    "Anyone up for a game?",
    "What's the plan for today?",
    "Did you see the news?",
    "2 Hello everyone!",
    "2 How's it going?",
    "2 Anyone up for a game?",
    "2 What's the plan for today?",
    "2 Did you see the news?",
    "3 Hello everyone!",
    "3 How's it going?",
    "3 Anyone up for a game?",
    "3 What's the plan for today?",
    "3 Did you see the news?",
    "4 Hello everyone!",
    "4 How's it going?",
    "4 Anyone up for a game?",
    "4 What's the plan for today?",
    "4 Did you see the news?",
    "5 Hello everyone!",
    "5 How's it going?",
    "5 Anyone up for a game?",
    "5 What's the plan for today?",
    "5 Did you see the news?",
]


async def simulate_chat(
    publish: Callable[[str, str, str], None],
    *,
    users: Sequence[str] | None = None,
    messages: Sequence[str] | None = None,
    # delay_range: tuple[int, int] = (2, 5),
    delay_range: tuple[int, int] = (1, 2),
) -> None:
    user_names = list(users or DEFAULT_USERS)
    message_texts = list(messages or DEFAULT_MESSAGES)

    if not user_names or not message_texts:
        return

    random.shuffle(user_names)

    for user_name in user_names:
        await asyncio.sleep(random.randint(*delay_range))
        publish(user_name, f"{user_name} has joined the chat.", "login_message")

        await asyncio.sleep(random.randint(*delay_range))
        publish(user_name, random.choice(message_texts), "chat_message")
