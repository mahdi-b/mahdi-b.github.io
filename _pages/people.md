---
layout: page
title: People
permalink: /people/
description: Researchers building new computational methods for biology, language, and scientific collaboration.
nav: true
nav_order: 3
---
<div class="people">
  <p class="category">CURRENT LAB</p>
  {% assign current_people = site.people | where: "category", "current" | sort: "importance" %}
  <div class="container mb-5">
    <div class="row row-cols-2">
      {% for person in current_people %}{% include people_horizontal.html %}{% endfor %}
    </div>
  </div>

  <section class="alumni-section">
    <p class="category">LAB ALUMNI</p>
    <div class="alumni-list">
      <p><strong>Candace Edwards</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Andy Yu</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Cedric Arisdakessian</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Michael Rogers</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Nima Azbijari</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Sushil Shrestha</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Ethan Chow</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Gum Aung</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Kameron Wong</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Lucy Rock</strong><span>Information &amp; Computer Sciences</span></p>
      <p><strong>Jaclyn Lee</strong><span>Economics · Data Science Fellow</span></p>
      <p><strong>Sean Takafuji</strong><span>ICS · Data Science Fellow</span></p>
      <p><strong>Layn Fujioka</strong><span>Physics · Data Science Fellow</span></p>
      <p><strong>Charles Dickens</strong><span>Electrical Engineering · Data Science Fellow</span></p>
      <p><strong>Tristan McKenzie</strong><span>Earth Sciences · Data Science Fellow</span></p>
      <p><strong>Charlotte Smith</strong><span>NREM · Data Science Fellow</span></p>
    </div>
  </section>
</div>
