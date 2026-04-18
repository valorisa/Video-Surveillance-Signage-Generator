# Générateur d'affiche réglementaire pour vidéoprotection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Conformité CSI](https://img.shields.io/badge/Conformit%C3%A9-CSI%20L223--1%20%C3%A0%20L255--1-blue)](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000025503132/LEGISCTA000025505703/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

Un outil simple, gratuit et open-source permettant de générer l'affichette d'information obligatoire conforme au Code de la sécurité intérieure française (articles L223-1 à L223-9 et L251-1 à L255-1). Destiné aux établissements équipés d'un système de vidéoprotection, ce générateur produit une affiche réglementaire prête à imprimer avec mention légale, numéro d'autorisation préfectorale, références juridiques et QR-code vers le site officiel de la CNIL.

---

## Présentation du projet

Ce générateur a été conçu pour aider les commerçants, artisans, gérants de restaurants, propriétaires de locaux commerciaux et responsables de lieux recevant du public (ERP) à se mettre en conformité avec la réglementation française sur la vidéoprotection.

L'outil produit une affiche réglementaire clé en main qui contient :
- La mention légale obligatoire « Établissement sous vidéo-protection »
- Le numéro d'autorisation préfectorale
- Les références des articles du Code de la sécurité intérieure
- Les coordonnées pour exercer le droit d'accès aux images
- Un QR-code pointing vers le site officiel de la CNIL

---

## Conformité légale

### Base juridique

L'affichage d'information sur la vidéoprotection est une obligation légale en France. Voici les textes applicables :

#### Articles du Code de la sécurité intérieure

- **L223-1 à L223-9** : Dispositions relatives à la vidéo-protection dans les lieux publics et ouverts au public
- **L251-1 à L255-1** : Dispositions relatives aux systèmes de vidéosurveillance dans les ERP

Ces articles définissent les obligations des exploitants de systèmes de vidéoprotection, notamment :
- L'obligation d'information du public (article L223-2)
- Les modalités d'exercice du droit d'accès aux images (article L253-1 et suivants)
- Les sanctions en cas de non-conformité (article L254-1)

#### Sanctions encourues

