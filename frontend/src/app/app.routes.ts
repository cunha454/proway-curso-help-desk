import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: "tickets",
        loadComponent: () => import("./pages/tickets/lista/lista").then(m => m.Lista),
    },
    {
        path: "tickets/cadastro",
        loadComponent: () => import("./pages/tickets/cadastro/cadastro").then(m => m.Cadastro)
    },
];
