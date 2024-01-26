# Crie um arquivo python, como create_groups.py

# Importe os modelos do Django necessários
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

# Crie uma função para criar grupos e atribuir permissões
def create_groups():
    # Crie um grupo
    group, created = Group.objects.get_or_create(name='Usuarios')

    # Exemplo de atribuição de permissões
    # Aqui, você precisa identificar os tipos de conteúdo e as permissões
    content_type = ContentType.objects.get_for_model(MeuModelo)

    # Adicione permissões específicas
    permission = Permission.objects.create(
        codename='pode_fazer_algo',
        name='Pode Fazer Algo',
        content_type=content_type,
    )

    # Adicione permissões ao grupo
    group.permissions.add(permission)

    # Salve o grupo
    group.save()

# Chame a função para criar grupos
create_groups()
