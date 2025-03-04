---
description: Intégrez djLint avec votre éditeur préféré. Formatez automatiquement vos modèles avec Pre-Commit. Lint avec SublimeText.
title: Intégrations
keywords: template linter, template formatter, djLint, HTML, templates, formatter, linter, intégrations
---

# {{ "integrations" | i18n }}

Il existe plusieurs intégrations d'éditeurs construites pour djLint.

## Pre-Commit

djLint peut être utilisé comme un hook [pre-commit](https://pre-commit.com).

Le repo fournit de multiples hooks pré-configurés pour des profils djLint spécifiques (il suffit de prédéfinir l'argument `--profile` et d'indiquer à pre-commit les extensions de fichiers à rechercher) :

:: : contenu

- `djlint-django` pour les modèles Django :
  Il recherchera les fichiers correspondant à `templates/**.html` et définira `--profile=django`.
- `djlint-jinja`
  Ceci recherchera les fichiers correspondant à `*.j2` et définira `--profile=jinja`.
- `djlint-nunjucks`
  Cette commande recherchera les fichiers correspondant à `*.njk` et définira `--profile=nunjucks`.
- `djlint-handlebars`
  Ceci recherchera les fichiers correspondant à `*.hbs` et définira `--profile=handlebars`.
- `djlint-golang`
  Ceci recherchera les fichiers correspondant à `*.tmpl` et définira `--profile=golang`.
  :: :

Notez que ces hooks prédéfinis sont parfois trop conservateurs dans les entrées qu'ils acceptent (vos templates peuvent utiliser une extension différente) donc pre-commit vous permet explicitement de remplacer n'importe laquelle de ces options prédéfinies. Consultez la [docs pre-commit](https://pre-commit.com/#pre-commit-configyaml---hooks) pour une configuration supplémentaire.

### Exemple de Django par défaut

```yaml
repos:
  - repo: https://github.com/Riverside-Healthcare/djLint
    rev: 0.5.10 # grab latest tag from GitHub
    hooks:
      - id: djlint-django
```

### Handlebars avec l'extension .html au lieu de .hbs

```yaml
repos:
  - repo: https://github.com/Riverside-Healthcare/djLint
    rev: 0.5.10 # grab latest tag from GitHub
    hooks:
      - id: djlint-handlebars
        files: "\\.html"
        types_or: ['html']
```

Vous pouvez utiliser les paramètres `files` ou `exclude` pour contraindre chaque hook à son propre répertoire, ce qui vous permet de supporter plusieurs langages de template dans le même repo.

## Linter SublimeText

djLint peut être utilisé comme un plugin SublimeText Linter. Il peut être installé via [package-control](https://packagecontrol.io/packages/SublimeLinter-contrib-djlint).

:: : contenu

1. `cmd + shft + p`
2. Installer SublimeLinter
3. Installer SublimeLinter-contrib-djlint
   :: :

Assurez-vous que djLint est installé dans votre python global, ou sur votre `PATH`.

## Visual Studio Code

::: content

- [Page du marché](https://marketplace.visualstudio.com/items?itemName=monosans.djlint)
- [GitHub dépôt](https://github.com/monosans/djlint-vscode)
  :::

## neovim

djLint peut être utilisé comme formateur dans neovim en utilisant le plugin `null-ls`.

::: content

- [GitHub dépôt](https://github.com/jose-elias-alvarez/null-ls.nvim/)
- [Exemple de configuration](https://github.com/shaeinst/roshnivim/blob/5d991fcfa1b8f865f9653a98c6d97a829d4a2add/lua/plugins/null-ls_nvim.lua#L84-L91)
  :::

## coc.nvim

::: content

- [npm package](https://www.npmjs.com/package/coc-htmldjango)
  :::
