class TestReceiver:

    def test_receive(self):
        telegram_input = {
            "update_id": 10000,
            "message": {
                "date": 1441645532,
                "chat": {
                    "last_name": "Test Lastname",
                    "id": 1111111,
                    "type": "private",
                    "first_name": "Test Firstname",
                    "username": "Testusername"
                },
                "message_id": 1365,
                "from": {
                    "last_name": "Test Lastname",
                    "id": 1111111,
                    "first_name": "Test Firstname",
                    "username": "Testusername"
                },
                "text": "/start"
            }
        }
        central_data = {
            "name": "New message",
            "content": "/start"
        }
        assert telegram_input["message"]["text"] == central_data["content"]
