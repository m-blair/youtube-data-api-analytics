from datetime import datetime, timedelta
import isodate
from typing import List
from pathlib import Path
from os import listdir, getcwd
import pandas as pd
import string
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words

all_punct = string.punctuation
all_punct += '`'
all_punct += '’'

def remove_punct(title: str):
    translator = str.maketrans('', '', all_punct)
    return title.translate(translator)


def duration_to_secs(time_str: str) -> timedelta:
    hours, minutes, seconds = map(int, time_str.split(":"))
    time_del = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return time_del


def secs_to_duration(seconds):
    time_delta = timedelta(seconds=seconds)
    # Create a datetime object with a fixed date (Jan 1, 1900) and add the time duration
    base_date = datetime(1900, 1, 1)
    result_datetime = base_date + time_delta

    # Format the result as "hh:mm:ss"
    formatted_time = result_datetime.strftime("%H:%M:%S")
    return formatted_time
