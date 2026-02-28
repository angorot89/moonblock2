#!/usr/bin/env python
"""Moonblock Setup — run once to initialize everything."""
import os, sys, subprocess

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moonblock.settings')

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout: print(r.stdout.strip())
    return r.returncode

print("=" * 55)
print("  MOONBLOCK — Full Setup with i18n + CMS")
print("=" * 55)

print("\n[1/5] Running migrations...")
run("python manage.py migrate")

import django; django.setup()
from store.models import SiteSettings, Category, Product

print("\n[2/5] Initialising Site Settings...")
SiteSettings.get()
print("  Site settings ready.")

print("\n[3/5] Creating sample categories...")
cats = [
    ("Hoodies & Sweats", "هوديز وسويتشيرت", "Sweats & Hoodies", "hoodies-sweats", 1),
    ("Gym Wear", "ملابس جيم", "Tenue de Gym", "gym-wear", 2),
    ("Bottoms", "بنطلونات", "Bas", "bottoms", 3),
    ("Accessories", "إكسسوارات", "Accessoires", "accessories", 4),
    ("Outerwear", "ملابس خارجية", "Outerwear", "outerwear", 5),
]
for en, ar, fr, slug, order in cats:
    cat, created = Category.objects.get_or_create(slug=slug, defaults={"name_en": en, "name_ar": ar, "name_fr": fr, "order": order})
    print(f"  {'Created' if created else 'Exists'}: {en}")

print("\n[4/5] Creating admin user...")
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@moonblock.com', 'moonblock2026')
    print("  Admin created: admin / moonblock2026")
    print("  ⚠️  Change password after first login!")
else:
    print("  Admin already exists.")

print("\n[5/5] Done!\n")
print("=" * 55)
print("  Start server:  python manage.py runserver")
print("  Website:       http://127.0.0.1:8000/")
print("  Admin:         http://127.0.0.1:8000/admin/")
print("  Login:         admin / moonblock2026")
print()
print("  ADMIN FEATURES:")
print("  ✦ Site Settings — edit ALL text in EN/AR/FR")
print("  ✦ Products      — add items with images & sizes")
print("  ✦ Categories    — manage with translations")
print("  ✦ Lookbook      — add/reorder photo gallery")
print("  ✦ Orders        — view & update order status")
print("=" * 55)
