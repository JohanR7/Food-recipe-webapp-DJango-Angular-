from django.http import JsonResponse
from api.utils import fetch  # Import the updated fetch function

def search_recipes(request):
    query = request.GET.get("query", "")

    if not query:
        return JsonResponse({"error": "Query parameter 'query' is required."}, status=400)

    try:
        response = fetch(
            "recipes/complexSearch",
            params={
                "query": query,
                "number": 10,  # Get up to 10 results
                "addRecipeInformation": True,  # Get full details
                "fillIngredients": True  # Fetch ingredient info
            }
        )

        if "error" in response:
            return JsonResponse(response, status=500)

        # Debugging - Print raw API response
        print("Raw API response:", response)

        if not response or "results" not in response:
            return JsonResponse({"message": "No results found."}, status=404)

        # Transform response to match frontend
        transformed_results = [
            {
                "name": recipe.get("title", ""),
                "description": f"Ready in {recipe.get('readyInMinutes', 'N/A')} minutes. Servings: {recipe.get('servings', 'N/A')}.",
                "image": recipe.get("image", ""),
                "cuisine": ", ".join(recipe.get("cuisines", ["Unknown"])),  # Cuisine type
                "foodType": ", ".join(recipe.get("dishTypes", ["General"])),  # Dish type (dessert, main, etc.)
                "difficulty": (
                    "Easy" if recipe.get("readyInMinutes", 60) <= 30 else
                    "Medium" if recipe.get("readyInMinutes", 60) <= 60 else
                    "Hard"
                ),
                "recipeUrl": recipe.get("sourceUrl", "#")  # Link to full recipe
            }
            for recipe in response.get("results", [])
        ]

        print("Transformed response:", transformed_results)  # Debugging

        return JsonResponse(transformed_results, safe=False)

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debugging
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
