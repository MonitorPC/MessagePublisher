# MessagePublisher

### To start 
- Clone the rep
- Run `docker compose up --build -d`
- Run `src/user_api.py`, `src/filter_service.py`, `src/screaming_service.py`, `src/publisher_service.py`. Each in different Run`src/user_api.py , `src/filter_service.py`, `src/screaming_service.py`, `src/publisher_service.py`. Each in different terminal.

### To test
- Run `curl -H 'Content-Type: application/json' -X POST -d '{"user": "testuser", "message": "This is a normal test message."}' http://127.0.0.1:5000/message`