L'absence d'affichage peut entraîner :
- Une contravention de 5e classe (jusqu'à 1500 €)
- Des sanctions administratives supplémentaires
- La mise en demeure de mise en conformité par le préfet

### Source officielle

- [Code de la sécurité intérieure - Legifrance](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000025503132/LEGISCTA000025505703/)
- [CNIL - Vidéoprotection et droits des personnes](https://www.cnil.fr/fr/videoprotection-droits-des-personnes)

---

## Fonctionnalités

### Fonctionnalités principales

| Fonctionnalité | Description |
|----------------|-------------|
| **Génération de texte légal** | Production instantanée du texte conforme avec remplacement des variables |
| **QR-code intégré** | Génération automatique d'un QR-code vers la page CNIL |
| **Format vectoriel** | Sortie SVG pour intégration dans une charte graphique |
| **Format bitmap** | Sortie PNG 300 DPI pour impression directe |
| **Personnalisation** | Modification du template via fichier texte |

### Caractéristiques techniques

- **Langage** : Python 3.8+
- **Dépendances** : qrcode, Pillow (PIL)
- **Sortie** : PNG ou SVG
- **Taille QR-code** : >= 2x2 cm (respect de la norme)
- **Positionnement** : QR-code en bas à droite de l'affiche

---

## Installation

### Prérequis

Assurez-vous d'avoir installé Python 3.8 ou une version ultérieure sur votre système.

```bash
python --version
```

### Étape 1 : Cloner le dépôt

```bash
git clone https://github.com/valorisa/Video-Surveillance-Signage-Generator.git
cd Video-Surveillance-Signage-Generator
```

### Étape 2 : Installer les dépendances

```bash
pip install -r requirements.txt
```

Les dépendances nécessaires sont :
- `qrcode` : Génération du QR-code
- `Pillow` : Manipulation d'images

### Étape 3 : Vérifier l'installation

```bash
python src/generate_affiche.py --help
```

Vous devriez voir s'afficher l'aide du script.

---

## Utilisation

### Utilisation basique

La commande minimale nécessite deux paramètres :

```bash
python src/generate_affiche.py --autorisation "2024-12345" --telephone "01 23 45 67 89"
```

Cette commande génère :
- Un fichier `affiche_2024-12345.png` dans le dossier `output/`
- Un fichier `qrcode_2024-12345.png` pour le QR-code seul

### Utilisation avancée

#### Spécifier le format de sortie

```bash
python src/generate_affiche.py --autorisation "2024-12345" --telephone "01 23 45 67 89" --format png
```

Formats disponibles : `PNG` (défaut) ou `SVG`

#### Personnaliser le nom de sortie

```bash
python src/generate_affiche.py --autorisation "2024-12345" --telephone "01 23 45 67 89" --output mon_affiche
```

#### Combiner les options

```bash
python src/generate_affiche.py \
    --autorisation "2024-12345" \
    --telephone "09 69 36 20 06" \
    --format png \
    --output affiche_mon_commerce
```

---

## Personnalisation

### Modifier le texte de l'affiche

Le fichier `src/template.txt` contient le texte de l'affiche. Vous pouvez le modifier selon vos besoins tout en conservant les variables `{{NUMERO_AUTORISATION}}` et `{{TELEPHONE_RESPONSABLE}}`.

Exemple de template personnalisé :

```text
Mon Commerce sous vidéo-protection.

Autorisation préfectorale N° {{NUMERO_AUTORISATION}}

Conformément à la réglementation, nous vous informons que ce lieu est équipé d'un système de vidéosurveillance.

Articles L223-1 à L223-9 et L251-1 à L255-1 du Code de la sécurité intérieure

Pour toute demande relative à vos droits, contactez le responsable au {{TELEPHONE_RESPONSABLE}}.
```

### Modifier la police

Le script utilise par défaut la police Arial. Pour utiliser une autre police :

1. Placez votre fichier `.ttf` dans le dossier `fonts/`
2. Modifiez la variable `DEFAULT_FONT` dans `generate_affiche.py`

```python
DEFAULT_FONT = "OpenSans"  # Au lieu de "Arial"
```

### Ajouter un logo

Pour ajouter votre logo commercial, modifiez la fonction `create_affiche()` dans le script :

```python
logo = Image.open("chemin/vers/votre_logo.png")
logo = logo.resize((100, 100), Image.Resampling.LANCZOS)
img.paste(logo, (MARGIN, MARGIN), logo)
```

---

## Spécifications du QR-code

### Caractéristiques techniques

| Paramètre | Valeur |
|-----------|--------|
| URL encodée | https://www.cnil.fr/fr/videoprotection-droits-des-personnes |
| Niveau de correction d'erreur | Élevé (ERROR_CORRECT_H) |
| Taille minimale | 2x2 cm sur support imprimé |
| Format recommandé | PNG 300 DPI ou SVG |

### Positionnement

Le QR-code doit être placé :
- **Emplacement** : Coin inférieur droit de l'affiche
- **Marge de sécurité** : 5 mm minimum du bord
- **Zone de silence** : 4 modules delargeur autour du QR-code (respectés automatiquement par la bibliothèque)

### Texte d'accompagnement

Un texte optionnel peut être ajouté sous le QR-code :
> « Scannez pour connaître vos droits sur les images »

Ce texte est généré automatiquement par le script.

---

## Exemple de sortie

L'affiche générée contient les éléments suivants :

```
Etablissement sous vidéo-protection.

Conformément à l'autorisation préfectorale N° 2024-12345, nous vous informons que cet établissement est placé sous vidéo protection afin d'assurer la sécurité des biens et personnes.

Code de la sécurité intérieure (Livre II - Titre V) Articles L223-1 à L223-9 et L251-1 à L255-1

Pour toute question concernant votre droit d'accès aux images enregistrées, s'adresser au responsable sécurité au N° 01 23 45 67 89 ou à l'accueil du magasin auprès desquels vous pouvez exercer votre droit d'accès aux images vous concernant.

[QR-code en bas à droite]
Scannez pour connaître vos droits sur les images
```

---

## Foire aux questions

### Questions juridiques

**Q : L'affichage est-il vraiment obligatoire ?**

R : Oui. L'article L223-2 du Code de la sécurité intérieure impose une information claire et permanente du public. L'absence d'affichage constitue une infraction passible de sanctions.

**Q : Puis-je modifier le texte de l'affiche ?**

R : Vous pouvez modifier le texte tant qu'il contient les mentions obligatoires : mention « vidéoprotection », numéro d'autorisation, références légales, et modalités d'exercice du droit d'accès.

**Q : Le QR-code vers la CNIL est-il obligatoire ?**

R : Non, ce n'est pas une obligation légale. Cependant, il est recommandé car la CNIL est l'autorité de contrôle en matière de données personnelles et offre des informations complètes sur les droits des personnes filmées.

**Q : Que faire si je n'ai pas encore mon numéro d'autorisation ?**

R : Vous devez obtenir l'autorisation préfectorale avant d'installer un système de vidéoprotection. Contactez la préfecture de votre département. En attendant, vous pouvez mentionner « Autorisation en cours de demande » mais vous devez régulariser la situation.

### Questions techniques

**Q : Le script fonctionne-t-il sur Windows ?**

R : Oui, le script est compatible avec Windows, macOS et Linux.

**Q : Comment générer plusieurs affiches à la fois ?**

R : Vous pouvez créer un script bash ou Python qui boucle sur plusieurs numéros d'autorisation :

```bash
for auth in "2024-0001" "2024-0002" "2024-0003"; do
    python src/generate_affiche.py --autorisation "$auth" --telephone "01 23 45 67 89"
done
```

**Q : Puis-je utiliser une image de fond ?**

R : Oui, modifiez la fonction `create_affiche()` pour charger une image de fond au lieu de créer un fond blanc.

---

## Contribuer

Les contributions sont les bienvenues ! Pour participer au développement :

1. Forkez le projet sur GitHub
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`)
3. Commitez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/ma-fonctionnalite`)
5. Ouvrez une Pull Request

### Vérifications avant soumission

Avant de soumettre une contribution, vérifiez que :
- Le code respecte les conventions Python (PEP 8)
- Les tests existants passent
- Les mentions légales restent conformes au CSI

---

## Avertissements

1. **Ce n'est pas un conseil juridique.** Pour des questions spécifiques à votre situation, consultez un avocat spécialisé ou votre préfecture.

2. **Vérifiez toujours les exigences locales.** Certaines préfectures peuvent avoir des exigences spécifiques.

3. **Maintenez à jour vos autorisations.** Les autorisations préfectorales ont une durée limitée et doivent être renouvelées.

---

## Licence

Ce projet est distribué sous licence **MIT**. Vous êtes libre de l'utiliser, de le modifier et de le distribuer, y compris à des fins commerciales, sous réserve de conserver la notice de copyright et la clause de non-responsabilité.

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Références

- [Legifrance - Code de la sécurité intérieure](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000025503132/LEGISCTA000025505703/)
- [CNIL - Vidéoprotection : vos droits](https://www.cnil.fr/fr/videoprotection-droits-des-personnes)
- [Service-public.fr - Vidéosurveillance](https://www.service-public.fr/particuliers/vosdroits/F35084)

---

**Générateur d'affiche vidéoprotection** — Un outil simple pour rester en conformité avec la réglementation française, sans tracas.
