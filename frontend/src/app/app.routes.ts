import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: "tickets",
        loadComponent: () => import("./pages/tickets/lista/lista").then(m => m.Lista),
    }
];
