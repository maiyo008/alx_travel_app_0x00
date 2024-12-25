# AirBnB Project
# ALX Travel App 0x00

## Description

This project is an extended version of the `alx_travel_app`. It focuses on defining database models, creating serializers for API data representation, and implementing a management command to seed the database with sample data. This README provides setup instructions and a guide to the main functionalities.

---

## Features

1. **Database Models**:  
   - `Listing`: Represents travel accommodations or properties.  
   - `Booking`: Represents user reservations for listings.  
   - `Review`: Represents user reviews for listings.

2. **API Serializers**:  
   - Serialize `Listing` and `Booking` data for API responses.

3. **Database Seeder**:  
   - A management command to populate the database with sample listings.

---

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- SQLite (default database for Django)

### Clone the Repository

```bash
git clone <repository-url>
cd alx_travel_app_0x00
