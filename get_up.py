import argparse
import requests
import pendulum
import json


from github import Github

# the morning issue index is 4
GET_UP_ISSUE_NUMBER = 4
GET_UP_MESSAGE_TEMPLATE = (
    "今天的起床时间是--{get_up_time}.\r\n\r\n 起床啦，背个单词，锻炼身体。\r\n\r\n 今天的一句诗:\r\n {sentence}"
)
SENTENCE_API = "https://v1.jinrishici.com/all"
DEFAULT_SENTENCE = "苟利国家生死以\r\n岂因祸福避趋之\r\n"
TIMEZONE = "Asia/Shanghai"


def login(token):
    return Github(token)


def get_one_sentence():
    try:
        r = requests.get(SENTENCE_API)
        if r.ok:
            return r.json().get("content", DEFAULT_SENTENCE)
        return DEFAULT_SENTENCE
    except:
        print("get SENTENCE_API wrong")
        return DEFAULT_SENTENCE


def get_today_get_up_status(issue):
    comments = list(issue.get_comments())
    if not comments:
        return False
    latest_comment = comments[-1]
    now = pendulum.now(TIMEZONE)
    latest_day = pendulum.instance(latest_comment.created_at).in_timezone(
        "Asia/Shanghai"
    )
    is_today = (latest_day.day == now.day) and (latest_day.month == now.month)
    return is_today


def make_get_up_message():
    sentence = get_one_sentence()
    now = pendulum.now(TIMEZONE)
    # 4 - 7 means early for me
    # is_get_up_early = 4 <= now.hour <= 7 
    is_get_up_early = True
    get_up_time = now.to_datetime_string()
    body = GET_UP_MESSAGE_TEMPLATE.format(get_up_time=get_up_time, sentence=sentence)
    return body, is_get_up_early


# def main(github_token, repo_name, weather_message, tele_token, tele_chat_id):
def main(github_token, repo_name, weather_message,wc_robot_url):  
    u = login(github_token)
    repo = u.get_repo(repo_name)
    issue = repo.get_issue(GET_UP_ISSUE_NUMBER)
    is_toady = get_today_get_up_status(issue)
    if is_toady:
        print("Today I have recorded the wake up time")
        return
    early_message, is_get_up_early = make_get_up_message()
    body = early_message
    if weather_message:
        weather_message = f"现在的天气是{weather_message}\n"
        body = weather_message + early_message
    if is_get_up_early:
        issue.create_comment(body)

        # send to wechat
        if wc_robot_url:
            send_body = {'content':body}
            send_data = {"msgtype":"text","text":send_body}
            headers = {'Content-Type': 'application/json'}
            requests.post(url=wc_robot_url,headers=headers,data=json.dumps(send_data))

        # send to telegram
        # if tele_token and tele_chat_id:
        #     requests.post(
        #         url="https://api.telegram.org/bot{0}/{1}".format(
        #             tele_token, "sendMessage"
        #         ),
        #         data={
        #             "chat_id": tele_chat_id,
        #             "text": body,
        #         },
        #     )
    else:
        print("You wake up late")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument(
        "--weather_message", help="weather_message", nargs="?", default="", const=""
    )
    parser.add_argument("--wc_robot_url", help="wc_robot_url", nargs="?", default="", const="")
    # parser.add_argument("--tele_chat_id", help="tele_chat_id", nargs="?", default="", const="")
    options = parser.parse_args()
    main(
        options.github_token,
        options.repo_name,
        options.weather_message,
        options.wc_robot_url,
        # options.tele_chat_id,
    )