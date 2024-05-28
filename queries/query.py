import random

from translator_app.models import User, Word


def get_words():
    return Word.objects.all()


def get_user(chat_id, first_name=None, username=None):
    user, created = User.objects.get_or_create(chat_id=chat_id)
    if created:
        user.first_name = first_name
        user.username = username
        user.save()
    return user


def get_random_word(user_word_ids: list):
    words = Word.objects.all()
    word_ids = words.values_list('id', flat=True)
    if user_word_ids:
        word_ids = word_ids.exclude(id__in=user_word_ids)

    random_id = random.choice(word_ids)
    word = words.get(id=random_id)
    user_word_ids.append(random_id)
    return word, user_word_ids

