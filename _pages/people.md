---
layout: page
title: People
permalink: /people/
description: Current and Former Members
nav: true
nav_order: 2
display_categories: [current]
horizontal: true
---
<div class="people">
  {% if site.enable_people_categories and page.display_categories %}
    <!-- Display categorized people -->
    {% for category in page.display_categories %}
      <h2 class="category mb-3">{{ category | upcase }}</h2> <!-- Added mb-3 for bottom margin -->
      {% assign categorized_people = site.people | where: "category", category %}
      {% assign sorted_people = categorized_people | sort: "name" %}

      <!-- Generate cards for each person -->
      {% if page.horizontal %}
        <div class="container mb-3"> <!-- Added mb-3 for bottom margin -->
          <div class="row row-cols-2">
            {% for person in sorted_people %}
              {% include people_horizontal.html %}
            {% endfor %}
          </div>
        </div>
      {% else %}
        <div class="grid mb-3"> <!-- Added mb-3 for bottom margin -->
          {% for person in sorted_people %}
            {% include person.html %}
          {% endfor %}
        </div>
      {% endif %}
    {% endfor %}
{% else %}
<!-- Display people without categories -->
{% assign sorted_people = site.people | sort: "name" %}

    <!-- Generate cards for each person -->
    {% if page.horizontal %}
      <div class="container mb-3"> <!-- Added mb-3 for bottom margin -->
        <div class="row row-cols-2">
          {% for person in sorted_people %}
            {% include people_horizontal.html %}
          {% endfor %}
        </div>
      </div>
    {% else %}
      <div class="grid mb-3"> <!-- Added mb-3 for bottom margin -->
        {% for person in sorted_people %}
          {% include person.html %}
        {% endfor %}
      </div>
    {% endif %}
{% endif %}

<h2 class="category mb-3">{{ "Former" | upcase }}</h2> <!-- Added mb-3 for bottom margin -->


<h3 class="card-title truncate-text">{{ "Candace Edwards" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Andy Yu" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Cedric Arisdakessian" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Michael Rogers" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Nima Azbijari" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Sushil Shrestha" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Ethan Chow" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Gum Aung" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Kameron Wong" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Lucy Rock" | uppercase }}, ICS</h3>
<h3 class="card-title truncate-text">{{ "Jaclyn Lee" | uppercase }}, Econ - Data Science Fellow</h3>
<h3 class="card-title truncate-text">{{ "Sean Takafuji" | uppercase }}, ICS - Data Science Fellow</h3>
<h3 class="card-title truncate-text">{{ "Layn Fujioka" | uppercase }}, Physics - Data Science Fellow</h3>
<h3 class="card-title truncate-text">{{ "Charles Dickens" | uppercase }}, EE - Data Science Fellow</h3>
<h3 class="card-title truncate-text">{{ "Tristan McKenzie" | uppercase }}, Earth Sciences - Data Science Fellow</h3>
<h3 class="card-title truncate-text">{{ "Charlotte Smith" | uppercase }}, NREM - Data Science Fellow</h3>





