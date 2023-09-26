﻿# DDobok-backend

![Alt Text](https://user-images.githubusercontent.com/79842380/215327372-cb503153-8156-4b2a-9dd0-713d2e610d2b.gif)

- [Frontend Repository](https://github.com/SeokyoungYou/DDobok-frontend)
- Deployed with [render](https://render.com/)
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
