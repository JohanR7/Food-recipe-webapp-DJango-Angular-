import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ApiComponent } from './api/api.component';  // Import your components

const routes: Routes = [
  { path: '', component: ApiComponent },  // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],  // Add routes here
  exports: [RouterModule]
})
export class AppRoutingModule { }
