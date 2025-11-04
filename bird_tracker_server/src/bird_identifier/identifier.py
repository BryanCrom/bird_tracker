from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime

def merge_detections(detections: list, merge_gap: float) -> list:

    """
    Merge consecutive detections into single detection.

    :param detections: all detections
    :param merge_gap: gap between detections for an acceptable merge
    :return merged: new list of merged detections
    """

    merged = []
    detections = sorted(detections, key=lambda d: d["start_time"])

    for detection in detections:
        if not merged:
            merged.append(detection)
            continue

        last = merged[-1]

        if detection["common_name"] == last["common_name"] and detection["start_time"] - last["start_time"] <= merge_gap:
            last["end_time"] = detection["end_time"]
            last["confidence"] = max(detection["confidence"],last["confidence"])
        else:
            merged.append(detection)

    return merged


class Identifier:
    def __init__(self) -> None:
        self.analyzer = Analyzer()

    def identify(self, bird_call) -> None:

        """
        identify a bird from its call.
        :param bird_call: path to bird call audio file
        :return: None
        """

        recording = Recording(self.analyzer, bird_call, lat=0, lon=0, date=datetime.now(), min_conf=0.25)
        recording.analyze()
        print(len(merge_detections(recording.detections, 3)))
