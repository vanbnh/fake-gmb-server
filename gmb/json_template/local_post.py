def local_post_json_template(acc_id, loc_id, post_id):
    local_post_temp = {
        "name": f"accounts/{acc_id}/locations/{loc_id}/localPosts/{post_id}",
        "languageCode": "ja",
        "summary": "秋のスーパーセール",
        "callToAction": {
            "actionType": "LEARN_MORE",
            "url": "https://photos.google.com/"
        },
        "state": "LIVE",
        "event": {
            "title": "【テスト】キャンペーン",
            "schedule": {
                "startDate": {
                    "year": 2022,
                    "month": 11,
                    "day": 11
                },
                "startTime": {
                    "hours": 23,
                    "minutes": 59,
                    "seconds": 59
                },
                "endDate": {
                    "year": 2022,
                    "month": 11,
                    "day": 22
                },
                "endTime": {
                    "hours": 23,
                    "minutes": 59,
                    "seconds": 59
                }
            }
        },
        "updateTime": "2022-11-17T10:41:15.243Z",
        "createTime": "2022-11-17T10:41:15.243Z",
        "media": [
            {
                "name": f"accounts/{acc_id}/locations/{loc_id}/media/localPosts/AF1QipPdVwNM2joUQnObyMBq_zxEMP2R-WjWB-3QFpEX",
                "mediaFormat": "PHOTO",
                "googleUrl": f"https://lh3.googleusercontent.com/p/AF1QipPdVwNM2joUQnObyMBq_zxEMP2R-WjWB-3QFpEX"
            }
        ],
        "topicType": "EVENT"
    }
    return local_post_temp
