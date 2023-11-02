import math
from collections import Counter
from datetime import datetime, timedelta
import isodate
from typing import List
from pathlib import Path
from os import listdir, getcwd
import string
from itertools import chain

import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words

# local file import
import preprocessing

stop_words = list(get_stop_words('en'))
stop_words += [i.title() for i in stop_words]  # add capitalized versions of stop_words to stop_word list


# NLP-related methods //////////////////////////////////////////////////////////////

def bag_of_words(title: str, remove_stop_words: bool = False):
    title = preprocessing.remove_punct(title)
    words = word_tokenize(title)
    if remove_stop_words:
        words = [word for word in words if word not in stop_words]
    return words


def count_words(all_titles: list):
    counter = Counter()
    # flatten list of lists to a single list
    all_words = list(chain(*all_titles))
    for word in all_words:
        if word not in counter.keys():
            counter[word] = 1
        else:
            counter[word] += 1
    return counter


# DESCRIPTIVE STATS CALCULATIONS ///////////////////////////////////////////////////

def sample_mean(samples: List[float]) -> float:
    """calculates the mean of a sample"""
    num_samples = len(samples)
    return round(sum(samples) / num_samples, 2)


def sample_variance(samples: List[float]) -> float:
    """calculates sample variance"""
    x_bar = sample_mean(samples)
    n = len(samples)
    sum_of_square_diffs = sum([(i - x_bar) ** 2 for i in samples])
    return round(sum_of_square_diffs / (n - 1), 2)


def quartile_info(samples: List[float]) -> tuple:
    """returns relevant values related to the quartiles of the data"""
    sorted_samples: list = sorted(samples)
    n = len(sorted_samples)

    if n % 2 == 0:
        median = (sorted_samples[n // 2 - 1] + sorted_samples[n // 2]) / 2
    else:
        median = sorted_samples[n // 2]

    q1_index = int(n * 0.25)
    q1 = (sorted_samples[q1_index] + sorted_samples[q1_index - 1]) / 2 if n % 4 == 0 else sorted_samples[q1_index]
    q3_index = int(n * 0.75)
    q3 = (sorted_samples[q3_index] + sorted_samples[q3_index - 1]) / 2 if n % 4 == 0 else sorted_samples[q3_index]

    iqr = round(q3 - q1, 2)
    return q1, median, q3, iqr


def sample_std_dev(sample_variance: float) -> float:
    """calculates sample standard deviation from the mean"""
    return round(math.sqrt(sample_variance), 2)
