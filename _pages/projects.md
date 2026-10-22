---
layout: page
title: Portfolio
permalink: /portfolio/
description: Selected research, software and technically relevant projects.
nav: true
nav_order: 2
---

Selected research, software and independent technical work relevant to my professional interests.

<section class="site-section" aria-labelledby="retfound-project">
  <article class="site-record">
    <p class="site-meta">Research software · Published package · 2026</p>
    <h2 id="retfound-project">RETFound: unofficial Python packaging</h2>
    <p>I develop and maintain an installable distribution of the existing RETFound code for secure research environments where direct repository downloads may be restricted.</p>
    <p><strong>Contribution:</strong> packaging, distribution and deployment. The original foundation model, architecture and research belong to the upstream RETFound authors. Pretrained weights are obtained separately.</p>
    <div class="site-actions">
      <a href="https://github.com/jamescporter/Unofficial_RETFound_pip">Source and documentation</a>
      <a href="https://pypi.org/project/retfound-unofficial/">PyPI package</a>
      <a href="https://doi.org/10.5281/zenodo.22129620">DOI: 10.5281/zenodo.22129620</a>
      <a href="https://github.com/rmaphoh/RETFound">Original RETFound project</a>
    </div>
  </article>
</section>

{% assign portfolio_projects = site.projects | where: "category", "portfolio" | sort: "importance" %}
{% for project in portfolio_projects %}
  <article class="site-record">
    <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
    <p>{{ project.description }}</p>
  </article>
{% endfor %}
