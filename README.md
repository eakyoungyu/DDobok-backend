# DDobok-backend

![Alt Text](https://user-images.githubusercontent.com/79842380/215327372-cb503153-8156-4b2a-9dd0-713d2e610d2b.gif)

- [Frontend Repository](https://github.com/SeokyoungYou/DDobok-frontend)

## Tools
- **[Render](https://render.com/)** for deployment
- **[Poetry](https://python-poetry.org/)** for python packaging
- **Django REST framework** for providing data to frontend
- **AWS S3** for image storage
---

## Rest API
#### Brand
GET /api/v1/brands: List every jiujitsu gi brand

#### Gi
GET /api/v1/gis/: List every jiujitsu gi (ordered by priority)
- filters: color, price, priority
- examples\
GET /api/v1/gis/?color=Black\
GET /api/v1/gis/?color=Black&color=White\
GET /api/v1/gis/?min_price=100000&max_price=200000\
GET /api/v1/gis/?color=Black&min_price=100000&max_price=200000
  
| Color |
|-------|
| Black |
| White |
| Blue |
| Bright |
| Dark |

---
## Models
#### Brand

| Brand        |
|------------------|
| - id: int (PK)   |
| - name: str      |
| - link_store: str|
| - link_sns: str  |
| + __str__(): str |

#### Gi

| Gi        |
|------------------|
| - id: int (PK)   |
| - name: str      |
| - photo: ImageField|
| - link_store: str|
| - price: int     |
| - priority: int  |
| - color: str     |
| - brand: Brand   |
| + __str__(): str |

#### Priority

| Priority        |
|------------------|
| + LOW: int       |
| + MID: int       |
| + HIGH: int      |
| + COMMERCIAL: int|

#### Color

| Color        |
|------------------|
| + BLACK: str     |
| + WHITE: str     |
| + BLUE: str      |
| + BRIGHT: str    |
| + DARK: str      |

#### Relationships:

- Gi ◆--> Priority (Gi has a Priority)
- Gi ◆--> Color (Gi has a Color)
- Brand --> Gi (Gi belongs to a Brand)
