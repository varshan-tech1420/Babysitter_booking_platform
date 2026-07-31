# Problem Statement

## 1. Title
Babysitter Booking Platform

## 2. Domain
Web Application

## 3. Who is the user?
- Parent
- Babysitter
- Admin

## 4. What problem are we solving?
Parents often face difficulty finding trustworthy babysitters on short notice. Traditional methods rely on personal references and phone calls, making the process slow and unreliable. There is no centralized platform to compare babysitters, check availability, and book their services. This project aims to simplify and secure the babysitter booking process.

## 5. Proposed Solution
The Babysitter Booking Platform is a web application that allows parents to search for available babysitters, view their profiles, book appointments, and manage bookings. Babysitters can update their availability, while administrators manage users and monitor the platform.

## 6. Core Entities / Database Tables
- User
- Parent
- Babysitter
- Booking
- Payment
- Review

## 7. User Roles & Permissions

### Admin
- Manage users
- Manage babysitters
- View all bookings
- Monitor payments

### Parent
- Register and login
- Search babysitters
- Book babysitters
- View booking history
- Make payments

### Babysitter
- Register and login
- Update profile
- Set availability
- Accept or reject bookings

## 8. Success Criteria
- Parents can register and log in successfully.
- Parents can search and book babysitters.
- Babysitters can manage their availability.
- Admin can manage users and bookings.
- Booking information is stored correctly in the database.

## 9. Out of Scope
- Video calling
- GPS live tracking
- Mobile application
- AI-based babysitter recommendation

## 10. Chosen Track
Python (Django)