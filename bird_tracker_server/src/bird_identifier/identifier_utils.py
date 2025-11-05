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

        if detection["common_name"] == last["common_name"] and detection["start_time"] - last["end_time"] <= merge_gap:
            last["end_time"] = detection["end_time"]
            last["confidence"] = max(detection["confidence"],last["confidence"])
        else:
            merged.append(detection)

    return merged