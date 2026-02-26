# MOONBLOCK — Django E-Commerce (Full CMS + EN/AR/FR)

## Quick Start

```bash
# 1. Install
pip install -r requirements.txt

# 2. Setup DB + admin + sample data (run once)
python setup.py

# 3. Run
python manage.py runserver
```

- **Site**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/ (admin / moonblock2026)

---

## Admin Panel — What You Can Edit

### 🌐 Site Settings (everything on the site)
Go to **Store → Site Settings** to edit:
- Hero section (title, subtitle, CTA buttons) in EN + AR + FR
- Scrolling ticker text in all 3 languages
- "New Arrivals" section title
- "About" section — both paragraphs, stats (4K+, 32, 100%)
- "Categories" section heading
- Newsletter section text
- Footer tagline
- Social media links (IG, TikTok, X)
- All navigation labels

### 📦 Products
- Add product name in EN + AR + FR
- Add description in all 3 languages
- Upload up to 3 product images
- Set price, sale price, stock, sizes
- Toggle: Active, Featured, New

### 📂 Categories
- Create/edit categories with names in EN + AR + FR
- Set display order

### 📸 Lookbook
- Upload lookbook images
- Add title + caption in EN + AR + FR
- Set order and toggle active/inactive

### 📋 Orders
- View all orders with customer info
- Update status: Pending → Processing → Shipped → Delivered

### 📧 Newsletter
- View all subscribers

---

## Language Switching
Users can switch between EN / AR / FR using the buttons in the nav.
Arabic enables full RTL layout automatically.

## File Structure
```
moonblock2/
├── manage.py
├── setup.py           ← Run first!
├── requirements.txt
├── db.sqlite3         ← Created after setup
├── media/
│   ├── products/      ← Product images uploaded here
│   └── lookbook/      ← Lookbook images uploaded here
├── moonblock/         ← Django settings
└── store/             ← Main app
    ├── models.py      ← All database models
    ├── views.py       ← Page logic
    ├── admin.py       ← Admin panel configuration
    ├── middleware.py  ← Language detection
    ├── context_processors.py
    ├── templatetags/
    │   └── moonblock_tags.py  ← Translation helpers
    └── templates/store/
        ├── base.html
        ├── home.html
        ├── shop.html
        ├── product_detail.html
        ├── lookbook.html
        ├── cart.html
        ├── checkout.html
        └── order_success.html
```
