Little Lemon API - Endpoints à tester
=====================================

Menu API
---------
- /api/menu-items/               -> Liste des plats (GET, POST si authentifié)
- /api/menu-items/<id>/          -> Détail d’un plat (GET, PUT, DELETE)

Booking API
------------
- /api/booking/tables/           -> Réservations (GET, POST, PUT, DELETE)

Authentification
-----------------
- /auth/token/login/             -> Obtenir un token (POST : username, password)
- /auth/token/logout/            -> Supprimer un token (POST)
- /auth/users/                   -> Créer un nouvel utilisateur (POST)

Exemple d’utilisation
---------------------
1. Créez un utilisateur avec : POST /auth/users/
2. Connectez-vous avec : POST /auth/token/login/
3. Copiez le token reçu et utilisez-le pour tester les autres endpoints.
