from datetime import datetime, timedelta
import isodate
from typing import List
from pathlib import Path
from os import listdir, getcwd
import math
import string
from itertools import chain

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import demoji
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words


all_punct = string.punctuation
all_punct += '`'
all_punct += '’'

ROOT = Path(getcwd())
DATA = ROOT.joinpath('data')
CLEAN_DATA = ROOT.joinpath('clean_data')
current_files = [Path(str(i)).name for i in listdir(DATA)]
file_data = {'index': [i + 1 for i in range(len(current_files))],
             'name': current_files}
file_df = pd.DataFrame.from_dict(file_data, orient='columns')




# //////////////////////////////////////////

def convert_date(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").date()
    return dt.strftime("%Y-%m-%d")


def convert_duration(duration):
    delta = isodate.parse_duration(duration)

    # Extract hours, minutes, and seconds
    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format as a readable string
    return f"{int(hours)}:{int(minutes):02}:{int(seconds):02}"


def duration_to_secs(duration):
    return sum(int(part) * conv_factors[i] for i, part in enumerate(duration.split(':')))


def remove_emojis(text):
    dem = demoji.findall(text)
    for item in dem.keys():
        text = text.replace(item, '').strip()
    return text


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
