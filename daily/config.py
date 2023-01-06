READ_LABEL_LIST = [
    "Read",
]

PUSHUP_LABEL_LIST = [
    "PushUps",
]

MORNING_LABEL_LIST = [
    "Morning",
]

WEEKLY_LABEL_LIST = [
    "Weekly",
]

SQUAT_LABEL_LIST = [
    "Squat",
]

PULLUP_LABEL_LIST = [
    "PullUps",
]

SHANBAY_LABEL_LIST = [
    "Shanbay",
]

MY_BLOG_REPO = "mengziin/gitblog"
GITHUB_README_COMMENTS = (
    "(<!--START_SECTION:{name}-->\n)(.*)(<!--END_SECTION:{name}-->\n)"
)

# add new label here
LABEL_DICT = {
    "Read": {"label_list": READ_LABEL_LIST, "comment_name": "my_read"},
    "PushUps": {"label_list": PUSHUP_LABEL_LIST, "comment_name": "my_pushups"},
    "Morning": {"label_list": MORNING_LABEL_LIST, "comment_name": "my_morning"},
    "Weekly": {"label_list": WEEKLY_LABEL_LIST, "comment_name": "my_weekly"},
    "Squat": {"label_list": SQUAT_LABEL_LIST, "comment_name": "my_squat"},
    "PullUps": {"label_list": PULLUP_LABEL_LIST, "comment_name": "my_pullups"},
}

##### BASE COMMENT TABLE ######
BASE_ISSUE_STAT_HEAD = "| Name | Start | Update | \n | ---- | ---- | ---- | \n"
BASE_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | \n"

##### BLOG COMMENT ######
BLOG_ISSUE_STAT_HEAD = (
    "| Name | Start | Update | Comments | \n | ---- | ---- | ---- | ---- |\n"
)
BLOG_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | {comments} | \n"

##### Month Summary ######
MONTH_SUMMARY_HEAD = "| Month | Number | \n | ---- | ---- | \n"

MONTH_SUMMARY_STAT_TEMPLATE = "| {month} | {number} |\n"