---
layout: page
title: Projects
permalink: /projects/
description:
nav: true
nav_order: 2
#display_categories: [bioinformatics, daa]
horizontal: false
---
<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-3">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="row">
    {%- for project in sorted_projects -%}
      <div class="col-md-4 col-sm-6 mb-4">
        {% include projects.html %}
      </div>
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}
{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-3">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="row">
    {%- for project in sorted_projects -%}
      <div class="col-md-4 col-sm-6 mb-4">
        {% include projects.html %}
      </div>
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>
