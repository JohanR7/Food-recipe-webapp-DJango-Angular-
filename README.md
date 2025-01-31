

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

## 3. Backend Setup (Django)

### Prerequisites
- Python 3.9+
- pip package manager
- Virtual environment support
- Spoonacular API subscription

### Installation Steps
```bash
# Create project directory
mkdir recipe-search-project
cd recipe-search-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install django requests python-dotenv

# Create Django project
django-admin startproject recipe_search
cd recipe_search

# Create API app
python manage.py startapp api
```

### Configuration
1. `.env` File
```
SPOONACULAR_API_KEY=your_api_key_here
DEBUG=False
SECRET_KEY=your_django_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1,your-render-domain
```

2. `settings.py` Updates
```python
INSTALLED_APPS = [
    ...
    'api',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "https://your-frontend-domain.com"
]
```

## 4. Frontend Setup (Angular)

### Prerequisites
- Node.js 18+
- Angular CLI
- npm package manager

### Installation
```bash
# Install Angular CLI globally
npm install -g @angular/cli

# Create new Angular project
ng new recipe-frontend
cd recipe-frontend

# Install additional dependencies
npm install @angular/material
npm install bootstrap
```

### Project Structure
```
recipe-frontend/
│
├── src/
│   ├── app/
│   │   ├── components/
│   │   │   ├── search/
│   │   │   └── recipe-list/
│   │   ├── services/
│   │   │   └── recipe.service.ts
│   │   └── models/
│   │       └── recipe.model.ts
│   └── environments/
│       ├── environment.ts
│       └── environment.prod.ts
```

## 5. API Endpoint Details

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

## 6. Deployment

### Backend (Render)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn project.wsgi:application`
- **Environment**: Python
- **Region**: Choose closest to target audience

### Frontend (Render)
- **Build Command**: `npm install && ng build --configuration=production`
- **Publish Directory**: `dist/frontend`
- **Environment**: Static Site

## 7. Error Handling

### Possible Status Codes
- `200`: Successful request
- `400`: Invalid input
- `404`: No recipes found
- `500`: Server or API error

## 8. Performance Optimization
- Implement caching
- Use lazy loading
- Minimize API calls
- Implement debounce on search

## 9. Security Considerations
- Use environment variables
- Implement rate limiting
- Validate and sanitize inputs
- Use HTTPS
- Manage API key securely

## 10. Future Enhancements
- User authentication
- Save favorite recipes
- Nutritional information
- Advanced filtering

## 11. Troubleshooting
- Verify API connectivity
- Check network logs
- Validate environment configurations
- Monitor API usage limits

## 12. Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

