from .from_issues import get_info_from_issue_comments

MY_STATUS_DICT_FROM_COMMENTS = {
    "俯卧撑": {"daily_func": get_info_from_issue_comments, "unit_str": " (个)"},
    "深蹲": {"daily_func": get_info_from_issue_comments, "unit_str": " (个)"},
    "引体向上": {"daily_func": get_info_from_issue_comments, "unit_str": " (个)"},
    "周记": {"daily_func": get_info_from_issue_comments, "unit_str": " (周)"},
    "早起": {"daily_func": get_info_from_issue_comments, "unit_str": " (天)"},
}
