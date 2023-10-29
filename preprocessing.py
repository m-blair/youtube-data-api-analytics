from datetime import datetime
import isodate
import demoji
import pandas as pd
from typing import List
from pathlib import Path
from os import listdir, getcwd

ROOT = Path(getcwd())
DATA = ROOT.joinpath('data')
CLEAN_DATA = ROOT.joinpath('clean_data')
current_files = [Path(str(i)).name for i in listdir(DATA)]
file_data = {'index': [i + 1 for i in range(len(current_files))],
             'name': current_files}
file_df = pd.DataFrame.from_dict(file_data, orient='columns')


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
    conv_factors = [3600, 60, 1]
    # total = 0
    # for index, part in enumerate(duration[':']):
    #     total += int(part) * conv_factors[index]
    return sum(int(part) * conv_factors[i] for i, part in enumerate(duration.split(':')))

def remove_emojis(text):
    dem = demoji.findall(text)
    for item in dem.keys():
        text = text.replace(item, '').strip()
    return text
