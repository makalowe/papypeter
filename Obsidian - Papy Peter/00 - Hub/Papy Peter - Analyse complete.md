# Papy Peter by Zion Garden — Analyse complète

**Date** : 2026-05-06
**Statut** : MVP en ligne + prospection active
**Tags** : #projet #permaculture #site-web #crm #marketing

---

## 1. Vision

**Papy Peter** est le personal branding de Pierre, fondateur de **Zion Garden**. Mission : devenir la référence en Wallonie et Belgique pour la permaculture appliquée, les jardins thérapeutiques et la transmission pratique. Le projet couvre toute la chaîne : site web, CRM prospection, marketing de contenu, et personal branding.

---

## 2. Les 4 piliers du projet

```
┌─────────────────────────────────────────────────────────────┐
│                     PAPY PETER / ZION GARDEN                 │
├───────────────────┬──────────────────┬──────────────────────┤
│   1. Site web     │  2. CRM &        │  3. Marketing        │
│   (Vitrine +      │  Prospection     │  Contenu             │
│    Blog)          │                  │                      │
├───────────────────┼──────────────────┼──────────────────────┤
│  HTML/CSS/JS      │  Google Sheets   │  Calendrier éditorial│
│  statique         │  + Python        │  14 jours            │
│  Hostinger VPS    │  + Apollo CRM    │  Podcast, réseaux    │
│  Formspree        │  + n8n (futur)   │  Lead magnet PDF     │
├───────────────────┼──────────────────┼──────────────────────┤
│  4. Personal Branding │                                    │
│  Bio officielle, slogans, kit branding, charte              │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Arborescence du projet

```
02 - Papy Peter Permaculture/
│
├── site/                                  # 🌐 SITE WEB (statique)
│   ├── index.html                         # Page d'accueil one-page (13 sections)
│   ├── about.html                         # À propos
│   ├── tarifs.html                        # Tarifs indicatifs
│   ├── temoignages.html                   # Témoignages
│   ├── blog.html                          # Blog (listing)
│   ├── privacy.html                       # Confidentialité
│   ├── merci.html                         # Page confirmation formulaire
│   ├── styles.css                         # CSS complet (12 KB)
│   ├── blog.js                            # Blog dynamique (fetch JSON)
│   ├── track.js                           # Tracking GTM (WhatsApp, formulaires)
│   ├── robots.txt                         # SEO
│   ├── sitemap.xml                        # 4 URLs seulement
│   ├── deploy/                            # Déploiement Hostinger
│   │   ├── DEPLOY_HOSTINGER.md
│   │   └── nginx-zion-garden.conf
│   ├── assets/                            # 12 images (logos, photos terrain)
│   └── data/posts.json                    # 3 articles blog
│
├── GoogleDrive - Zion Garden - Pilotage/  # 📁 DRIVE MIROIR
│   ├── 01_Strategie/                      # Roadmap, plan, études
│   ├── 02_CRM_Prospects/                  # Fichiers CRM + scripts Python
│   ├── 03_Marketing_Contenu/              # Branding, calendrier, podcasts
│   ├── 04_Site_Web/                       # Backup du site
│   └── 05_Administratif/                  # Boards, sections
│
├── Obsidian - Papy Peter/                 # 📓 SECOND CERVEAU
│   ├── 00 - Hub/Papy Peter - Hub.md
│   ├── 01 - Strategie/01 - Strategie.md
│   ├── 02 - Site/02 - Site.md
│   ├── 03 - CRM Prospection/03 - CRM Prospection.md
│   ├── 04 - Contenu Marketing/04 - Contenu Marketing.md
│   └── 05 - Operations/05 - Operations.md
│
├── *.md (racine)                          # 25+ fichiers de stratégie
├── *.csv / *.xlsx                         # CRM, prospects, scoring
├── *.py                                   # Scripts CRM dashboard
├── Sales Assets - Apollo/                 # Profils Apollo.io
├── photo videos/                          # 40+ photos terrain
├── blue eco/                              # Ressources Blue Economy
└── node-ts-rides-api/                     # Projet API (indépendant)
```

---

## 4. Site web — Détail

### Stack
| Technologie | Usage |
|---|---|
| **HTML5** statique | 7 pages |
| **CSS3** vanilla | 1 fichier `styles.css` (~12 KB) |
| **JavaScript** vanilla | `blog.js` (fetch JSON → DOM) + `track.js` (GTM events) |
| **Google Tag Manager** | Tracking : clics WhatsApp, email, téléphone, formulaires |
| **Formspree** | Backend des formulaires de contact |
| **Nginx** | Serveur HTTP (Hostinger VPS) |
| **Let's Encrypt** | HTTPS |

### Pages
| Page | Contenu |
|---|---|
| `index.html` | One-page : Hero, Offres (4 packs), Bio, Blog, Guide gratuit, Entreprises/CSE, Méthode, Thérapeutique, Preuves, Témoignages, Conférences, Contact, FAQ |
| `about.html` | Bio Papy Peter + mission |
| `tarifs.html` | Grille tarifaire indicative |
| `temoignages.html` | Témoignages clients |
| `blog.html` | Liste des articles (via `posts.json`) |
| `privacy.html` | Politique de confidentialité |
| `merci.html` | Confirmation post-formulaire |

### Design
- Thème **dark nature** : fond #0e100f, texte #f4f1df, accents or #e4cf63
- Typo : Space Grotesk (sans-serif) + Merriweather (serif titres)
- Animations : `rise` (fade-in + translateY), hover sur les cartes
- Responsive : oui (breakpoint 980px et 700px), mais menu déborde en mobile

### Fonctionnalités
- ✅ Blog dynamique (JSON → rendu JS)
- ✅ Tracking GTM : WhatsApp, email, téléphone, formulaires
- ✅ Formulaire guide gratuit avec segmentation (école, entreprise, particulier, soins)
- ✅ Formulaire devis avec sélection du type de projet
- ✅ Honeypot anti-spam
- ✅ Consentement RGPD
- ✅ Sitemap + robots.txt
- ✅ Open Graph + Twitter Cards
- ✅ JSON-LD (Organization + ContactPoint + Social)
- ✅ Page merci après formulaire

---

## 5. CRM & Prospection

### Stack CRM
| Technologie | Usage |
|---|---|
| **Google Sheets** | Base de données CRM principale |
| **Apollo.io** | Enrichissement contacts B2B |
| **Python** | Scripts de scoring et dashboard |
| **CSV** | Exports batchs de prospection |

### Fichiers CRM
| Fichier | Contenu |
|---|---|
| `CRM Prospects - Wave 1 (30).csv` | 30 prospects qualifiés |
| `Prospects - Mons Wallonie (100).csv` | 100 prospects Mons |
| `Prospects - Mons Wallonie (100) - Qualified.csv` | Version qualifiée |
| `Scoring Priorite A - Batch 01.csv` | Scoring priorité |
| `Enrichissement Contacts - Batch 01.csv` | Données enrichies |
| `Suivi Outreach - Batch 01.csv` | Suivi des relances |

### Scripts Python
| Script | Rôle |
|---|---|
| `crm_zion_dashboard.py` | Dashboard CRM automatisé (Streamlit ?) |
| `qualify_prospects_batch.py` | Scoring et qualification automatique |

---

## 6. Marketing de contenu

### Calendrier éditorial 14 jours
- Jour 1 : Facebook + LinkedIn — Conseil de la semaine
- Jour 2 : Instagram Reel + TikTok — Astuce terrain 30s
- Jour 3 : Facebook — Jardin thérapeutique
- Jour 4 : LinkedIn — Autorité / Blue Economy
- Jour 5 : Instagram + Facebook — Avant/Après terrain
- Jour 6 : TikTok — Mythe vs réalité
- Jour 7 : Tous réseaux — Récap semaine
- Semaine 2 : même structure, angles différents

### Lead magnets
| Fichier | Contenu |
|---|---|
| `Calendrier des cultures - Wallonie (cadeau).pdf` | Guide gratuit |
| `Calendrier des cultures - Wallonie - Zion Garden (lead magnet).pdf` | Version lead magnet |

### Personal branding
- **Kit Personal Branding - Papy Peter.md** : bio, messages clés, positionnement
- **Bio officielle - Papy Peter.md** : bio validée
- **Slogans - Zion Garden.md** : slogans
- **Scripts podcast - Semaine 1.md** : 7 scripts podcast

---

## 7. Points forts

### Site web
- Design dark/or cohérent et élégant
- CTA clairs et visibles (WhatsApp, devis, guide gratuit)
- Tracking GTM complet (tous les événements importants)
- SEO présent (JSON-LD, OG, sitemap, robots.txt)
- Blog fonctionnel avec JSON
- Formulaire segmenté (type de structure)
- Anti-spam honeypot + RGPD
- Page merci dédiée

### Stratégie
- Roadmap claire avec phases et KPI (Phase 0-5 + backlog)
- Prospection structurée (batchs CSV, scoring, suivi)
- Calendrier éditorial solide (14 jours, cross-plateforme)
- Lead magnet défini (calendrier des cultures)
- Kit branding complet (bio, slogans, profile Apollo)

---

## 8. Problèmes identifiés

### 🔴 Critique
| Problème | Détail |
|---|---|
| **Formspree pas configuré** | `REPLACE_WITH_YOUR_FORM_ID` dans les formulaires — aucun prospect reçu |
| **3 articles blog seulement** | Tous avec `url: "#"` — pas de vraies pages indexables |
| **Sitemap incomplet** | Seulement 4 URLs (manquent blog.html, temoignages.html) |
| **Menu mobile illisible** | Les liens du menu passent à la ligne sur mobile (pas de hamburger) |

### 🟡 Forte priorité
| Problème | Détail |
|---|---|
| **Images non optimisées** | Pas de lazy loading, pas de WebP, pas de CDN |
| **CSS/JS non minifié** | styles.css = 12 KB transportés en brut |
| **Blog sans SEO** | Pas de page article dédiée, pas d'URL de slug, pas de maillage interne |
| **Aucune landing page SEO** | Pas de page "jardin thérapeutique Belgique" ou "potager école Wallonie" |
| **Tracking URL locale** | Même problème que Zion Tour — tracking sur localhost |

### 🟢 Priorité moyenne
| Problème | Détail |
|---|---|
| **Pas de galerie avant/après** | Les photos existent dans `assets/` (avant.jpg, apres.jpg) mais ne sont pas exploitées |
| **Pas de newsletter** | Pas d'intégration Brevo ou Mailchimp pour le lead magnet |
| **Pas de témoignages vidéo** | Les vidéos existent dans `photo videos/` mais ne sont pas sur le site |
| **Pas de numéro réel** | `+32 00 00 00 00` — numéro fictif partout |
| **WhatsApp lien #** | `href="#"` au lieu d'un vrai lien wa.me |

---

## 9. Plan d'exécution recommandé

### Phase 0 — Corrections immédiates (1 jour)
| Action | Fichier | Temps |
|---|---|---|
| Remplacer `REPLACE_WITH_YOUR_FORM_ID` par vrai ID Formspree | `index.html` | 5 min |
| Remplacer `+32 00 00 00 00` par vrai numéro | `index.html`, `tarifs.html` | 5 min |
| Remplacer `href="#"` WhatsApp par vrai lien | `index.html` | 2 min |
| Ajouter `blog.html` + `temoignages.html` dans `sitemap.xml` | `sitemap.xml` | 5 min |
| Créer `robots.txt` avec sitemap | `robots.txt` | 2 min |

### Phase 1 — SEO & Contenu (semaine 1)
| Action | Détail |
|---|---|
| Créer 8 articles blog avec vraies pages HTML | `site/articles/*.html` |
| Mettre à jour `posts.json` avec vraies URLs | `data/posts.json` |
| Ajouter les pages dans le sitemap | `sitemap.xml` |
| Créer landing page "Jardin thérapeutique Belgique" | Nouveau fichier |
| Créer landing page "Potager école Wallonie" | Nouveau fichier |

### Phase 2 — Performance & UX (semaine 2)
| Action | Détail |
|---|---|
| Minifier CSS/JS | `styles.css`, `blog.js`, `track.js` |
| Ajouter lazy loading images | Attribut `loading="lazy"` |
| Convertir images en WebP | `/assets/*.webp` |
| Remplacer menu par hamburger | CSS + JS menu toggle |
| Ajouter galerie avant/après | Nouvelle section + JS |
| Ajouter Calendly réservation | Lien intégré |

### Phase 3 — Conversion & Tracking (semaine 3)
| Action | Détail |
|---|---|
| Newsletter Brevo (lead magnet guide gratuit) | Intégration API |
| Ajouter Microsoft Clarity (heatmap) | Script dans le head |
| Ajouter UTM tracking aux liens | Paramètres dans tous les CTA |
| Ajouter scroll depth tracking | GTM event |
| Ajouter page "Merci" avec contenu dynamique | `merci.html` |

---

## 10. Dashboard KPI

| Indicateur | Cible 90 jours | Statut |
|---|---|---|
| Pages indexées Google | 10+ | ❌ 4 |
| Articles blog publiés | 12 | ❌ 3 (placeholders) |
| Demandes devis via formulaire | 20 | ❌ Formspree pas configuré |
| Taux de clic WhatsApp | — | ❌ Pas mesurable |
| Visiteurs mensuels | — | ❌ Pas de GA4 configuré |

---

## 11. Flux de conversion cible

```
Réseaux sociaux (Facebook, Insta, TikTok, LinkedIn)
    │
    ▼
Site web (blog, landing pages, guides)
    │
    ├──➤ Guide gratuit (lead magnet) → Email → Newsletter
    │
    ├──➤ WhatsApp direct → Conversation → Devis
    │
    ├──➤ Formulaire devis → Formspree → Email → Relance
    │
    └──➤ Calendly → Rendez-vous téléphone → Proposition → Signature
```

---

## 12. Concurrence & positionnement

| Concurrent | Positionnement | Différence Papy Peter |
|---|---|---|
| Permaculture Design | International, en ligne | Local Wallonie, terrain |
| Jardins thérapeutiques FR | France, institutionnel | Belgique, toutes échelles |
| Paysagistes classiques | Esthétique | Pédagogique + thérapeutique |
| Formateurs permaculture | Théorique | **Terrain + transmission + Blue Economy** |

---

## 13. Liens utiles

- Dossier projet : `C:\Users\MIMBI\OneDrive\Bureau\02 - Papy Peter Permaculture`
- Site (local) : `./site/index.html`
- Déploiement Hostinger : `./site/deploy/DEPLOY_HOSTINGER.md`
- Obsidian Hub : `Obsidian - Papy Peter/00 - Hub/Papy Peter - Hub.md`

Projets connexes :
- [[Zion Tour]] — Agence booking artistique, même fondateur
- [[Campus Plus]] — E-learning, partage possible de l'infra VPS

---

## 14. Journal de mise à jour

- 2026-05-06 : Analyse complète du projet
- 2026-04-29 : Vérification formulaire
- 2026-04-23 : Création contexte global CRM
- 2026-04-20 : Roadmap site + branding
