# Pet Adoption System

## Overview
This system provides a platform to adopt and return pets

1. **Admin**: Manages pets in the system.

2. **User**: Adopts a pet or returns a pet.

## Features

### Admin Routes
1. **View All Pets**
   - **Endpoint**: `GET /admin/pets`
   - **Description**: Displays all pets with their details.
   - **How to Access**: Navigate to `/admin/pets` after logging in as an admin.

2. **Add a New Pet**
   - **Endpoint**: `POST /admin/pets`
   - **Description**: Allows the admin to add a new pet with details like type, breed, age.
  

3. **Update Pet Details**
   - **Endpoint**: `PUT /admin/pets/<pet_id>`
   - **Description**: Updates the details of a specific pet.
   - **How to Access**: Navigate to `/admin/pets`, enter id of the pet and updated details and submit.

4. **Delete a Pet**
   - **Endpoint**: `DELETE /admin/pets/<pet_id>`
   - **Description**: Deletes a specific pet using petId
   - **How to Access**: Navigate to `/admin/pets`, enter the petId, and enter.

### User Routes
1. **Search for pets by type**
   - **Endpoint**: `POST /pets`
   - **Description**: Displays all available pets related to the type entered by user
   - **How to Access**: Navigate to `/pets` after logging in as a user, enter the type of pet you want and enter.

2. **Adopt a pet**
   - **Endpoint**: `POST /pets/adopt`
   - **Description**: Allows the user to adopt a pet.
   - **How to Access**: Enter the petId of the pet you want to adopt and press enter

3. **Return a pet**
   - **Endpoint**: `POST /pets/return`
   - **Description**: Returns the adopted pet
   - **How to Access**: Navigate to `/pets/return`, enter the petId and press enter

## Getting Started
- Clone the repository: git clone https://github.com/your-username/your-repository.git
- Create and activate the virtual environment
- Install dependencies: pip install flask, Flask-SQLAlchemy
- Run the application: python app.py
- You can interact with the application using browser, thunder client and Postman

## Technologies Used
- **Backend**: Flask
- **Database**: SQLite
