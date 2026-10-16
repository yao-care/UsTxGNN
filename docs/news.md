---
layout: default
title: Health News
nav_order: 90
description: "Health news about drugs with repurposing reports on UsTxGNN"
permalink: /news/
---

# Health News
{: .fs-9 }

News pages for drugs with repurposing reports on UsTxGNN. Each page links back to the drug report.
{: .fs-6 .fw-300 }

{% assign items = site.news | sort: 'title' %}
<ul>
{% for n in items %}<li><a href="{{ n.url | relative_url }}">{{ n.title }}</a></li>
{% endfor %}</ul>
