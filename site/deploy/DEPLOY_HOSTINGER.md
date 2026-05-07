# Déploiement VPS Hostinger — Zion Garden

## 1) Pré-requis
- VPS Ubuntu (22.04/24.04)
- Domaine pointé vers l'IP du VPS (`A` record)
- Accès SSH root ou sudo

## 2) Installer Nginx + Certbot
```bash
sudo apt update
sudo apt install -y nginx certbot python3-certbot-nginx
```

## 3) Créer dossier site
```bash
sudo mkdir -p /var/www/zion-garden
sudo chown -R $USER:$USER /var/www/zion-garden
```

## 4) Uploader le contenu du dossier `site/`
Depuis ton poste local:
```bash
scp -r ./site/* user@TON_IP_VPS:/var/www/zion-garden/
```

## 5) Activer la config Nginx
- Copier `deploy/nginx-zion-garden.conf` vers `/etc/nginx/sites-available/zion-garden`
- Adapter les domaines (`zion-garden.be`, `www.zion-garden.be`)

```bash
sudo ln -s /etc/nginx/sites-available/zion-garden /etc/nginx/sites-enabled/zion-garden
sudo nginx -t
sudo systemctl reload nginx
```

## 6) Activer HTTPS
```bash
sudo certbot --nginx -d zion-garden.be -d www.zion-garden.be
```

## 7) Vérifications
- https://zion-garden.be
- https://zion-garden.be/privacy.html
- https://zion-garden.be/robots.txt
- https://zion-garden.be/sitemap.xml

## 8) Mise à jour continue
Pour publier une nouvelle version:
```bash
scp -r ./site/* user@TON_IP_VPS:/var/www/zion-garden/
```

## 9) Post-déploiement marketing
- Remplacer `GTM-XXXXXXX` dans les pages par l'ID réel GTM
- ✅ Formspree déjà configuré (ID: fa222847ba1b23bc)
- ✅ Numéros de téléphone mis à jour (+32 466 33 79 32)
- ✅ Sitemap enrichi (7 pages)
- ✅ WhatsApp configuré
- Soumettre `sitemap.xml` dans Google Search Console
