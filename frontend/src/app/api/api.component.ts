import { HttpClient } from '@angular/common/http';
import { Component, ViewEncapsulation } from '@angular/core';

interface Recipe {
  name: string;
  description: string;
  image: string;
  cuisine: string;
  foodType: string;
  difficulty: string;
  recipeUrl: string;
}

@Component({
  selector: 'app-api',
  standalone: false,
  templateUrl: './api.component.html',
  styleUrls: ['./api.component.css'],
  encapsulation: ViewEncapsulation.None,
})
export class ApiComponent {
  item: string = '';
  results: Recipe[] = [];
  loading: boolean = false;
  errorMessage: string = '';

  constructor(private http: HttpClient) {}

  searchRecipe() {
    if (this.item.trim()) {
      this.loading = true;
      this.errorMessage = '';
      this.results = [];

      console.log('Searching for:', this.item);
      const apiUrl = `http://localhost:8000/api/search_recipes/?query=${this.item}`;
      console.log('Making request to:', apiUrl);
      
      this.http.get<Recipe[]>(apiUrl).subscribe({
        next: (response) => {
          console.log('Received response:', response);
          this.results = response;
          this.loading = false;
        },
        error: (error) => {
          console.error('Error fetching data:', error);
          this.errorMessage = 'Failed to fetch recipes. Please try again.';
          this.loading = false;
        },
        complete: () => {
          console.log('Request completed');
        }
      });
    }
  }
}
