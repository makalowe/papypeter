# Verification Formulaire - 2026-04-29

## Resultat
- Statut global: **bloque (test d'envoi impossible)**.

## Controles effectues
- Formulaire guide detecte: `site/index.html` ligne 125.
- Formulaire devis detecte: `site/index.html` ligne 411.
- Methode: `POST` sur Formspree.
- Champs anti-spam `_gotcha` presents.

## Bloquants identifies
- ID Formspree non configure:
  - `https://formspree.io/f/REPLACE_WITH_YOUR_FORM_ID` (lignes 125 et 411).
- WhatsApp encore placeholder:
  - `https://wa.me/32000000000` (lignes 96 et 401).
- GTM encore placeholder:
  - `GTM-XXXXXXX` (lignes 56 et 62).
- URL de redirection `_next` en localhost:
  - `http://127.0.0.1:5500/merci.html` (lignes 129 et 414).

## Action necessaire pour valider le test
1. Remplacer `REPLACE_WITH_YOUR_FORM_ID` par l'ID Formspree reel.
2. Remplacer le numero WhatsApp reel.
3. Remplacer `GTM-XXXXXXX` par ton ID GTM.
4. Remplacer `_next` par l'URL publique du site (ou `/merci.html` en relatif).

