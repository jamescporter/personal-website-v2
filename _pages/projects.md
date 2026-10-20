---
layout: page
title: Portfolio
permalink: /portfolio/
description: Selected research, software and technically relevant projects.
nav: true
nav_order: 2
---

Selected research, software and independent technical work relevant to my professional interests.

{% assign portfolio_projects = site.projects | where: "category", "portfolio" | sort: "importance" %}
{% if portfolio_projects.size > 0 %}
<div class="projects">
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in portfolio_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
{% else %}
Projects will be added here as their summaries and links are prepared.
{% endif %}
