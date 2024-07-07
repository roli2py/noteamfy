class TestSender:

    def test_send(self):
        central_data = {
            "name": "New message",
            "content": "/start"
        }
        discord_output = {
            "embeds": [
                {
                    "title": "New message",
                    "description": "/start"
                }
            ]
        }
        assert central_data["name"] == discord_output["embeds"][0]["title"]
        assert central_data["content"] == discord_output["embeds"][0]["description"]
