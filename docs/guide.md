---
layout: default
title: User Guide
nav_order: 92
permalink: /guide/
last_modified_at: 2026-11-04
description: "UsTxGNN user guide: how to look up drugs, read evidence levels and interpret recommendations."
---

# User Guide

<div class="key-takeaway">
Check the evidence level first, then the recommendation, then read the source literature.
</div>

<p class="key-answer" data-question="Which medicines approved by the FDA have clinical trial evidence for a new indication?">
See the <a href="{{ '/evidence-high/' | relative_url }}">high</a> and
<a href="{{ '/evidence-medium/' | relative_url }}">moderate</a> evidence-level lists, or browse the full
<a href="{{ '/drugs/' | relative_url }}">All Drugs</a> directory. Each entry links to the NCT and PMID
records behind the evidence level.
</p>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## United States: a worked example from this site

Reading a report on this site takes three checks, in this order: evidence level, local market data, review log.

{% assign gx = site.data.local_facts.example %}
{% if gx %}Open [{{ gx.t }}]({{ gx.u | relative_url }}): the header shows evidence level **{{ gx.l }}**; the main predicted new indication is **{{ gx.i }}**; the local data list **{{ gx.lt }}** FDA applications (NDA/ANDA/BLA), **{{ gx.lv }}** of them marketed; the review log on the page has **{{ gx.r }}** entries.{% endif %}

{% if site.data.local_facts.most_reviewed.size > 0 %}Medicines with the most review-log entries: {% for r in site.data.local_facts.most_reviewed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.r }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Latest review-log corrections: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Examples of predictions that no other TxGNN site lists for the same medicine: [Bremelanotide]({{ '/drugs/bremelanotide/' | relative_url }}) → acne (disease), [Cevimeline]({{ '/drugs/cevimeline/' | relative_url }}) → hypertrichosis (disease), [Collagenase Clostridium Histolyticum]({{ '/drugs/collagenase-clostridium-histolyticum/' | relative_url }}) → primary release disorder of platelets, [Denileukin Diftitox]({{ '/drugs/denileukin-diftitox/' | relative_url }}) → plasmacytoma, [Diethylpropion]({{ '/drugs/diethylpropion/' | relative_url }}) → hypervitaminosis, [Diethyltoluamide]({{ '/drugs/diethyltoluamide/' | relative_url }}) → insomnia (disease).

<!-- local-facts:end -->

## Looking up a drug

<ol class="actionable-steps">
<li>Use the search box at the top of the page (generic ingredient names match better than brand names).</li>
<li>Or browse the full list on <a href="{{ '/drugs/' | relative_url }}">All Drugs</a>.</li>
<li>You can also browse by evidence level: <a href="{{ '/evidence-high/' | relative_url }}">high</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderate</a>, <a href="{{ '/evidence-low/' | relative_url }}">model prediction only</a>.</li>
</ol>

---

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## Reading a report

<p class="key-answer" data-question="What do evidence levels L1 to L5 mean?">
Each predicted indication carries a level from <strong>L1</strong> (several Phase 3 trials) to <strong>L5</strong> (model prediction only). Every piece of evidence cites an NCT or PMID number you can open; predictions are research leads, not clinical advice. Definitions and grading rules: <a href="{{ '/methodology/' | relative_url }}">Methodology</a>.
</p>
<!-- local-condensed:end -->

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
