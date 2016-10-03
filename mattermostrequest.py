class MattermostRequest(object):
    def __init__(self, post_data):
        self.response_url = post_data.get("response_url")
        self.text = post_data.get("text")
        self.token = post_data.get("token")
        self.channel_id = post_data.get("channel_id")
        self.team_id = post_data.get("team_id")
        self.command = post_data.get("command")
        self.team_domain = post_data.get("team_domain")
        self.user_name = post_data.get("user_name")
        self.channel_name = post_data.get("channel_name")
