# Holistic Web Application

A comprehensive web application for holistic wellness services including booking, testimonials, blog management, and more.

## Features

- **Booking System**: Schedule and manage appointments
- **Blog Management**: Create and manage blog posts
- **Testimonials**: Collect and display client testimonials
- **Admin Panel**: Administrative interface for managing the application
- **Authentication**: User authentication and authorization
- **Social Media Integration**: Facebook posting capabilities

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your actual API keys and credentials
   ```

3. Run the application:
   ```bash
   python start_app.py
   ```

## Project Structure

- `features/` - Modular feature implementations
- `routes/` - Flask route handlers
- `templates/` - HTML templates
- `static/` - Static assets (CSS, JS, images)
- `db/` - Database models and configuration
- `utils/` - Utility functions and helpers

## Technologies Used

- Flask (Python web framework)
- SQLite (Database)
- HTML/CSS/JavaScript (Frontend)
- Bootstrap (UI framework)
