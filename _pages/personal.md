---
layout: page
title: Personal
permalink: /personal/
description: Independent projects and creative interests.
nav: true
nav_order: 3
---

A space for projects beyond my academic work, including game modifications, custom maps, experiments and other interests.

{% assign personal_projects = site.projects | where: "category", "personal" | sort: "importance" %}
{% if personal_projects.size > 0 %}
<div class="projects">
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in personal_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
{% else %}
Personal projects will be added here as their pages are prepared.
{% endif %}
