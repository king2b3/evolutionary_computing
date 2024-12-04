"""Simple timer data structure

original author: bking
"""
import time
class Timer():
    """Basic timer utility"""
    def __init__(self):
        """Timer class to track and report time usage to print"""
        self.start_time = 0
        self.end_time = 0
        self.time = 0

    def start_timer(self) -> None:
        """Records the start of a timer and resest both the start / end"""
        self.start_time = time.time()

    def end_timer(self) -> None:
        """Records the end value of a timer"""
        self.end_time = time.time()

    def __str__(self) -> float:
        """Returns the End - Start."""
        self.time = self.end_time - self.start_time
        return 'Run time: {:0.4f}\n'.format(self.time)
