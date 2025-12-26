---
title: Contact / Contacto
nav:
  order: 4
  tooltip: How to reach us
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

We would love to hear from you! / Nos encantaría saber de usted.

{%
  include button.html
  type="email"
  text="pablo.iturralde@ucu.edu.uy"
  link="pablo.iturralde@ucu.edu.uy"
%}
{%
  include button.html
  type="email"
  text="enrique.ferreira@ucu.edu.uy"
  link="enrique.ferreira@ucu.edu.uy"
%}

{% include section.html %}

## Location / Ubicación

Universidad Católica del Uruguay
Facultad de Ingeniería y Tecnologías
Av. 8 de Octubre 2738
Montevideo, Uruguay

{%
  include figure.html
  image="images/ucu-campus.jpg"
  caption="Universidad Católica del Uruguay"
%}

{% include section.html %}

## Social

{% include list.html data="members" component="portrait" filters="role: pi" %}

{% for link in site.links %}
{% if link[1] != "" %}
{%
  include button.html
  type="{{ link[0] }}"
  link="{{ link[1] }}"
  text="{{ link[0] | capitalize }}"
%}
{% endif %}
{% endfor %}
