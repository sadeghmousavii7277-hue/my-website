import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mousavi.settings')
django.setup()

from django.contrib.auth.models import User, Group

# Create Manager group
manager_group, created = Group.objects.get_or_create(name='Manager')

# Create Manager user
username = 'manager_admin'
password = 'manager_password123'

if not User.objects.filter(username=username).exists():
    user = User.objects.create_user(username=username, password=password, first_name='آقای مدیر')
    user.is_staff = True
    user.is_superuser = True # Give superuser to ensure full access if needed, or just Manager group
    user.save()
    user.groups.add(manager_group)
    print(f"User created successfully!\nUsername: {username}\nPassword: {password}")
else:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    user.groups.add(manager_group)
    print(f"User already existed, updated password.\nUsername: {username}\nPassword: {password}")
