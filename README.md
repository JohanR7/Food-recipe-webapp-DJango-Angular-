

# 🍲 Food Recipe Search Application

## 1. Project Overview

### Purpose
A full-stack web application enabling users to search and discover food recipes using modern web technologies and the Spoonacular API.

### Key Features
- Real-time recipe search
- Detailed recipe information
- Responsive design
- API-driven content
- Error handling and user feedback

## 2. System Architecture

### Backend (Django)
- **Framework**: Django 4.x
- **Language**: Python 3.9+
- **API Integration**: Spoonacular REST API
- **Data Flow**: 
  1. Receive search query
  2. Validate input
  3. Fetch recipes from external API
  4. Transform and return structured data

### Frontend (Angular)
- **Framework**: Angular 19.x
- **Language**: TypeScript
- **State Management**: RxJS
- **Routing**: Angular Router
- **Components**: 
  - Search input
  - Recipe list
  - Recipe details

## 3. Running the Project Locally

### Backend (Django)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JohanR7/Food-recipe-webapp-DJango-Angular-.git
   cd backend
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

### Frontend (Angular)

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the Angular development server**:
   ```bash
   ng serve
   ```

4. **Access the application**:
   Open your browser and go to `http://localhost:4200` to view the application.

## 4. API Endpoint Details

### Request Specification
- **URL**: `/search_recipes`
- **Method**: GET
- **Parameters**:
  - `query` (required): Recipe search term
  - `number` (optional): Max results (default: 10)

### Response Structure
```json
[ 
  {
    "name": "Pasta Carbonara",
    "description": "Ready in 20 minutes. Servings: 2.",
    "image": "https://spoonacular.com/recipeImages/123456-312x231.jpg",
    "cuisine": "Italian",
    "foodType": "Main Course",
    "difficulty": "Medium",
    "recipeUrl": "https://spoonacular.com/pasta-carbonara"
  }
]
```

### Example Response
```json
[
  {
    "name": "Chicken Alfredo",
    "description": "Ready in 30 minutes. Servings: 4.",
    "image": "https://spoonacular.com/recipeImages/654321-312x231.jpg",
    "cuisine": "Italian",
    "foodType": "Main Course",
    "difficulty": "Medium",
    "recipeUrl": "https://spoonacular.com/chicken-alfredo"
  },
  {
    "name": "Chocolate Cake",
    "description": "Ready in 50 minutes. Servings: 8.",
    "image": "https://spoonacular.com/recipeImages/987654-312x231.jpg",
    "cuisine": "American",
    "foodType": "Dessert",
    "difficulty": "Hard",
    "recipeUrl": "https://spoonacular.com/chocolate-cake"
  }
]
```

## 5. Deployment

### Backend (Render)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn project.wsgi:application`
- **Environment**: Python
- **Region**: Choose closest to target audience
- **URL**: [Recipe Search API](https://customuser-2u8d.onrender.com/search_recipes)

### Frontend (Render)
- **Build Command**: `npm install && ng build --configuration=production`
- **Publish Directory**: `dist/frontend`
- **Environment**: Static Site
- **URL**: Coming soon
## 6. Error Handling

### Possible Status Codes
- `200`: Successful request
- `400`: Invalid input
- `404`: No recipes found
- `500`: Server or API error

## 7. Performance Optimization
- Implement caching
- Use lazy loading
- Minimize API calls
- Implement debounce on search

## 8. Security Considerations
- Use environment variables
- Implement rate limiting
- Validate and sanitize inputs
- Use HTTPS
- Manage API key securely

## 9. Future Enhancements
- User authentication
- Save favorite recipes
- Nutritional information
- Advanced filtering

## 10. Troubleshooting
- Verify API connectivity
- Check network logs
- Validate environment configurations
- Monitor API usage limits

## 11. Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

