#!/usr/bin/python3
def best_score(score_dict):
    if not score_dict:
        return None
    return max(score_dict, key=score_dict.get)
