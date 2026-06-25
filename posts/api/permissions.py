from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff

# con esta configuracion de permisos todos los usuarios pueden leer
# pero solo los admins pueden editar, publicar, eliminar
        
