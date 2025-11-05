from src.bird_identifier.identifier_utils import merge_detections

from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime

class Identifier:

    analyzer: Analyzer

    def __init__(self) -> None:
        self.analyzer = Analyzer()

    def identify(self, bird_call) -> list:

        """
        identify a bird from its call.
        :param bird_call: path to bird call audio file
        :return: None
        """

        recording = Recording(self.analyzer, bird_call, lat=0, lon=0, date=datetime.now(), min_conf=0.25)
        recording.analyze()

        return merge_detections(recording.detections, 2)
