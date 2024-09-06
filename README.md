# Pun-O-Meter

**Pun-O-Meter** is a Django-based web application that allows users to submit puns and rate them based on their humor. The application features real-time updates for ratings and a leaderboard showcasing the top punsters. This project is designed to be both fun and functional, making it a great example of Django's capabilities in handling WebSocket connections and real-time interactions.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Pun Submission**: Users can submit their own puns.
- **Rating System**: Users can rate puns, and ratings are updated in real-time.
- **Real-Time Updates**: Using Django Channels, the average rating for puns is updated live without needing to refresh the page.
- **Leaderboard**: Displays top punsters based on their rating contributions.

## Technologies Used

- **Django**: Web framework for building the application.
- **Django Channels**: For handling WebSocket connections and real-time updates.
- **Redis**: Used as the channel layer backend for Django Channels.
- **HTML/CSS**: For the frontend styling and user interface.
- **JavaScript**: For handling WebSocket communication and dynamic content updates.

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/pun_o_meter.git
    cd pun_o_meter
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run Redis Server**:
    ```bash
    redis-server
    ```

6. **Run the Django Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Run Daphne for WebSockets**:
    ```bash
    daphne -b 0.0.0.0 -p 8000 pun_o_meter.asgi:application
    ```

8. **Access the Application**: Open your browser and go to `http://127.0.0.1:8000/` to start using the app.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Whether it’s a bug fix, feature request, or improvement, your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
