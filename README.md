# James C. Porter — Personal website

Source code for my personal, academic and professional website, including research, a project portfolio, writing, and CV material.

**Live website:** https://jamescporter.github.io/personal-website-v2/

## Structure

- `_pages/` — website pages, including research, projects, personal interests and CV.
- `_data/` — structured website content and configuration data.
- `_bibliography/` — publication references.
- `assets/` — images and other site assets.
- `_config.yml` — site identity, navigation-related settings and deployment URL.

## Development

This site uses [Jekyll](https://jekyllrb.com/) and is customised from the [al-folio](https://github.com/alshedivat/al-folio) academic website starter. Its dependencies are declared in `Gemfile` and `package.json`.

To work locally, install the Ruby dependencies and start Jekyll:

```bash
bundle install
bundle exec jekyll serve
```

The configured project-site path is `/personal-website-v2/`. For theme-specific setup and configuration, see [al-folio documentation](https://github.com/alshedivat/al-folio) and the documentation under `docs/` in this repository.

## Attribution

Based on the open-source **al-folio** project by its maintainers and contributors. This repository is a personal adaptation, not the official al-folio starter. See [LICENSE](LICENSE) and the [upstream project](https://github.com/alshedivat/al-folio) for licensing and attribution.
