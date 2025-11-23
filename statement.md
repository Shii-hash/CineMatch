# Project Statement

## 1. Problem Statement
Traditional manual movie ticketing systems suffer from inefficiency, human calculation errors, and a lack of real-time seat tracking. This often leads to issues such as double-booking seats and difficulty in maintaining accurate sales records for theater managers.

## 2. Scope of the Project
The project is a Command Line Interface (CLI) based "Theater Management System" that:
* Digitalizes the ticket booking process.
* Manages a database of movies, prices, and live seat inventories.
* Automates cost calculations to prevent billing errors.
* Maintains a persistent history of all transactions using file-based storage.

## 3. Target Users
* **Small City Theater Managers:** This can be used by small theaters.
* **Customers:** To check seat availability in real-time and book tickets instantly.

## 4. High-Level Features
* **Real-time Seat Tracking:** The system automatically updates the seat count after every booking to prevent overbooking.
* **Data Persistence:** All data (movie details and booking logs) is stored in text files, ensuring records are saved even if the program is closed.
* **Smart Validation:** The system prevents invalid inputs, such as booking negative tickets or selecting non-existent movie IDs.
* **Transaction Logging:** Every successful booking generates a digital log entry with the user's name, movie, and total cost.
